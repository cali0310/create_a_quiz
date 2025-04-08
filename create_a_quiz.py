# Import necessary libraries
import os        
import json      
import time      
from colorama import Fore, Style, init  
import emoji     

# Initialize colorama to auto-reset color styles after each print
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "\n" + emoji.emojize(":direct_hit: QUIZ CREATOR :direct_hit:") + Style.RESET_ALL)

def loading_animation(message, duration=1.5):
    chars = "|/-\\"
    for _ in range(int(duration * 10)):
        for char in chars:
            print(f"\r{Fore.YELLOW}{message} {char}", end="", flush=True)
            time.sleep(0.1)
    print()

def get_input(prompt, color=Fore.GREEN):
    return input(f"{color}{prompt}{Style.RESET_ALL}")

def create_question():
    display_header()
    
    # section header
    print(Fore.GREEN + "\n" + emoji.emojize(":pencil:  CREATE NEW QUESTION") + Style.RESET_ALL)
    print(Fore.YELLOW + "═" * 50 + Style.RESET_ALL)

    # get the question from the user
    question = get_input("\n" + emoji.emojize(":memo: Enter your question: "), Fore.CYAN)

    # four answer choices
    print(Fore.YELLOW + "\n--- Enter the four answer choices ---" + Style.RESET_ALL)
    choices = {}
    options = ['a', 'b', 'c', 'd']

    for option in options:
        choices[option] = get_input(f"Option {option.upper()}: ")

    # Loop until a valid correct answer is entered
    while True:
        correct_answer = get_input("\n" + emoji.emojize(":white_check_mark: Enter the correct answer (a/b/c/d): "), Fore.MAGENTA).lower()
        if correct_answer in options:
            break
        print(Fore.RED + "Invalid option! Please enter a, b, c, or d." + Style.RESET_ALL)

    # Return the constructed question data
    return {
        "question": question,
        "choices": choices,
        "correct_answer": correct_answer
    }
# save questions to a file in JSON format
def load_saved_quiz_questions(file_name="quiz_questions.txt"):
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as input_file:
                return json.load(input_file)
        return []  # Return an empty list if file doesn't exist
    except Exception as error_message:
        print(Fore.RED + f"Error loading quiz questions: {error_message}" + Style.RESET_ALL)
        return []
