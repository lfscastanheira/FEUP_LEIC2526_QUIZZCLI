#!/usr/bin/env python3
"""
=============================================================
  Universal CLI Quiz Tool
  ─────────────────────────────────────────────────────────
  Usage:
    python3 quiz.py                  # Interactive menu
    python3 quiz.py --help           # Help text
    python3 quiz.py --subject lcom   # Jump straight to a subject

  To add a new subject just drop a new <subject>.json file
  in the same directory as this script.
=============================================================
"""

import json
import os
import random
import sys
import textwrap
import time
import argparse
from pathlib import Path

# ─── ANSI colours ────────────────────────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BLUE   = "\033[94m"
MAGENTA= "\033[95m"
WHITE  = "\033[97m"

def c(text, color):
    return f"{color}{text}{RESET}"

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def hr(char="─", width=60, color=CYAN):
    print(c(char * width, color))

def wrap(text, width=70, indent=0):
    prefix = " " * indent
    return textwrap.fill(text, width=width, initial_indent=prefix,
                         subsequent_indent=prefix)

# ─── Banner ──────────────────────────────────────────────────────────────────

BANNER = f"""
{CYAN}╔══════════════════════════════════════════════════════════════╗
║  {BOLD}{WHITE}🎓  Universal CLI Quiz Tool{RESET}{CYAN}                                  ║
║  {DIM}Randomised multiple-choice quizzes from question banks{RESET}{CYAN}      ║
╚══════════════════════════════════════════════════════════════╝{RESET}
"""

# ─── Discover question banks ─────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent

def discover_subjects():
    """Return dict  {slug: path}  for every .json bank found."""
    banks = {}
    for p in sorted(SCRIPT_DIR.glob("*.json")):
        try:
            with open(p) as f:
                data = json.load(f)
            if "subject" in data and "questions" in data:
                slug = p.stem
                banks[slug] = p
        except Exception:
            pass
    return banks

# ─── Load & validate questions ───────────────────────────────────────────────

def load_bank(path):
    with open(path) as f:
        data = json.load(f)
    qs = []
    for i, q in enumerate(data["questions"]):
        if not all(k in q for k in ("id", "question", "options", "answer", "explanation")):
            print(c(f"  ⚠  Question #{i} is malformed – skipping.", YELLOW))
            continue
        if q["answer"] not in q["options"]:
            print(c(f"  ⚠  Question id={q['id']} answer key not in options – skipping.", YELLOW))
            continue
        qs.append(q)
    return data.get("subject", "Unknown"), data.get("topics", []), qs

# ─── Quiz session ────────────────────────────────────────────────────────────

def run_quiz(subject_name, all_questions, n_questions, topics_filter=None):
    """Run one quiz session. Returns (score, total, wrong_questions)."""

    pool = all_questions
    if topics_filter:
        pool = [q for q in pool if q.get("topic", "") in topics_filter]
    if not pool:
        print(c("  No questions match the selected topic(s).", RED))
        return 0, 0, []

    sample = random.sample(pool, min(n_questions, len(pool)))
    total  = len(sample)
    score  = 0
    wrong  = []

    clear()
    print(BANNER)
    hr()
    print(c(f"  Subject : {subject_name}", BOLD + WHITE))
    print(c(f"  Questions: {total}  |  No negative marking", DIM))
    hr()
    print()

    for idx, q in enumerate(sample, 1):
        # ── Print question ─────────────────────────────────────────────
        tag = f"[{idx}/{total}]"
        topic = q.get("topic", "")
        diff  = q.get("difficulty", "")
        meta  = f"  {c(tag, CYAN)}  {c(topic, MAGENTA)}"
        if diff:
            diff_colour = {"easy": GREEN, "medium": YELLOW, "hard": RED}.get(diff.lower(), DIM)
            meta += f"  {c(diff.upper(), diff_colour)}"
        print(meta)
        print()
        print(wrap(q["question"], indent=2))
        print()

        # Shuffle option letters
        opts = list(q["options"].items())
        random.shuffle(opts)
        letter_map = {}  # letter shown → original key
        display_letters = "ABCD"
        for i, (orig_key, opt_text) in enumerate(opts):
            letter = display_letters[i]
            letter_map[letter] = orig_key
            print(f"    {c(letter + '.', BOLD + YELLOW)}  {opt_text}")
        print()

        # ── Get answer ─────────────────────────────────────────────────
        valid = set(display_letters[:len(opts)])
        while True:
            try:
                ans = input(c("  Your answer (A/B/C/D): ", CYAN)).strip().upper()
            except (EOFError, KeyboardInterrupt):
                print()
                return score, idx - 1, wrong
            if ans in valid:
                break
            print(c("  ✗  Please enter one of: " + "/".join(sorted(valid)), RED))

        # ── Check answer ───────────────────────────────────────────────
        chosen_key   = letter_map[ans]
        correct_key  = q["answer"]
        correct_text = q["options"][correct_key]

        if chosen_key == correct_key:
            score += 1
            print(c("  ✔  Correct!\n", GREEN + BOLD))
        else:
            # Find the display letter for the correct answer
            correct_letter = next(l for l, k in letter_map.items() if k == correct_key)
            print(c(f"  ✗  Wrong.  Correct answer: {correct_letter}. {correct_text}\n", RED + BOLD))
            print(c("  📖  Explanation:", YELLOW))
            print(wrap(q["explanation"], indent=5))
            print()
            wrong.append(q)

        hr(char="·", color=DIM)
        print()

    return score, total, wrong

