import time
import random
import json
import os

def calculate_wpm(typed: str, elapsed_seconds: float) -> float:
    # Standardize to 5 characters per word (industry standard for WPM)
    minutes = elapsed_seconds / 60
    return round((len(typed) / 5) / minutes, 1) if minutes > 0 else 0.0


def calculate_accuracy(target: str, typed: str) -> float:
    if not typed:
        return 0.0

    correct_chars = 0

    # Compare only up to len(target) so extra typed characters don't unfairly
    # lower the score — missing characters still count as wrong
    for i in range(len(target)):
        if i < len(typed) and target[i] == typed[i]:
            correct_chars += 1

    return round((correct_chars / len(target)) * 100, 1)


LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


def save_score(name: str, wpm: float, accuracy: float):
    scores = load_leaderboard()
    scores.append({"name": name, "wpm": wpm, "accuracy": accuracy})
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(scores, f, indent=4)


def display_leaderboard():
    scores = load_leaderboard()
    if not scores:
        print("\nNo scores yet.\n")
        return

    # Rank by WPM * accuracy so a fast-but-inaccurate score doesn't beat
    # a slower, more accurate one (e.g. 70 WPM @ 95% beats 100 WPM @ 50%)
    scores.sort(key=lambda x: -(x["wpm"] * (x["accuracy"] / 100)))

    print("\n--- Leaderboard (ranked by WPM x accuracy) ---")
    for i, score in enumerate(scores[:10], start=1):
        print(f"{i}. {score['name']} - {score['wpm']} WPM, {score['accuracy']}%")
    print()


def ask_yes_no(prompt: str) -> bool:
    # Loop until we get a valid answer so unexpected input doesn't break the flow
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def run_typing_test(passages):
    passage = random.choice(passages)

    print("\nGet ready! Press Enter to start...")
    input()

    print("\n--- Type the following passage ---\n")
    print(passage)
    print("\nStart typing below:\n")

    start_time = time.time()
    user_input = input("> ")
    elapsed = time.time() - start_time

    wpm = calculate_wpm(user_input, elapsed)
    accuracy = calculate_accuracy(passage, user_input)

    print("\n--- Results ---")
    print(f"Time:     {elapsed:.1f} seconds")
    print(f"WPM:      {wpm}")
    print(f"Accuracy: {accuracy}%\n")

    name = input("Enter your name for the leaderboard (leave blank to skip): ").strip()
    if name:
        save_score(name, wpm, accuracy)


def main():
    passages = [
        "The quick brown fox jumps over the lazy dog.",
        "Practice makes perfect when learning to type quickly.",
        "Python is a powerful and simple programming language.",
        "Typing tests are a great way to improve speed and accuracy.",
        "Consistency is the key to mastering any new skill."
    ]

    while True:
        run_typing_test(passages)

        if ask_yes_no("View leaderboard? (y/n): "):
            display_leaderboard()

        if not ask_yes_no("Do you want to try again? (y/n): "):
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()