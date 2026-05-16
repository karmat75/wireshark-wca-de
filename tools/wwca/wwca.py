#!/usr/bin/env python3
"""wwca - local helper tool for the Wireshark WCA DE course."""

import argparse
import datetime as dt
import json
import random
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required but not installed.", file=sys.stderr)
    print("Install it with: python3 -m pip install PyYAML", file=sys.stderr)
    sys.exit(2)

APP_NAME = "wireshark-wca-de"
COURSE_VERSION = "0.1.0"


def repo_root():
    return Path(__file__).resolve().parents[2]


def quiz_dir():
    return repo_root() / "quizzes" / "questions"


def progress_path():
    return Path.home() / ".local" / "share" / APP_NAME / "progress.json"


def now_iso():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def load_yaml(path):
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: YAML root must be a mapping")
    return data


def load_quizzes():
    result = {}
    qdir = quiz_dir()
    if not qdir.exists():
        return result
    for path in sorted(qdir.glob("*.yml")):
        data = load_yaml(path)
        quiz_id = str(data.get("id") or path.stem)
        data["_path"] = str(path.relative_to(repo_root()))
        result[quiz_id] = data
    return result


def load_progress():
    path = progress_path()
    if not path.exists():
        return {"course_version": COURSE_VERSION, "created_at": now_iso(), "updated_at": now_iso(), "attempts": []}
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data.get("attempts"), list):
        data["attempts"] = []
    return data


def save_progress(data):
    path = progress_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = now_iso()
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def parse_answer(value):
    value = value.strip()
    if not value:
        return []
    parts = value.replace(";", ",").replace(" ", ",").split(",")
    numbers = []
    for part in parts:
        if not part:
            continue
        try:
            numbers.append(int(part))
        except ValueError:
            return []
    return sorted(set(numbers))


def is_correct(question, selected):
    answers = question.get("answers") or []
    selected_indexes = {number - 1 for number in selected}
    correct_indexes = {idx for idx, answer in enumerate(answers) if bool(answer.get("correct"))}
    return selected_indexes == correct_indexes


def score_label(score):
    if score >= 90:
        return "sehr sicher"
    if score >= 80:
        return "prüfungsnah gut"
    if score >= 70:
        return "solide, Lücken prüfen"
    if score >= 60:
        return "Grundlagen wiederholen"
    return "Thema erneut durcharbeiten"


def quiz_list(_args):
    quizzes = load_quizzes()
    if not quizzes:
        print("No quizzes found.")
        return 1
    width = min(shutil.get_terminal_size((100, 20)).columns, 100)
    print("\nVerfügbare Quizzes")
    print("-" * width)
    for quiz_id, quiz in sorted(quizzes.items()):
        questions = quiz.get("questions") or []
        print(f"{quiz_id:16} {len(questions):3} Fragen  {quiz.get('title', '')}")
        if quiz.get("description"):
            print(f"{'':16}     {quiz.get('description')}")
        print(f"{'':16}     {quiz.get('_path', '')}\n")
    return 0


def validate_file(path, data):
    errors = []
    if not data.get("id"):
        errors.append(f"{path}: missing quiz id")
    questions = data.get("questions")
    if not isinstance(questions, list) or not questions:
        errors.append(f"{path}: no questions")
        return errors
    seen = set()
    for index, question in enumerate(questions, start=1):
        prefix = f"{path}: question #{index}"
        if not isinstance(question, dict):
            errors.append(f"{prefix}: must be a mapping")
            continue
        qid = question.get("id")
        if not qid:
            errors.append(f"{prefix}: missing id")
        elif qid in seen:
            errors.append(f"{prefix}: duplicate id {qid}")
        else:
            seen.add(qid)
        for field in ("type", "objective", "question", "explanation"):
            if not question.get(field):
                errors.append(f"{prefix}: missing {field}")
        answers = question.get("answers")
        if not isinstance(answers, list) or not answers:
            errors.append(f"{prefix}: missing answers")
        else:
            if not any(isinstance(answer, dict) and answer.get("correct") for answer in answers):
                errors.append(f"{prefix}: no correct answer")
            for answer_index, answer in enumerate(answers, start=1):
                if not isinstance(answer, dict) or not answer.get("text"):
                    errors.append(f"{prefix}: answer #{answer_index} missing text")
        refs = question.get("references")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{prefix}: missing references")
    return errors


def quiz_validate(_args):
    qdir = quiz_dir()
    if not qdir.exists():
        print(f"ERROR: quiz directory not found: {qdir}", file=sys.stderr)
        return 2
    errors = []
    for path in sorted(qdir.glob("*.yml")):
        try:
            data = load_yaml(path)
            errors.extend(validate_file(path, data))
        except Exception as exc:
            errors.append(f"{path}: {exc}")
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Quiz validation passed.")
    return 0


