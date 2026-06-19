#!/usr/bin/env python3
"""
=============================================================
  Universal CLI Quiz Tool
  ─────────────────────────────────────────────────────────
  Usage:
    python3 quiz.py                  # Interactive menu
    python3 quiz.py --help           # Help text
    python3 quiz.py --subject lcom   # Jump straight to a subject

  Directory layout:
    subjects/
      <subject>/
        <subject>.json               # Practice question bank
        exams/
          *.json                     # Past-exam simulations

    info/
      <subject>/
        *.md                         # Study notes / past papers

  To add a new subject, drop a new folder under subjects/ with
  a <subject>.json file that has "subject" and "questions" keys.
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

RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
WHITE   = "\033[97m"

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
║  {BOLD}{WHITE}🎓  Universal CLI Quiz Tool{RESET}{CYAN}                                 ║
║  {DIM}Randomised multiple-choice quizzes from question banks{RESET}{CYAN}      ║
╚══════════════════════════════════════════════════════════════╝{RESET}
"""

# ─── Paths ───────────────────────────────────────────────────────────────────

SCRIPT_DIR   = Path(__file__).parent
SUBJECTS_DIR = SCRIPT_DIR / "subjects"
HISTORY_FILE = SCRIPT_DIR / "quiz_history.json"
ANSWERED_FILE = SCRIPT_DIR / "answered_questions.json"

# ─── Discover question banks ─────────────────────────────────────────────────

def discover_subjects():
    """
    Scan subjects/<slug>/<slug>.json for practice banks.

    Returns:
        dict: {slug: {"name": str, "path": Path, "exams": [(title, path), ...]}}
    """
    result = {}

    if not SUBJECTS_DIR.exists():
        return result

    for subject_dir in sorted(SUBJECTS_DIR.iterdir()):
        if not subject_dir.is_dir():
            continue

        slug = subject_dir.name
        bank_path = subject_dir / f"{slug}.json"

        if not bank_path.exists():
            # Try any single *.json at this level
            candidates = list(subject_dir.glob("*.json"))
            if len(candidates) == 1:
                bank_path = candidates[0]
            else:
                continue

        try:
            with open(bank_path) as f:
                data = json.load(f)
            if "subject" not in data or "questions" not in data:
                continue
        except Exception:
            continue

        # Discover exam simulations under subjects/<slug>/exams/
        exams = []
        exams_dir = subject_dir / "exams"
        if exams_dir.is_dir():
            for exam_path in sorted(exams_dir.glob("*.json")):
                try:
                    with open(exam_path) as f:
                        edata = json.load(f)
                    if edata.get("exam_mode") and "questions" in edata:
                        title = edata.get("exam_title", exam_path.stem)
                        exams.append((title, exam_path))
                except Exception:
                    pass

        result[slug] = {
            "name": data.get("subject", slug),
            "path": bank_path,
            "exams": exams,
        }

    return result

# ─── Load & validate a bank ──────────────────────────────────────────────────

def load_bank(path):
    """
    Load and validate a question bank JSON file.

    Returns:
        tuple: (subject_name: str, topics: list, questions: list)
    """
    with open(path) as f:
        data = json.load(f)

    qs = []
    for i, q in enumerate(data.get("questions", [])):
        required = ("id", "question", "options", "answer", "explanation")
        if not all(k in q for k in required):
            print(c(f"  ⚠  Question #{i} is malformed – skipping.", YELLOW))
            continue
        if q["answer"] not in q["options"]:
            print(c(f"  ⚠  Question id={q['id']} answer key not in options – skipping.", YELLOW))
            continue
        qs.append(q)

    subject_name = data.get("subject", "Unknown")
    topics = data.get("topics", [])
    return subject_name, topics, qs

# ─── Quiz session ────────────────────────────────────────────────────────────

