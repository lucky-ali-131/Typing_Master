import time
import random
import string

# Sample text for typing practice
sample_texts = [
    "Hello everyone, i am Md Ali the creater of this program. Thanks for using typing code. Have a good day",
    "Python is an easy to learn, powerful programming language.",
    "Typing is an important skill for many tasks in today's world.",
    "Practice makes a man perfect, and that goes for typing too."
]

# Function to calculate typing speed and accuracy
def calculate_wpm_and_accuracy(start_time, end_time, typed_text, correct_text):
    time_taken = end_time - start_time  # Time taken in seconds
    word_count = len(typed_text.split())  # Word count
    wpm = (word_count / time_taken) * 60  # Words per minute

    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(typed_text, correct_text) if a == b)
    accuracy = (correct_chars / len(correct_text)) * 100 if correct_text else 0
    
    return wpm, accuracy

# Main function to run the typing test
def typing_test():
    # Choose a random sentence from the sample texts
    correct_text = random.choice(sample_texts)
    print("Type the following text as quickly and accurately as you can:")
    print(f"\n{correct_text}\n")

    input("Press Enter when you're ready to start...")
    start_time = time.time()  # Start the timer

    typed_text = input("Start typing here: ")  # Take the input from the user
    end_time = time.time()  # Stop the timer after typing

    # Calculate words per minute (WPM) and accuracy
    wpm, accuracy = calculate_wpm_and_accuracy(start_time, end_time, typed_text, correct_text)

    # Show results
    print(f"\nYour typing speed: {wpm:.2f} words per minute")
    print(f"Your accuracy: {accuracy:.2f}%")

# Run the typing test
if __name__ == "__main__":
    typing_test()
