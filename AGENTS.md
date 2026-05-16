# AGENTS.md

## Project

This repository contains an open-source German self-study course for network analysis with Wireshark, aligned with the Wireshark Certified Analyst WCA-101 learning objectives.

The course is independent and is not an official Wireshark Foundation project.

## Language

All learner-facing content must be written in German.

Technical terms may include their English term in parentheses on first use.

Examples:

- Anzeige-Filter (Display Filter)
- Mitschnitt (Capture)
- Neuübertragung (Retransmission)
- Paketverlust (Packet Loss)
- Rundlaufzeit (Round Trip Time / RTT)
- Expert-Informationen (Expert Information)
- Gesprächsübersicht (Conversations)
- Endpunkte (Endpoints)

## Target audience

The course is written for learners who already have basic networking knowledge, especially:

- IP addresses and subnets
- VLANs
- cabling and switches
- basic network architecture
- simple troubleshooting in IT operations

The course must not assume deep protocol analysis knowledge.

## Course goals

The course should help learners build real packet analysis skills with Wireshark, TShark and reproducible lab environments.

The course should prepare learners for WCA-101 in a legitimate way.

Do not include:

- real certification exam questions
- exam dumps
- copied proprietary training material
- private packet captures
- credentials
- customer data
- personal data

## Writing style

Write clearly, practically and step by step.

Prefer explanations that connect concepts to real troubleshooting situations.

Avoid unnecessary academic language.

Prefer this style:

> Ein DNS-Problem erkennst du nicht daran, dass "das Internet nicht geht", sondern daran, dass der Client eine Anfrage stellt und vom DNS-Server keine verwertbare Antwort erhält.

Avoid this style:

> DNS is a hierarchical distributed naming system that resolves domain names into resource records according to RFC-defined mechanisms.

Use examples, small scenarios and practical observations.

## Repository structure

Use the following structure:

```text
docs/       Course documentation and learning content
labs/       Practical exercises
pcaps/      Packet captures
docker/     Docker and lab environment resources
quizzes/    Questions, module tests and practice exams
tools/      Helper scripts and local CLI tools
```

## Documentation conventions

Course documentation belongs in `docs/`.

Each major course section should have its own directory.

Recommended structure:

```text
docs/
├── index.md
├── 00-orientierung/
├── 01-lern-und-uebungsumgebung/
├── 02-linux-grundlagen-fuer-den-kurs/
├── 03-wireshark-erster-kontakt/
├── 10-basis-kurs/
├── 20-advanced-kurs/
├── 30-wca-vorbereitung/
├── 40-labs-und-uebungen/
├── 50-quizzes/
├── 60-pcap-challenges/
└── 90-referenz/
```

## Lab conventions

Each lab should be structured consistently.

Recommended lab structure:

```text
labs/basic/lab-basic-030-dns-nxdomain/
├── README.md
├── scenario.md
├── tasks.md
├── hints.md
├── solution.md
├── metadata.yml
├── check_tshark.sh
└── files/
    └── capture.pcapng
```

Every lab should include:

- Ziel
- Voraussetzungen
- Szenario
- Aufgaben
- Hinweise
- Lösung
- WCA-Bezug
- Weiterführende Ressourcen

## Lab metadata

Where useful, labs should include machine-readable metadata.

Example:

```yaml
id: lab-basic-030-dns-nxdomain
title: "DNS NXDOMAIN analysieren"
track: basic
level: foundation
estimated_time: 30m
wca_objectives:
  - display-filters
  - dns
  - packet-details
  - troubleshooting-basics
tools:
  - wireshark
  - tshark
  - dig
requires:
  - lab-foundation-010-first-capture
outputs:
  - quiz
  - lab-check
  - analysis-report
```

## WCA alignment

When adding lessons or labs, include a WCA mapping where applicable.

The course may be aligned with WCA-101 objectives, but it must not copy protected exam content.

Good:

- "Dieses Lab übt Display Filter, DNS und Paketdetails."
- "Diese Aufgabe bereitet auf TCP-Troubleshooting-Ziele vor."

Bad:

- "Diese Frage kommt so in der Prüfung vor."
- "Originalfrage aus WCA-101."

## External resources

Prefer linking to external resources instead of copying them.

Useful external resources may include:

- official Wireshark documentation
- Wireshark User's Guide
- Wireshark Display Filter Reference
- TShark manual page
- SharkFest talks
- public packet analysis articles
- clearly licensed sample captures
- TCP/IP learning material

Do not copy external articles, slides, videos or packet captures into the repository unless the license clearly allows it.

## Packet capture policy

Packet captures can contain sensitive data.

Rules:

- Do not commit private captures.
- Do not commit productive network captures.
- Do not commit credentials, tokens or cookies.
- Do not commit customer data.
- Do not commit personal data.
- Prefer self-generated captures.
- Prefer synthetic lab traffic.
- External captures must have a clear license.
- If licensing is unclear, link to the source instead of committing the file.

## Technical baseline

Target platform:

- Ubuntu Desktop LTS
- Pop!_OS as compatible Ubuntu-based variant

Primary tools:

- Wireshark
- TShark
- tcpdump
- VSCode
- Docker
- Docker Compose
- Python
- Bash
- Git
- MkDocs Material

Commands should be suitable for Ubuntu-based systems.

Avoid platform-specific assumptions unless documented.

## Code conventions

Prefer:

- Bash for simple helper scripts
- Python for checks, quiz tooling and progress handling
- Docker Compose for reproducible labs
- Markdown for course content
- YAML for metadata

Scripts should be readable and include helpful error messages.

Do not hide complex logic in unreadable one-liners.

## Progress and quiz tooling

The course should work without a central server.

Progress should be stored locally.

Preferred locations:

```text
~/.local/share/wireshark-wca-de/progress.json
```

or later:

```text
~/.local/share/wireshark-wca-de/progress.sqlite
```

Export and import should be supported.

Example commands:

```bash
wwca progress
wwca quiz run basic-030
wwca lab check lab-basic-030-dns-nxdomain
wwca exam start wca-practice-01
wwca progress export ./mein-fortschritt.json
wwca progress import ./mein-fortschritt.json
```

## MkDocs conventions

The documentation should build with MkDocs Material.

Before committing MkDocs changes, check:

```bash
mkdocs build
```

The navigation should not reference non-existing files unless they are intentionally created in the same change.

## Review checklist

Before accepting changes, check:

- Is the content written in German?
- Is the explanation understandable for the target audience?
- Are commands suitable for Ubuntu-based systems?
- Does the Markdown render correctly?
- Are labs structured consistently?
- Are WCA references legitimate and not copied from protected exam material?
- Are external resources linked responsibly?
- Are there no private captures, credentials or personal data?
- Does `mkdocs build` complete successfully?

## Safety and legality

This project is for learning, troubleshooting and defensive network analysis.

Do not add offensive security instructions beyond defensive packet analysis.

Do not add content that encourages unauthorized packet capture or unauthorized access.

Always remind learners that packet capture is only allowed in networks where they have permission.