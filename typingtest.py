import time
import random
import json
import os

# function to calculate words per minute (WPM)
def calculate_wpm(typed: str, elapsed_seconds: float) -> float:
    # find the number of typed characters in the typed string including spaces
    char_count = len(typed)
    
    # elapsed_second is a float number divide by 60 since 60 secs in a min
    minutes = elapsed_seconds / 60
    
    # on average each word has 5 characters so we standarized it to 5 characters/word to make calculations easy
    # characters/5 = number of words
    # words/minutes = WPM (rounded)
    # if minutes is less than 1 then just void the calculatation and return 0.0
    # round to nearest whole number
    return round((char_count / 5) / minutes, 1) if minutes > 0 else 0.0

# target text is the text that the user is given and typed is the the user's attempt at typing the target text
def calculate_accuracy(target: str, typed: str) -> float:
    
    # if string is empty return 0.0
    if not typed:
        return 0.0

    # make a varible for correct characters user typed in comparison with target text
    correct_chars = 0
    
    # whichever string (target text or typed text) is bigger is logged as the total number of characters used for calculations
    total_chars = max(len(target), len(typed))

    # loop check for each characters
    for i in range(total_chars):
        # A character is only correct if it exists at the exact same index in both strings
        if i < len(target) and i < len(typed) and target[i] == typed[i]:
            correct_chars += 1

    # reach the accuracy by dividing correct characters by total characters and converting to percent by multiplying by 100
    # round to nearest whole number 
    return round((correct_chars / total_chars) * 100, 1)

# set file to the one named leaderboard.json
LEADERBOARD_FILE = "leaderboard.json"

# reads the leaderboard json file and returns a list of score dictionaries.
def load_leaderboard():
    
    # if the file leaderboard.json is missing return nothing
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    # reads the file's text and returns the current list in leaderboard.json
    with open(LEADERBOARD_FILE, "r") as f:
        try:
            return json.load(f)
        # if empty then just return empty
        except:
            return []

# adds a new score to the leaderboard
# score shows up on the leaderboard json file
def save_score(name: str, wpm: float, accuracy: float):
    
    # inputs the leaderboard scores and inputs into variable score
    scores = load_leaderboard()

    # adds score by adding the name, wpm, and accuracy of the user
    scores.append({
        "name": name,
        "wpm": wpm,
        "accuracy": accuracy
    })

    # opens with writing mode
    # adds the scores from the users with a 4 width space
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(scores, f, indent=4)

# prints top 10 scores from leaderboard
def display_leaderboard():

    # inputs the leaderboard scores and inputs into variable score
    scores = load_leaderboard()

    # if scores is empty say that there are no scores
    if not scores:
        print("\nNo scores yet.\n")
        return

    # sort scores by wpm and accuracy
    scores.sort(key=lambda x: (-x["wpm"], -x["accuracy"]))

    # show a header with the title Leaderboard
    print("\n--- Leaderboard ---")
    
    # print up to 10 scores in the format (name, wpm, accuracy)
    for i, score in enumerate(scores[:10], start=1):
        print(f"{i}. {score['name']} - {score['wpm']} WPM, {score['accuracy']}%")
    print()


# input the passgaes to the running test algorithm
def run_typing_test(passages):
    
    # choose a random passage from the options
    passage = random.choice(passages)

    # print a starting statement and enter any input to start
    print("\nGet ready! Press Enter to start...")
    input()

    # tell user to type
    print("\n--- Type the following passage ---\n")
    # show passage
    print(passage)
    # ask to type
    print("\nStart typing below:\n")

    # get the start time
    start_time = time.time()
    
    # user types > and the input is saved
    user_input = input("> ")
    
    # find the differences in time
    elapsed = time.time() - start_time

    # find wpm
    wpm = calculate_wpm(user_input, elapsed)
    
    #find accuracy
    accuracy = calculate_accuracy(passage, user_input)

    # print results
    print("\n--- Results ---")
    print(f"Time:     {elapsed:.1f} seconds")
    print(f"WPM:      {wpm}")
    print(f"Accuracy: {accuracy}%\n")

    # ask for name and save to variable
    name = input("Enter your name for the leaderboard (leave blank to skip): ").strip()
    
    # add name, wpm, accuracy to score
    if name:
        save_score(name, wpm, accuracy)

# start the function
def main():
    
    # sample text passages
    passages = [
        "The quick brown fox jumps over the lazy dog.",
        "Practice makes perfect when learning to type quickly.",
        "Python is a powerful and simple programming language.",
        "Typing tests are a great way to improve speed and accuracy.",
        "Consistency is the key to mastering any new skill."
    ]

    # run the actual typing test function with the selected passages
    while True:
        run_typing_test(passages)

        # ask if user wants to see leaderboard by a input of y/n 
        choice = input("View leaderboard? (y/n): ").strip().lower()
        # if yes then display leaderboard
        if choice == "y":
            display_leaderboard()

        # ask if user wants to try again by input of y/n
        retry = input("Do you want to try again? (y/n): ").strip().lower()
        # if not yes then end the typing test
        if retry != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()

    