# ─── Results screen ──────────────────────────────────────────────────────────

def show_results(score, total, wrong, subject_name):
    if total == 0:
        return
    pct = round(score / total * 100)
    grade_colour = GREEN if pct >= 75 else (YELLOW if pct >= 50 else RED)

    clear()
    print(BANNER)
    hr()
    print(c(f"\n  📊  Results for: {subject_name}\n", BOLD + WHITE))
    print(c(f"  Score : {score}/{total}  ({pct}%)", grade_colour + BOLD))
    if   pct == 100: print(c("  🏆  Perfect score! Amazing!", GREEN))
    elif pct >= 80:  print(c("  🎉  Excellent work!", GREEN))
    elif pct >= 60:  print(c("  👍  Good job, keep it up!", YELLOW))
    elif pct >= 40:  print(c("  📚  Review the topics below.", YELLOW))
    else:            print(c("  ⚠️   Needs significant review.", RED))
    print()

    if wrong:
        hr()
        print(c(f"\n  ❌  Questions you got wrong ({len(wrong)}):\n", RED + BOLD))
        for i, q in enumerate(wrong, 1):
            topic = q.get("topic", "")
            print(c(f"  {i}. [{topic}]", MAGENTA), wrap(q["question"], width=60, indent=5).lstrip())
            print(c("     ✔ Correct:", GREEN), q["options"][q["answer"]])
            print(c("     💡 Tip:", YELLOW), wrap(q["explanation"], width=58, indent=8).lstrip())
            print()
    hr()

# ─── Score history ───────────────────────────────────────────────────────────

HISTORY_FILE = SCRIPT_DIR / "quiz_history.json"

