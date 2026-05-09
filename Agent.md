# AGENTS.md

## Project

This repository contains an open-source German self-study course for network analysis with Wireshark, aligned with the Wireshark Certified Analyst WCA-101 objectives.

## Language

All learner-facing content must be written in German.

Technical terms may include their English term in parentheses on first use, for example:
- Anzeige-Filter (Display Filter)
- Mitschnitt (Capture)
- Neuübertragung (Retransmission)

## Course style

- Write clearly and practically.
- Prefer step-by-step labs.
- Explain concepts before asking learners to solve tasks.
- Every lab must include:
  - Ziel
    - Voraussetzungen
      - Szenario
        - Aufgaben
          - Hinweise
            - Lösung
              - WCA-Bezug
                - Weiterführende Ressourcen

                ## Repository structure

                - Course documentation goes into `docs/`.
                - Labs go into `labs/`.
                - PCAP files go into `pcaps/`.
                - Docker resources go into `docker/`.
                - Quiz and exam material goes into `quizzes/`.
                - Helper tools go into `tools/`.

                ## Safety and legality

                - Do not include real exam questions or exam dumps.
                - Do not include private captures, credentials, tokens, or customer data.
                - Use only self-created PCAPs or clearly licensed external resources.
                - Prefer linking to external resources instead of copying them.

                ## Technical baseline

                - Target OS: Ubuntu Desktop LTS.
                - Pop!_OS may be documented as a compatible variant.
                - Prefer Bash, Python, Docker Compose, Markdown, MkDocs, and TShark.
                - Keep commands understandable for learners.

                ## Review guidelines

                - Check that commands are suitable for Ubuntu LTS.
                - Check that Markdown renders correctly.
                - Check that labs have clear learning objectives.
                - Check that WCA mapping is present where applicable.
                - Check that external links are used responsibly.