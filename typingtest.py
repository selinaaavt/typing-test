import time
import random
import json
import os

def calculate_wpm(typed: str, elapsed_seconds: float) -> float:
    """
    Calculates words per minute (WPM). 
    Uses the typographical standard where one "word" equals exactly 5 characters, including spaces.
    """
    
    char_count = len(typed)
    
    minutes = elapsed_seconds / 60

    return round((char_count / 5) / minutes, 1) if minutes > 0 else 0.0


def calculate_accuracy(target: str, typed: str) -> float:
    """
    Calculates typing accuracy as a percentage.
    Compares the user's string against the target passage index by index.
    """
    
    if not typed:
        return 0.0

    correct_chars = 0
    

    total_chars = max(len(target), len(typed))

    for i in range(total_chars):
        # A character is only correct if it exists at the exact same index in both strings
        if i < len(target) and i < len(typed) and target[i] == typed[i]:
            correct_chars += 1

    return round((correct_chars / total_chars) * 100, 1)


LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    """Reads the JSON leaderboard file and returns a list of score dictionaries."""
    
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    with open(LEADERBOARD_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


def save_score(name: str, wpm: float, accuracy: float):
    """Appends a new score to the leaderboard and saves it to the JSON file."""
    
    scores = load_leaderboard()

    scores.append({
        "name": name,
        "wpm": wpm,
        "accuracy": accuracy
    })

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(scores, f, indent=4)


def display_leaderboard():
    """Formats and prints the top 10 scores from the leaderboard."""
    
    scores = load_leaderboard()

    if not scores:
        print("\nNo scores yet.\n")
        return

    scores.sort(key=lambda x: (-x["wpm"], -x["accuracy"]))

    print("\n--- Leaderboard ---")
    
    for i, score in enumerate(scores[:10], start=1):
        print(f"{i}. {score['name']} - {score['wpm']} WPM, {score['accuracy']}%")
    print()



def run_typing_test(passages):
    """Handles the core loop of picking a prompt, timing the user, and calculating results."""
    
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
    """Entry point of the program. Manages the game loop and menu flow."""
    
    passages = [
        "The quick brown fox jumps over the lazy dog.",
        "Practice makes perfect when learning to type quickly.",
        "Python is a powerful and simple programming language.",
        "Typing tests are a great way to improve speed and accuracy.",
        "Consistency is the key to mastering any new skill."
    ]

    while True:
        run_typing_test(passages)

        choice = input("View leaderboard? (y/n): ").strip().lower()
        if choice == "y":
            display_leaderboard()

        retry = input("Do you want to try again? (y/n): ").strip().lower()
        if retry != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()