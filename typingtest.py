import time

# Sample input 
# target = "The quick brown fox jumps over the lazy dog."
# typed  = "The quikc brown fox jumps over the lazy dg."

# Algorithm sketch:
# 1. Store the target passage as a string
# 2. Record start time
# 3. Display passage, wait for user to type
# 4. Record end time → elapsed = end - start
# 5. Zip target + typed → count matching characters
# 6. correct / max(len(target), len(typed)) → accuracy %
# 7. word count / (elapsed / 60) → WPM
# 8. Print results


def calculate_wpm(typed: str, elapsed_seconds: float) -> float:
    """Calculate words per minute."""
    word_count = len(typed.split())
    minutes = elapsed_seconds / 60
    return round(word_count / minutes, 1) if minutes > 0 else 0.0

def calculate_accuracy(target: str, typed: str) -> float:
    """Calculate typing accuracy as percentage."""
    if not typed:
        return 0.0

    # Count correct characters
    correct_chars = sum(1 for a, b in zip(target, typed) if a == b)

    # Penalize extra characters in typed text
    total_chars = max(len(target), len(typed))
    return round((correct_chars / total_chars) * 100, 1)

def run_typing_test(passage: str):
    """Run a single typing test."""
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

def main():
    passage = "The quick brown fox jumps over the lazy dog."
    
    while True:
        run_typing_test(passage)
        retry = input("Do you want to try again? (y/n): ").strip().lower()
        if retry != "y":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()