def save_history(subject, score, total):
    history = []
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE) as f:
                history = json.load(f)
        except Exception:
            history = []
    history.append({
        "subject": subject,
        "score": score,
        "total": total,
        "pct": round(score / total * 100) if total else 0,
        "timestamp": time.strftime("%Y-%m-%d %H:%M")
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def show_history():
    if not HISTORY_FILE.exists():
        print(c("  No history yet.", DIM))
        return
    with open(HISTORY_FILE) as f:
        history = json.load(f)
    if not history:
        print(c("  No history yet.", DIM))
        return
    print(c("\n  📈  Quiz History\n", BOLD + WHITE))
    hr()
    print(f"  {'Date/Time':<18} {'Subject':<20} {'Score':<10} {'%':>5}")
    hr(char="─")
    for entry in history[-20:]:  # last 20
        pct = entry.get("pct", 0)
        col = GREEN if pct >= 75 else (YELLOW if pct >= 50 else RED)
        print(f"  {entry['timestamp']:<18} {entry['subject']:<20} "
              f"{entry['score']}/{entry['total']:<8} {c(str(pct)+'%', col):>10}")
    hr()

# ─── Topic selection ─────────────────────────────────────────────────────────

def choose_topics(topics):
    if not topics:
        return None
    print(c("\n  Available topics:", BOLD + CYAN))
    for i, t in enumerate(topics, 1):
        print(f"  {c(str(i)+'.', YELLOW)} {t}")
    print(f"  {c('0.', YELLOW)} All topics")
    print()
    while True:
        try:
            raw = input(c("  Select topics (comma-separated numbers, or 0 for all): ", CYAN)).strip()
        except (EOFError, KeyboardInterrupt):
            return None
        if raw == "0" or raw == "":
            return None
        try:
            chosen = [int(x.strip()) for x in raw.split(",")]
            if all(1 <= c2 <= len(topics) for c2 in chosen):
                return [topics[i - 1] for i in chosen]
        except ValueError:
            pass
        print(c("  Invalid input, try again.", RED))

# ─── Main menu ───────────────────────────────────────────────────────────────

def subject_menu(slug, path):
    """Inner menu for a selected subject."""
    subject_name, topics, all_qs = load_bank(path)
    if not all_qs:
        print(c("  No valid questions found in this bank.", RED))
        input(c("\n  Press Enter to go back...", DIM))
        return

    default_n = 20  # same as exam

    while True:
        clear()
        print(BANNER)
        hr()
        print(c(f"  Subject : {subject_name}", BOLD + WHITE))
        print(c(f"  Questions in bank: {len(all_qs)}", DIM))
        hr()
        print()
        print(c("  1.", YELLOW), "Start quiz (default exam size)")
        print(c("  2.", YELLOW), "Start quiz (custom number of questions)")
        print(c("  3.", YELLOW), "Filter by topic")
        print(c("  4.", YELLOW), "View score history")
        print(c("  5.", YELLOW), "Back to main menu")
        print()

        try:
            choice = input(c("  Choose: ", CYAN)).strip()
        except (EOFError, KeyboardInterrupt):
            return

        if choice == "1":
            score, total, wrong = run_quiz(subject_name, all_qs, default_n)
            show_results(score, total, wrong, subject_name)
            if total > 0:
                save_history(subject_name, score, total)
            input(c("\n  Press Enter to continue...", DIM))

        elif choice == "2":
            try:
                n = int(input(c(f"  How many questions? (max {len(all_qs)}): ", CYAN)).strip())
                n = max(1, min(n, len(all_qs)))
            except (ValueError, EOFError):
                n = default_n
            score, total, wrong = run_quiz(subject_name, all_qs, n)
            show_results(score, total, wrong, subject_name)
            if total > 0:
                save_history(subject_name, score, total)
            input(c("\n  Press Enter to continue...", DIM))

        elif choice == "3":
            selected = choose_topics(topics)
            score, total, wrong = run_quiz(subject_name, all_qs, default_n,
                                           topics_filter=selected)
            show_results(score, total, wrong, subject_name)
            if total > 0:
                save_history(subject_name, score, total)
            input(c("\n  Press Enter to continue...", DIM))

        elif choice == "4":
            clear()
            show_history()
            input(c("\n  Press Enter to continue...", DIM))

        elif choice == "5":
            return

def main():
    parser = argparse.ArgumentParser(description="Universal CLI Quiz Tool")
    parser.add_argument("--subject", help="Subject slug to jump directly to (e.g. lcom)")
    args = parser.parse_args()

    banks = discover_subjects()

    # Direct jump
    if args.subject:
        if args.subject in banks:
            subject_menu(args.subject, banks[args.subject])
            return
        else:
            print(c(f"  Subject '{args.subject}' not found. Available: {list(banks.keys())}", RED))
            sys.exit(1)

    # Main menu
    while True:
        clear()
        print(BANNER)
        hr()

        if not banks:
            print(c("  ⚠  No question banks found!", RED))
            print(c("  Place a <subject>.json file in the same directory.", DIM))
            input(c("\n  Press Enter to exit...", DIM))
            return

        print(c("  Available subjects:\n", BOLD + WHITE))
        items = list(banks.items())
        for i, (slug, path) in enumerate(items, 1):
            sname, _, qs = load_bank(path)
            print(f"  {c(str(i)+'.', YELLOW)} {c(sname, BOLD)}  {c(f'({len(qs)} questions)', DIM)}")

        print()
        print(c(f"  {len(items)+1}.", YELLOW), "View score history")
        print(c(f"  {len(items)+2}.", YELLOW), "Quit")
        print()

        try:
            choice = input(c("  Choose: ", CYAN)).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye! 👋")
            return

        if choice.isdigit():
            n = int(choice)
            if 1 <= n <= len(items):
                slug, path = items[n - 1]
                subject_menu(slug, path)
            elif n == len(items) + 1:
                clear()
                show_history()
                input(c("\n  Press Enter to continue...", DIM))
            elif n == len(items) + 2:
                print(c("\n  Goodbye! 👋\n", CYAN))
                return

if __name__ == "__main__":
    main()