def run_quiz(subject_name, all_questions, n_questions,
             topics_filter=None, fixed_order=False,
             unanswered_only=False, answered_ids=None):
    """
    Run one quiz session.

    Args:
        subject_name:   Display name for the subject.
        all_questions:  Full list of question dicts.
        n_questions:    Max number of questions to ask.
        topics_filter:  Optional list of topic strings to restrict to.
        fixed_order:    If True, use questions in their existing order
                        (exam simulation mode) rather than random sampling.

    Returns:
        tuple: (score: int, total: int, wrong_questions: list)
    """
    pool = all_questions
    if topics_filter:
        pool = [q for q in pool if q.get("topic", "") in topics_filter]
    if unanswered_only and answered_ids is not None:
        pool = [q for q in pool if str(q.get("id")) not in answered_ids]
    if not pool:
        print(c("  No questions available matching the criteria.", RED))
        return 0, 0, [], []

    if fixed_order:
        sample = pool[:n_questions]
    else:
        sample = random.sample(pool, min(n_questions, len(pool)))

    total = len(sample)
    score = 0
    wrong = []
    answered_this_session = []

    clear()
    print(BANNER)
    hr()
    print(c(f"  Subject  : {subject_name}", BOLD + WHITE))
    mode_label = "Exam Simulation – fixed order" if fixed_order else "Practice – random order"
    print(c(f"  Mode     : {mode_label}", DIM))
    print(c(f"  Questions: {total}  |  No negative marking", DIM))
    hr()
    print()

    for idx, q in enumerate(sample, 1):
        # ── Print question ─────────────────────────────────────────────
        tag   = f"[{idx}/{total}]"
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

        # Shuffle option letters so you can't memorise positions
        opts = list(q["options"].items())
        random.shuffle(opts)
        letter_map = {}  # displayed letter → original option key
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
                return score, idx - 1, wrong, answered_this_session
            if ans in valid:
                answered_this_session.append(str(q.get("id")))
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
            correct_letter = next(l for l, k in letter_map.items() if k == correct_key)
            print(c(f"  ✗  Wrong.  Correct answer: {correct_letter}. {correct_text}\n", RED + BOLD))
            print(c("  📖  Explanation:", YELLOW))
            print(wrap(q["explanation"], indent=5))
            print()
            wrong.append(q)

        hr(char="·", color=DIM)
        print()

    return score, total, wrong, answered_this_session

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
            print(c(f"  {i}. [{topic}]", MAGENTA),
                  wrap(q["question"], width=60, indent=5).lstrip())
            print(c("     ✔ Correct:", GREEN), q["options"][q["answer"]])
            print(c("     💡 Tip:", YELLOW),
                  wrap(q["explanation"], width=58, indent=8).lstrip())
            print()
    hr()

# ─── Score history ───────────────────────────────────────────────────────────