def run_quiz(args):
    quizzes = load_quizzes()
    quiz = quizzes.get(args.quiz_id)
    if quiz is None:
        print(f"ERROR: quiz not found: {args.quiz_id}", file=sys.stderr)
        print("Available quizzes:", file=sys.stderr)
        for quiz_id in sorted(quizzes):
            print(f"  {quiz_id}", file=sys.stderr)
        return 2
    questions = list(quiz.get("questions") or [])
    if args.shuffle:
        random.shuffle(questions)
    if args.limit is not None:
        questions = questions[: args.limit]
    if not questions:
        print("No questions found.")
        return 1

    print(f"\nQuiz: {quiz.get('title', quiz.get('id', args.quiz_id))}")
    print(f"Datei: {quiz.get('_path', '')}")
    print(f"Fragen: {len(questions)}")
    print("\nEingabe: Single Choice = 1, Multiple Choice = 1,3,4\n")

    correct_count = 0
    answered = []
    for index, question in enumerate(questions, start=1):
        answers = question.get("answers") or []
        print("=" * 78)
        print(f"Frage {index}/{len(questions)} | {question.get('id')} | {question.get('type')} | {question.get('objective')}\n")
        print(question.get("question", "<no question text>"))
        print()
        for answer_index, answer in enumerate(answers, start=1):
            print(f"  {answer_index}. {answer.get('text', '')}")
        print()
        selected = parse_answer(input("Antwort: "))
        ok = is_correct(question, selected)
        if ok:
            correct_count += 1
        correct_numbers = [str(i + 1) for i, answer in enumerate(answers) if answer.get("correct")]
        print("\n" + ("RICHTIG" if ok else "FALSCH"))
        print("Richtige Antwort(en): " + ", ".join(correct_numbers))
        if question.get("explanation"):
            print("\nErklärung:")
            print(question["explanation"])
        refs = question.get("references") or []
        if refs:
            print("\nReferenzen:")
            for ref in refs:
                print(f"  - {ref}")
        print()
        answered.append({"id": question.get("id"), "objective": question.get("objective"), "selected": selected, "correct": ok})

    total = len(questions)
    score = round(correct_count / total * 100, 2)
    print("=" * 78)
    print("Ergebnis")
    print(f"Richtig: {correct_count}/{total}")
    print(f"Score:   {score:.2f}%")
    print(f"Bewertung: {score_label(score)}")

    progress = load_progress()
    progress.setdefault("attempts", []).append({
        "kind": "quiz",
        "quiz_id": args.quiz_id,
        "quiz_title": quiz.get("title"),
        "timestamp": now_iso(),
        "question_count": total,
        "correct_count": correct_count,
        "score": score,
        "passed": score >= 80,
        "shuffle": bool(args.shuffle),
        "limit": args.limit,
        "answers": answered,
    })
    save_progress(progress)
    print(f"\nFortschritt gespeichert: {progress_path()}")
    return 0 if score >= 60 else 1


def progress_show(_args):
    progress = load_progress()
    attempts = progress.get("attempts") or []
    print(f"\nProgress file: {progress_path()}")
    print(f"Attempts:      {len(attempts)}\n")
    if not attempts:
        print("No attempts recorded yet.")
        return 0
    for attempt in attempts[-10:]:
        print(
            f"{attempt.get('timestamp', '')}  "
            f"{attempt.get('quiz_id', ''):16} "
            f"{attempt.get('correct_count', 0)}/{attempt.get('question_count', 0)}  "
            f"{attempt.get('score', 0):.2f}%  "
            f"{'passed' if attempt.get('passed') else 'not passed'}"
        )
    return 0


def progress_export(args):
    source = progress_path()
    if not source.exists():
        print("No progress file exists yet.")
        return 1
    dest = Path(args.path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)
    print(f"Exported progress to: {dest}")
    return 0


def progress_reset(_args):
    path = progress_path()
    if not path.exists():
        print("No progress file exists.")
        return 0
    print(f"This will delete: {path}")
    if input("Type DELETE to continue: ").strip() != "DELETE":
        print("Aborted.")
        return 1
    path.unlink()
    print("Progress deleted.")
    return 0


def build_parser():
    parser = argparse.ArgumentParser(prog="wwca", description="Local helper tool for Wireshark WCA DE course.")
    sub = parser.add_subparsers(dest="command")

    quiz = sub.add_parser("quiz", help="Quiz commands")
    quiz_sub = quiz.add_subparsers(dest="quiz_command")
    q_list = quiz_sub.add_parser("list", help="List quizzes")
    q_list.set_defaults(func=quiz_list)
    q_validate = quiz_sub.add_parser("validate", help="Validate quiz YAML files")
    q_validate.set_defaults(func=quiz_validate)
    q_run = quiz_sub.add_parser("run", help="Run a quiz")
    q_run.add_argument("quiz_id", help="Quiz id, e.g. foundation or basic")
    q_run.add_argument("--limit", type=int, default=None, help="Limit number of questions")
    q_run.add_argument("--shuffle", action="store_true", help="Shuffle questions")
    q_run.set_defaults(func=run_quiz)

    progress = sub.add_parser("progress", help="Show or manage progress")
    progress_sub = progress.add_subparsers(dest="progress_command")
    p_show = progress_sub.add_parser("show", help="Show progress")
    p_show.set_defaults(func=progress_show)
    p_export = progress_sub.add_parser("export", help="Export progress JSON")
    p_export.add_argument("path", help="Destination JSON file")
    p_export.set_defaults(func=progress_export)
    p_reset = progress_sub.add_parser("reset", help="Reset local progress")
    p_reset.set_defaults(func=progress_reset)
    parser.set_defaults(func=None)
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "progress" and args.progress_command is None:
        return progress_show(args)
    if args.func is None:
        parser.print_help()
        return 2
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
