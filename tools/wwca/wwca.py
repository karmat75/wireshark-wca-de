#!/usr/bin/env python3
"""
wwca - local helper tool for the Wireshark WCA DE course.

This tool intentionally stays small and local-only.

Supported commands:
  wwca quiz list
  wwca quiz validate
  wwca quiz run <quiz-id>
  wwca exam list
  wwca exam validate
  wwca exam run <exam-id>
  wwca progress
  wwca progress export <path>
  wwca progress reset
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import random
import shutil
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required but not installed.", file=sys.stderr)
    print("Install it with: python3 -m pip install PyYAML", file=sys.stderr)
    sys.exit(2)


APP_NAME = "wireshark-wca-de"
COURSE_VERSION = "0.1.0"


def repo_root() -> Path:
    here = Path(__file__).resolve()
    return here.parents[2]


def quiz_dir() -> Path:
    return repo_root() / "quizzes" / "questions"


def exam_dir() -> Path:
    return repo_root() / "quizzes" / "exams"


def progress_path() -> Path:
    return Path.home() / ".local" / "share" / APP_NAME / "progress.json"


def utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def load_yaml_file(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: YAML root must be a mapping")
    return data


def load_quizzes() -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Dict[str, Any]] = {}
    qdir = quiz_dir()
    if not qdir.exists():
        return result

    for path in sorted(qdir.glob("*.yml")):
        data = load_yaml_file(path)
        quiz_id = str(data.get("id") or path.stem)
        data["_path"] = str(path.relative_to(repo_root()))
        result[quiz_id] = data

    return result


def load_exams() -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Dict[str, Any]] = {}
    edir = exam_dir()
    if not edir.exists():
        return result

    for path in sorted(edir.glob("*.yml")):
        data = load_yaml_file(path)
        exam_id = str(data.get("id") or path.stem)
        data["_path"] = str(path.relative_to(repo_root()))
        result[exam_id] = data

    return result


def load_progress() -> Dict[str, Any]:
    path = progress_path()
    if not path.exists():
        return {
            "course_version": COURSE_VERSION,
            "created_at": utc_now(),
            "updated_at": utc_now(),
            "attempts": [],
        }

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if "attempts" not in data or not isinstance(data["attempts"], list):
        data["attempts"] = []

    return data


def save_progress(data: Dict[str, Any]) -> None:
    path = progress_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = utc_now()
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def normalize_answer_input(value: str) -> List[int]:
    value = value.strip()
    if not value:
        return []

    parts = value.replace(";", ",").replace(" ", ",").split(",")
    numbers: List[int] = []
    for part in parts:
        if not part:
            continue
        try:
            numbers.append(int(part))
        except ValueError:
            return []
    return sorted(set(numbers))


def question_correct(question: Dict[str, Any], selected_numbers: List[int]) -> bool:
    answers = question.get("answers") or []
    selected_indexes = {n - 1 for n in selected_numbers}
    correct_indexes = {idx for idx, answer in enumerate(answers) if bool(answer.get("correct"))}
    return selected_indexes == correct_indexes


def correct_answer_numbers(question: Dict[str, Any]) -> List[str]:
    answers = question.get("answers") or []
    return [str(i + 1) for i, answer in enumerate(answers) if bool(answer.get("correct"))]


def format_question_header(index: int, total: int, question: Dict[str, Any]) -> str:
    qid = question.get("id", "<no-id>")
    qtype = question.get("type", "<no-type>")
    objective = question.get("objective", "<no-objective>")
    return f"Frage {index}/{total} | {qid} | {qtype} | {objective}"


def score_label(score: float) -> str:
    if score >= 90:
        return "sehr sicher"
    if score >= 80:
        return "prüfungsnah gut"
    if score >= 70:
        return "solide, Lücken prüfen"
    if score >= 60:
        return "Grundlagen wiederholen"
    return "Thema erneut durcharbeiten"


def ask_questions(
    *,
    title: str,
    source_label: str,
    questions: List[Dict[str, Any]],
    pass_score: float,
    mode: str,
    time_limit_minutes: Optional[int] = None,
) -> Tuple[int, int, float, List[Dict[str, Any]]]:
    if not questions:
        raise ValueError("No questions to ask")

    print()
    print(f"{mode.title()}: {title}")
    print(f"Quelle: {source_label}")
    print(f"Fragen: {len(questions)}")
    if time_limit_minutes:
        print(f"Zeitlimit: {time_limit_minutes} Minuten (Hinweis, aktuell kein harter Abbruch)")
    print()
    print("Eingabe:")
    print("  Single Choice: 1")
    print("  Multiple Choice: 1,3,4")
    print()

    correct_count = 0
    answered: List[Dict[str, Any]] = []
    started = time.monotonic()

    for idx, question in enumerate(questions, start=1):
        qtype = str(question.get("type", "single-choice"))
        answers = question.get("answers") or []

        print("=" * 78)
        print(format_question_header(idx, len(questions), question))
        print()
        print(question.get("question", "<no question text>"))
        print()

        for ans_idx, answer in enumerate(answers, start=1):
            print(f"  {ans_idx}. {answer.get('text', '')}")

        print()
        raw = input("Antwort: ")
        selected = normalize_answer_input(raw)

        is_correct = question_correct(question, selected)
        if is_correct:
            correct_count += 1

        if mode == "quiz":
            status = "RICHTIG" if is_correct else "FALSCH"
            print()
            print(status)
            print(f"Richtige Antwort(en): {', '.join(correct_answer_numbers(question))}")

            explanation = question.get("explanation")
            if explanation:
                print()
                print("Erklärung:")
                print(explanation)

            references = question.get("references") or []
            if references:
                print()
                print("Referenzen:")
                for ref in references:
                    print(f"  - {ref}")

            print()
        else:
            print("Antwort gespeichert.")
            print()

        answered.append(
            {
                "id": question.get("id"),
                "type": qtype,
                "objective": question.get("objective"),
                "selected": selected,
                "correct": is_correct,
                "correct_answers": correct_answer_numbers(question),
            }
        )

    elapsed_seconds = int(time.monotonic() - started)
    total = len(questions)
    score = round((correct_count / total) * 100, 2)

    print("=" * 78)
    print("Ergebnis")
    print(f"Richtig: {correct_count}/{total}")
    print(f"Score:   {score:.2f}%")
    print(f"Bewertung: {score_label(score)}")
    print(f"Dauer: {elapsed_seconds // 60}m {elapsed_seconds % 60}s")
    print(f"Bestanden: {'ja' if score >= pass_score else 'nein'} (Grenze: {pass_score:.0f}%)")

    if mode == "exam":
        print()
        print("Auswertung")
        for idx, question in enumerate(questions, start=1):
            result = answered[idx - 1]
            status = "RICHTIG" if result["correct"] else "FALSCH"
            print("-" * 78)
            print(format_question_header(idx, len(questions), question))
            print(status)
            print(f"Deine Antwort(en): {', '.join(str(x) for x in result['selected']) or '-'}")
            print(f"Richtige Antwort(en): {', '.join(result['correct_answers'])}")

            explanation = question.get("explanation")
            if explanation:
                print()
                print("Erklärung:")
                print(explanation)

            references = question.get("references") or []
            if references:
                print()
                print("Referenzen:")
                for ref in references:
                    print(f"  - {ref}")

    return correct_count, total, score, answered


def run_quiz(args: argparse.Namespace) -> int:
    quizzes = load_quizzes()
    quiz = quizzes.get(args.quiz_id)

    if quiz is None:
        print(f"ERROR: quiz not found: {args.quiz_id}", file=sys.stderr)
        print("Available quizzes:", file=sys.stderr)
        for qid in sorted(quizzes):
            print(f"  {qid}", file=sys.stderr)
        return 2

    questions = list(quiz.get("questions") or [])
    if args.shuffle:
        random.shuffle(questions)

    if args.limit is not None:
        questions = questions[: args.limit]

    if not questions:
        print("No questions found.")
        return 1

    correct_count, total, score, answered = ask_questions(
        title=str(quiz.get("title", quiz.get("id", args.quiz_id))),
        source_label=str(quiz.get("_path", "")),
        questions=questions,
        pass_score=80,
        mode="quiz",
    )

    progress = load_progress()
    progress.setdefault("attempts", []).append(
        {
            "kind": "quiz",
            "quiz_id": args.quiz_id,
            "quiz_title": quiz.get("title"),
            "timestamp": utc_now(),
            "question_count": total,
            "correct_count": correct_count,
            "score": score,
            "passed": score >= 80,
            "shuffle": bool(args.shuffle),
            "limit": args.limit,
            "answers": answered,
        }
    )
    save_progress(progress)

    print()
    print(f"Fortschritt gespeichert: {progress_path()}")

    return 0 if score >= 60 else 1


def quiz_list(_args: argparse.Namespace) -> int:
    quizzes = load_quizzes()

    if not quizzes:
        print("No quizzes found.")
        return 1

    width = shutil.get_terminal_size((100, 20)).columns
    print()
    print("Verfügbare Quizzes")
    print("-" * min(width, 100))

    for qid, quiz in sorted(quizzes.items()):
        questions = quiz.get("questions") or []
        print(f"{qid:16} {len(questions):3} Fragen  {quiz.get('title', '')}")
        desc = quiz.get("description")
        if desc:
            print(f"{'':16}     {desc}")
        print(f"{'':16}     {quiz.get('_path', '')}")
        print()

    return 0


def validate_quiz_file(path: Path, data: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    quiz_id = data.get("id")
    if not quiz_id:
        errors.append(f"{path}: missing quiz id")

    questions = data.get("questions")
    if not isinstance(questions, list) or not questions:
        errors.append(f"{path}: no questions")
        return errors

    seen_ids = set()

    for index, q in enumerate(questions, start=1):
        prefix = f"{path}: question #{index}"
        if not isinstance(q, dict):
            errors.append(f"{prefix}: must be a mapping")
            continue

        qid = q.get("id")
        if not qid:
            errors.append(f"{prefix}: missing id")
        elif qid in seen_ids:
            errors.append(f"{prefix}: duplicate id {qid}")
        else:
            seen_ids.add(qid)

        if not q.get("type"):
            errors.append(f"{prefix}: missing type")

        if not q.get("objective"):
            errors.append(f"{prefix}: missing objective")

        if not q.get("question"):
            errors.append(f"{prefix}: missing question")

        answers = q.get("answers")
        if not isinstance(answers, list) or not answers:
            errors.append(f"{prefix}: missing answers")
        else:
            correct = [a for a in answers if isinstance(a, dict) and bool(a.get("correct"))]
            if not correct:
                errors.append(f"{prefix}: no correct answer")
            for a_idx, answer in enumerate(answers, start=1):
                if not isinstance(answer, dict) or not answer.get("text"):
                    errors.append(f"{prefix}: answer #{a_idx} missing text")

        if not q.get("explanation"):
            errors.append(f"{prefix}: missing explanation")

        refs = q.get("references")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{prefix}: missing references")

    return errors


def quiz_validate(_args: argparse.Namespace) -> int:
    qdir = quiz_dir()
    if not qdir.exists():
        print(f"ERROR: quiz directory not found: {qdir}", file=sys.stderr)
        return 2

    all_errors: List[str] = []

    for path in sorted(qdir.glob("*.yml")):
        try:
            data = load_yaml_file(path)
        except Exception as exc:
            all_errors.append(f"{path}: {exc}")
            continue
        all_errors.extend(validate_quiz_file(path, data))

    if all_errors:
        print("Validation failed:")
        for error in all_errors:
            print(f"  - {error}")
        return 1

    print("Quiz validation passed.")
    return 0


def build_exam_questions(exam: Dict[str, Any], quizzes: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    sections = exam.get("sections") or []
    if not isinstance(sections, list) or not sections:
        raise ValueError("exam has no sections")

    final_questions: List[Dict[str, Any]] = []

    for section in sections:
        pool_id = section.get("pool")
        count = int(section.get("count", 0))
        if pool_id not in quizzes:
            raise ValueError(f"exam references unknown pool: {pool_id}")

        pool_questions = list(quizzes[pool_id].get("questions") or [])
        if count <= 0:
            raise ValueError(f"section {pool_id}: count must be > 0")
        if count > len(pool_questions):
            raise ValueError(f"section {pool_id}: requested {count}, available {len(pool_questions)}")

        random.shuffle(pool_questions)
        selected = pool_questions[:count]

        for q in selected:
            q = dict(q)
            q["_pool"] = pool_id
            final_questions.append(q)

    if bool(exam.get("shuffle", True)):
        random.shuffle(final_questions)

    return final_questions


def exam_list(_args: argparse.Namespace) -> int:
    exams = load_exams()
    if not exams:
        print("No exams found.")
        return 1

    print()
    print("Verfügbare Modulprüfungen")
    print("-" * 100)

    for exam_id, exam in sorted(exams.items()):
        sections = exam.get("sections") or []
        total = sum(int(s.get("count", 0)) for s in sections if isinstance(s, dict))
        pass_score = float(exam.get("pass_score", 80))
        time_limit = exam.get("time_limit_minutes", "-")
        print(f"{exam_id:24} {total:3} Fragen  pass {pass_score:.0f}%  {time_limit} min  {exam.get('title', '')}")
        desc = exam.get("description")
        if desc:
            print(f"{'':24}     {desc}")
        print(f"{'':24}     {exam.get('_path', '')}")
        print()

    return 0


def exam_validate(_args: argparse.Namespace) -> int:
    quizzes = load_quizzes()
    exams = load_exams()
    errors: List[str] = []

    if not exams:
        errors.append("no exam files found")

    for exam_id, exam in sorted(exams.items()):
        prefix = exam.get("_path", exam_id)
        if not exam.get("id"):
            errors.append(f"{prefix}: missing id")
        if not exam.get("title"):
            errors.append(f"{prefix}: missing title")
        if not isinstance(exam.get("sections"), list) or not exam.get("sections"):
            errors.append(f"{prefix}: missing sections")
            continue

        for section in exam.get("sections", []):
            pool_id = section.get("pool")
            count = int(section.get("count", 0))
            if pool_id not in quizzes:
                errors.append(f"{prefix}: unknown pool {pool_id}")
                continue
            available = len(quizzes[pool_id].get("questions") or [])
            if count <= 0:
                errors.append(f"{prefix}: section {pool_id} count must be > 0")
            if count > available:
                errors.append(f"{prefix}: section {pool_id} requests {count}, only {available} available")

    if errors:
        print("Exam validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Exam validation passed.")
    return 0


def exam_run(args: argparse.Namespace) -> int:
    quizzes = load_quizzes()
    exams = load_exams()
    exam = exams.get(args.exam_id)

    if exam is None:
        print(f"ERROR: exam not found: {args.exam_id}", file=sys.stderr)
        print("Available exams:", file=sys.stderr)
        for eid in sorted(exams):
            print(f"  {eid}", file=sys.stderr)
        return 2

    try:
        questions = build_exam_questions(exam, quizzes)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    pass_score = float(exam.get("pass_score", 80))
    time_limit = exam.get("time_limit_minutes")

    correct_count, total, score, answered = ask_questions(
        title=str(exam.get("title", args.exam_id)),
        source_label=str(exam.get("_path", "")),
        questions=questions,
        pass_score=pass_score,
        mode="exam",
        time_limit_minutes=int(time_limit) if time_limit else None,
    )

    progress = load_progress()
    progress.setdefault("attempts", []).append(
        {
            "kind": "exam",
            "exam_id": args.exam_id,
            "exam_title": exam.get("title"),
            "timestamp": utc_now(),
            "question_count": total,
            "correct_count": correct_count,
            "score": score,
            "pass_score": pass_score,
            "passed": score >= pass_score,
            "answers": answered,
        }
    )
    save_progress(progress)

    print()
    print(f"Fortschritt gespeichert: {progress_path()}")

    return 0 if score >= pass_score else 1


def progress_show(_args: argparse.Namespace) -> int:
    progress = load_progress()
    attempts = progress.get("attempts") or []

    print()
    print(f"Progress file: {progress_path()}")
    print(f"Attempts:      {len(attempts)}")
    print()

    if not attempts:
        print("No attempts recorded yet.")
        return 0

    for attempt in attempts[-15:]:
        ts = attempt.get("timestamp", "")
        kind = attempt.get("kind", "quiz")
        item_id = attempt.get("quiz_id") or attempt.get("exam_id") or ""
        score = attempt.get("score", 0)
        correct = attempt.get("correct_count", 0)
        total = attempt.get("question_count", 0)
        passed = "passed" if attempt.get("passed") else "not passed"
        print(f"{ts}  {kind:5}  {item_id:24} {correct}/{total}  {score:.2f}%  {passed}")

    return 0


def progress_export(args: argparse.Namespace) -> int:
    src = progress_path()
    if not src.exists():
        print("No progress file exists yet.")
        return 1

    dest = Path(args.path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    print(f"Exported progress to: {dest}")
    return 0


def progress_reset(_args: argparse.Namespace) -> int:
    path = progress_path()
    if not path.exists():
        print("No progress file exists.")
        return 0

    print(f"This will delete: {path}")
    answer = input("Type DELETE to continue: ").strip()
    if answer != "DELETE":
        print("Aborted.")
        return 1

    path.unlink()
    print("Progress deleted.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wwca",
        description="Local helper tool for Wireshark WCA DE course.",
    )

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

    exam = sub.add_parser("exam", help="Exam commands")
    exam_sub = exam.add_subparsers(dest="exam_command")

    e_list = exam_sub.add_parser("list", help="List exams")
    e_list.set_defaults(func=exam_list)

    e_validate = exam_sub.add_parser("validate", help="Validate exam YAML files")
    e_validate.set_defaults(func=exam_validate)

    e_run = exam_sub.add_parser("run", help="Run an exam")
    e_run.add_argument("exam_id", help="Exam id, e.g. module-basic")
    e_run.set_defaults(func=exam_run)

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


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "progress" and args.progress_command is None:
        return progress_show(args)

    if args.command == "quiz" and args.quiz_command is None:
        parser.parse_args(["quiz", "--help"])
        return 2

    if args.command == "exam" and args.exam_command is None:
        parser.parse_args(["exam", "--help"])
        return 2

    if args.func is None:
        parser.print_help()
        return 2

    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