def get_answered_questions():
    if not ANSWERED_FILE.exists():
        return {}
    try:
        import json
        with open(ANSWERED_FILE, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def save_answered_questions(slug, new_answered_ids):
    if not new_answered_ids:
        return
    data = get_answered_questions()
    if slug not in data:
        data[slug] = []
    # Union of existing and new
    data[slug] = list(set(data[slug] + new_answered_ids))
    with open(ANSWERED_FILE, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def save_history(subject, score, total):

    """Append a quiz result to the persistent history file."""
    history = []
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE) as f:
                history = json.load(f)
        except Exception:
            history = []
    history.append({
        "subject":   subject,
        "score":     score,
        "total":     total,
        "pct":       round(score / total * 100) if total else 0,
        "timestamp": time.strftime("%Y-%m-%d %H:%M"),
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def show_history(subjects=None):
    if subjects:
        answered_data = get_answered_questions()
        print(c("\n  📊  Subject Coverage\n", BOLD + WHITE))
        hr(char="─")
        for slug, info in subjects.items():
            _, _, qs = load_bank(info["path"])
            total_qs = len(qs)
            ans_count = len(set(answered_data.get(slug, [])) & set(str(q.get("id")) for q in qs if "id" in q))
            cov = round(ans_count / total_qs * 100) if total_qs else 0
            print(f"  {info['name']:<40} {ans_count}/{total_qs:<8} {cov}%")
        hr()

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
    print(f"  {'Date/Time':<18} {'Subject':<26} {'Score':<10} {'%':>5}")
    hr(char="─")
    for entry in history[-20:]:  # show last 20
        pct = entry.get("pct", 0)
        col = GREEN if pct >= 75 else (YELLOW if pct >= 50 else RED)
        print(f"  {entry['timestamp']:<18} {entry['subject']:<26} "
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

# ─── Exam simulation sub-menu ─────────────────────────────────────────────────

def exam_simulation_menu(exams, slug):
    """
    Display past-exam simulations for a subject and run the selected one.

    Args:
        exams: list of (title: str, path: Path) tuples.
    """
    while True:
        clear()
        print(BANNER)
        hr()
        print(c("  📝  Exam Simulations\n", BOLD + WHITE))
        print(c("  Select a past exam to simulate:\n", DIM))

        for i, (title, _path) in enumerate(exams, 1):
            print(f"  {c(str(i)+'.', YELLOW)} {title}")
        print()
        print(f"  {c(str(len(exams)+1)+'.', YELLOW)} Back")
        print()

        try:
            choice = input(c("  Choose: ", CYAN)).strip()
        except (EOFError, KeyboardInterrupt):
            return

        if not choice.isdigit():
            continue
        n = int(choice)

        if n == len(exams) + 1:
            return

        if 1 <= n <= len(exams):
            title, exam_path = exams[n - 1]
            subject_name, _topics, all_qs = load_bank(exam_path)
            if not all_qs:
                print(c("  No valid questions found.", RED))
                input(c("\n  Press Enter to go back...", DIM))
                continue

            # Exam simulations: fixed question order, shuffle option letters only
            score, total, wrong, answered_this_session = run_quiz(
                subject_name=f"{subject_name} \u2013 {title}",
                all_questions=all_qs,
                n_questions=len(all_qs),
                fixed_order=True,
            )
            show_results(score, total, wrong, f"{subject_name} \u2013 {title}")
            if total > 0:
                save_history(f"{subject_name} \u2013 {title}", score, total)
            if answered_this_session:
                save_answered_questions(slug, answered_this_session)
            input(c("\n  Press Enter to continue...", DIM))

# ─── Subject menu ─────────────────────────────────────────────────────────────

def subject_menu(slug, subject_info):
    """Inner menu for a selected subject."""
    path         = subject_info["path"]
    subject_name = subject_info["name"]
    exams        = subject_info["exams"]

    subject_name_loaded, topics, all_qs = load_bank(path)
    subject_name = subject_name_loaded  # use the name from the bank itself

    if not all_qs:
        print(c("  No valid questions found in this bank.", RED))
        input(c("\n  Press Enter to go back...", DIM))
        return

    default_n = 20  # matches typical exam length

    while True:
        clear()
        print(BANNER)
        hr()
        print(c(f"  Subject : {subject_name}", BOLD + WHITE))
        print(c(f"  Practice bank: {len(all_qs)} questions", DIM))
        if exams:
            print(c(f"  Exam simulations available: {len(exams)}", DIM))
        hr()
        print()
        print(c("  1.", YELLOW), "Start practice quiz (default exam size)")
        print(c("  2.", YELLOW), "Start practice quiz (custom number of questions)")
        print(c("  3.", YELLOW), "Start practice quiz (unanswered questions only)")
        print(c("  4.", YELLOW), "Filter practice by topic")
        print(c("  5.", YELLOW), "View score history")
        if exams:
            print(c("  6.", YELLOW), "📝  Exam Simulations (past papers)")
            print(c("  7.", YELLOW), "Back to main menu")
        else:
            print(c("  6.", YELLOW), "Back to main menu")
        print()

        try:
            choice = input(c("  Choose: ", CYAN)).strip()
        except (EOFError, KeyboardInterrupt):
            return

        back_option = "7" if exams else "6"

        if choice == "1":
            score, total, wrong, answered_this_session = run_quiz(subject_name, all_qs, default_n)
            show_results(score, total, wrong, subject_name)
            if total > 0:
                save_history(subject_name, score, total)
            if answered_this_session:
                save_answered_questions(slug, answered_this_session)
            input(c("\n  Press Enter to continue...", DIM))

        elif choice == "2":
            try:
                n = int(input(c(f"  How many questions? (max {len(all_qs)}): ", CYAN)).strip())
                n = max(1, min(n, len(all_qs)))
            except (ValueError, EOFError):
                n = default_n
            score, total, wrong, answered_this_session = run_quiz(subject_name, all_qs, n)
            show_results(score, total, wrong, subject_name)
            if total > 0:
                save_history(subject_name, score, total)
            if answered_this_session:
                save_answered_questions(slug, answered_this_session)
            input(c("\n  Press Enter to continue...", DIM))

        elif choice == "3":
            answered_data = get_answered_questions()
            answered_ids = set(answered_data.get(slug, []))
            score, total, wrong, answered_this_session = run_quiz(
                subject_name, all_qs, default_n,
                unanswered_only=True, answered_ids=answered_ids
            )
            show_results(score, total, wrong, subject_name)
            if total > 0:
                save_history(subject_name, score, total)
            if answered_this_session:
                save_answered_questions(slug, answered_this_session)
            input(c("\n  Press Enter to continue...", DIM))

        elif choice == "4":
            selected = choose_topics(topics)
            score, total, wrong, answered_this_session = run_quiz(subject_name, all_qs, default_n,
                                           topics_filter=selected)
            show_results(score, total, wrong, subject_name)
            if total > 0:
                save_history(subject_name, score, total)
            if answered_this_session:
                save_answered_questions(slug, answered_this_session)
            input(c("\n  Press Enter to continue...", DIM))

        elif choice == "5":
            clear()
            show_history({slug: subject_info})
            input(c("\n  Press Enter to continue...", DIM))

        elif choice == "6" and exams:
            exam_simulation_menu(exams, slug)

        elif choice == back_option:
            return

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Universal CLI Quiz Tool")
    parser.add_argument("--subject", help="Subject slug to jump directly to (e.g. lcom)")
    args = parser.parse_args()

    subjects = discover_subjects()

    # Direct jump via CLI flag
    if args.subject:
        if args.subject in subjects:
            subject_menu(args.subject, subjects[args.subject])
            return
        else:
            print(c(f"  Subject '{args.subject}' not found. Available: {list(subjects.keys())}", RED))
            sys.exit(1)

    # Main interactive menu
    while True:
        clear()
        print(BANNER)
        hr()

        if not subjects:
            print(c("  ⚠  No question banks found!", RED))
            print(c("  Place a subjects/<name>/<name>.json file with 'subject' and 'questions' keys.", DIM))
            input(c("\n  Press Enter to exit...", DIM))
            return

        print(c("  Available subjects:\n", BOLD + WHITE))
        items = list(subjects.items())
        for i, (slug, info) in enumerate(items, 1):
            _sname, _topics, qs = load_bank(info["path"])
            exam_badge = f"  {c('[+exams]', CYAN)}" if info["exams"] else ""
            print(f"  {c(str(i)+'.', YELLOW)} {c(info['name'], BOLD)}"
                  f"  {c(f'({len(qs)} questions)', DIM)}{exam_badge}")

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
                slug, info = items[n - 1]
                subject_menu(slug, info)
            elif n == len(items) + 1:
                clear()
                show_history(subjects)
                input(c("\n  Press Enter to continue...", DIM))
            elif n == len(items) + 2:
                print(c("\n  Goodbye! 👋\n", CYAN))
                return

if __name__ == "__main__":
    main()
