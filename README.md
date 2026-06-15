# 🎓 Universal CLI Quiz Tool

A flexible, colourful command-line quiz tool that loads question banks from JSON
files and randomises exam-style multiple-choice quizzes.

---

## Quick Start

```bash
# Run interactively (auto-discovers all *.json banks in this folder)
python3 quiz.py

# Jump straight to LCOM
python3 quiz.py --subject lcom
```

---

## File Structure

```
Test_CLI/
├── quiz.py          ← The quiz engine (never needs editing)
├── lcom.json        ← LCOM question bank (300 questions)
├── quiz_history.json← Auto-created; stores your session scores
└── README.md        ← This file
```

---

## Features

| Feature | Detail |
|---|---|
| 📦 Multi-subject | Drop any `<name>.json` in this folder — it appears in the menu |
| 🔀 Randomised | Questions AND answer order are shuffled every run |
| 🎯 Topic filter | Quiz only the topics you want to drill |
| 📖 Explanations | Wrong answers show an explanation immediately |
| 📈 History | Every session is logged; view anytime from the menu |
| 🔢 Custom size | Choose how many questions per session |

---

## LCOM Question Bank (`lcom.json`)

**300 questions** across 12 topics:

| Topic | Questions |
|---|---|
| C Programming | 73 |
| Interrupts and PIC | 29 |
| Keyboard and KBC | 29 |
| Video and VBE | 35 |
| i8254 Timer | 23 |
| OOP in C | 23 |
| PS/2 Mouse | 21 |
| RTC | 18 |
| Event-Driven Design | 16 |
| Graphics Buffering | 11 |
| XPM and Sprites | 12 |
| I/O and Device Drivers | 10 |

Difficulty levels: **easy / medium / hard** — mirroring past exam style.

---

## Adding a New Subject

Create `<slug>.json` in this folder with the structure:

```json
{
  "subject": "My Course Name",
  "topics": ["Topic A", "Topic B"],
  "questions": [
    {
      "id": 1,
      "topic": "Topic A",
      "difficulty": "medium",
      "question": "What is the answer to everything?",
      "options": {
        "A": "41",
        "B": "42",
        "C": "43",
        "D": "44"
      },
      "answer": "B",
      "explanation": "Douglas Adams, The Hitchhiker's Guide to the Galaxy."
    }
  ]
}
```

The tool discovers it automatically on the next run — no code changes needed.

---

## Tips for Exam Prep

1. **Run 3–4 short sessions per day** rather than one long cramming session.
2. **Use topic filter** to focus on your weakest areas first.
3. **Read every explanation** — even for correct answers.
4. **Target ≥80% consistently** before the exam.
5. **Hard questions** are marked — if you get those right, you're in great shape.
