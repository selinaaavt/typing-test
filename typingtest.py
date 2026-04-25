import time
import random
import json
import os

# WPM CALCULATION
def calculate_wpm(typed: str, elapsed_seconds: float) -> float:
    """
    Calculates words per minute (WPM). 
    Uses the typographical standard where one "word" equals exactly 5 characters, including spaces.
    """
    
    # We count characters rather than splitting by spaces to account for 
    # partial words and spacing inconsistencies in the user's input.
    char_count = len(typed)
    
    # Convert the raw seconds into minutes for the WPM formula
    minutes = elapsed_seconds / 60
    
    # Formula: (Total Characters / 5) gives total words. Divide by minutes to get WPM.
    # We return 0.0 if the timer was too fast to avoid a ZeroDivisionError.
    return round((char_count / 5) / minutes, 1) if minutes > 0 else 0.0


# ACCURACY CALCULATION
def calculate_accuracy(target: str, typed: str) -> float:
    """
    Calculates typing accuracy as a percentage.
    Compares the user's string against the target passage index by index.
    """
    
    # Base case: Prevent division by zero if the user just pressed Enter
    if not typed:
        return 0.0

    correct_chars = 0
    
    # We use the length of the longer string as our baseline. 
    # This ensures that if the user types extra characters or misses characters at the end, 
    # those discrepancies are properly penalized as mistakes.
    total_chars = max(len(target), len(typed))

    # Iterate through both strings simultaneously
    for i in range(total_chars):
        # A character is only correct if it exists at the exact same index in both strings
        if i < len(target) and i < len(typed) and target[i] == typed[i]:
            correct_chars += 1

    # Convert the ratio of correct characters to a percentage, rounded to 1 decimal
    return round((correct_chars / total_chars) * 100, 1)


# LEADERBOARD FUNCTIONS
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    """Reads the JSON leaderboard file and returns a list of score dictionaries."""
    
    # Return an empty list if this is the first run and the file hasn't been created
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    # Attempt to load the JSON data safely
    with open(LEADERBOARD_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            # Fallback: If the JSON file is empty or corrupted, reset it gracefully
            return []


def save_score(name: str, wpm: float, accuracy: float):
    """Appends a new score to the leaderboard and saves it to the JSON file."""
    
    # Fetch the current state of the leaderboard
    scores = load_leaderboard()

    # Append the new user's performance as a dictionary
    scores.append({
        "name": name,
        "wpm": wpm,
        "accuracy": accuracy
    })

    # Overwrite the file with the newly updated list, using indent=4 for readability
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(scores, f, indent=4)


def display_leaderboard():
    """Formats and prints the top 10 scores from the leaderboard."""
    
    scores = load_leaderboard()

    if not scores:
        print("\nNo scores yet.\n")
        return

    # Sort the leaderboard descending. 
    # The lambda function uses a tuple: (-WPM, -Accuracy). 
    # The negative signs force Python to sort from highest to lowest instead of default lowest to highest.
    scores.sort(key=lambda x: (-x["wpm"], -x["accuracy"]))

    print("\n--- Leaderboard ---")
    
    # Slice the list to only show the top 10 to keep the terminal output clean
    for i, score in enumerate(scores[:10], start=1):
        print(f"{i}. {score['name']} - {score['wpm']} WPM, {score['accuracy']}%")
    print()


# ---------------------------
# TYPING TEST LOGIC
# ---------------------------
def run_typing_test(passages):
    """Handles the core loop of picking a prompt, timing the user, and calculating results."""
    
    passage = random.choice(passages)

    # Pause execution until the user is ready, so the timer doesn't start prematurely
    print("\nGet ready! Press Enter to start...")
    input()

    print("\n--- Type the following passage ---\n")
    print(passage)
    print("\nStart typing below:\n")

    # Mark the start time immediately before taking input
    start_time = time.time()
    
    # The program blocks here while waiting for the user to type and press Enter
    user_input = input("> ")
    
    # Calculate exactly how many seconds elapsed during the input block
    elapsed = time.time() - start_time

    # Generate the performance metrics
    wpm = calculate_wpm(user_input, elapsed)
    accuracy = calculate_accuracy(passage, user_input)

    # Output the results
    print("\n--- Results ---")
    print(f"Time:     {elapsed:.1f} seconds")
    print(f"WPM:      {wpm}")
    print(f"Accuracy: {accuracy}%\n")

    # Prompt for leaderboard entry. Using .strip() ensures we don't save empty spaces as a name.
    name = input("Enter your name for the leaderboard (leave blank to skip): ").strip()
    
    if name:
        save_score(name, wpm, accuracy)


# MAIN PROGRAM
def main():
    """Entry point of the program. Manages the game loop and menu flow."""
    
    # A pool of test prompts of varying lengths and complexities
    passages = [
        "The quick brown fox jumps over the lazy dog.",
        "Practice makes perfect when learning to type quickly.",
        "Python is a powerful and simple programming language.",
        "Typing tests are a great way to improve speed and accuracy.",
        "Consistency is the key to mastering any new skill."
    ]

    # Infinite loop to keep the application running until the user explicitly quits
    while True:
        run_typing_test(passages)

        # Leaderboard prompt
        choice = input("View leaderboard? (y/n): ").strip().lower()
        if choice == "y":
            display_leaderboard()

        # Replay prompt
        retry = input("Do you want to try again? (y/n): ").strip().lower()
        if retry != "y":
            print("Thanks for playing! Goodbye.")
            break


# Ensure the script only runs if executed directly (not if imported as a module)
if __name__ == "__main__":
    main()