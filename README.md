# 🎓 Universal CLI Quiz Tool

A lightweight, terminal-based quiz engine written in Python. Supports multiple subjects, topic filtering, past-exam simulations, and persistent score tracking.

---

## Project Structure

```
Test_CLI/
├── quiz.py                  ← Quiz engine
├── quiz_history.json        ← Auto-generated score history (gitignored)
├── README.md
├── .gitignore
│
├── subjects/                ← Question banks (one folder per subject)
│   └── lcom/
│       ├── lcom.json        ← 300-question LCOM practice bank
│       └── exams/           ← Past-exam simulations (fixed order)
│           ├── test1.json   ← Test 1  — 4 Apr 2025  (20 Qs)
│           ├── test2.json   ← Test 2  — 29 Apr 2025 (25 Qs)
│           └── resit.json   ← Resit   — 27 Jun 2025 (30 Qs)
│
└── info/                    ← Study material (one folder per subject)
    └── lcom/
        ├── lectures.md      ← LCOM lecture notes
        └── exams.md         ← Past exam papers (source)
```

---

## Usage

```bash
# Interactive menu
python3 quiz.py

# Jump directly to a subject
python3 quiz.py --subject lcom

# Help
python3 quiz.py --help
```

---

## Subject Menu Options

| # | Option | Description |
|---|--------|-------------|
| 1 | Practice quiz — default size | Random sample of ~20 questions |
| 2 | Practice quiz — custom size | You choose how many questions |
| 3 | Filter by topic | Pick specific topics to drill |
| 4 | View score history | See your last 20 results |
| 5 | 📝 Exam Simulations | Past papers in original order |

---

## Adding a New Subject

1. Create `subjects/<subject>/` directory.
2. Add a `<subject>.json` file with the schema below.
3. Optionally add `subjects/<subject>/exams/*.json` for past-exam simulations.
4. Optionally add study notes to `info/<subject>/`.

### Practice Bank Schema

```json
{
  "subject": "Subject Display Name",
  "topics": ["Topic A", "Topic B"],
  "questions": [
    {
      "id": 1,
      "topic": "Topic A",
      "difficulty": "easy",
      "question": "Question text?",
      "options": {
        "A": "Option A",
        "B": "Option B",
        "C": "Option C",
        "D": "Option D"
      },
      "answer": "A",
      "explanation": "Why A is correct."
    }
  ]
}
```

### Exam Simulation Schema

Same as above, with three extra top-level fields:

```json
{
  "exam_mode": true,
  "exam_title": "Test 1 – Date",
  "exam_questions": 20,
  ...
}
```

---

## Score History

Results are saved automatically to `quiz_history.json` at the project root after every session (both practice and exam simulation). The history view shows the last 20 entries.

---

## Requirements

Python 3.7+ — no third-party packages needed.
