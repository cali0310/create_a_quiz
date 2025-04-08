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
    print(Fore.CYAN + Style.BRIGHT + "\n" + "\U0001F3AF  QUIZ CREATOR 🎯" + Style.RESET_ALL)

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
        correct_answer = get_input("\n" + "\u2705 Enter the correct answer (a/b/c/d): ", Fore.MAGENTA).lower()
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
def save_quiz_questions_to_file(quiz_questions_list, file_name="quiz_questions.txt"):
    try:
        with open(file_name, 'w') as output_file:
            json.dump(quiz_questions_list, output_file, indent=4)
        return True
    except Exception as error_message:
        print(Fore.RED + f"Error saving quiz questions: {error_message}" + Style.RESET_ALL)
        return False
    
# load previously saved quiz questions from a file
def load_saved_quiz_questions(file_name="quiz_questions.txt"):
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as input_file:
                return json.load(input_file)
        return []  # Return an empty list if file doesn't exist
    except Exception as error_message:
        print(Fore.RED + f"Error loading quiz questions: {error_message}" + Style.RESET_ALL)
        return []

# reset the questions (clear the list and reset the file)
def reset_all_questions(quiz_questions_list, filename="quiz_questions.txt"):
    try:
        # Clear the questions list in memory
        quiz_questions_list.clear()

        # Overwrite the file with an empty list
        with open(filename, 'w') as file:
            json.dump([], file, indent=4)
        
        print(Fore.GREEN + "\n✅ Questions have been reset!" + Style.RESET_ALL)
        return True
    except Exception as reset_exception:
        print(Fore.RED + f"Error resetting questions: {reset_exception}" + Style.RESET_ALL)
        return False

# main program loop
def main():
    file_name = "quiz_questions.txt"
    questions = load_saved_quiz_questions(file_name)
    
    while True:
        display_header()

        # current question count
        print(f"\n{Fore.CYAN}" + emoji.emojize(":bar_chart:") + f" Current question count: {Fore.WHITE}{len(questions)}")
        print(Fore.YELLOW + "═" * 50 + Style.RESET_ALL)

        # main menu options
        print(f"\n{Fore.GREEN}1.{Style.RESET_ALL} Add a new question")
        print(f"{Fore.RED}2.{Style.RESET_ALL} Reset questions")
        print(f"{Fore.RED}3.{Style.RESET_ALL} Exit")

        # ask for user choice
        choice = get_input("\n" + emoji.emojize(":backhand_index_pointing_right: Choose an option (1-3): "))
        
        if choice == '1':
            # create and append a new question
            new_question = create_question()
            questions.append(new_question)

            # show saving animation
            loading_animation("Saving question...")

            # save updated question list to file
            if save_quiz_questions_to_file(questions, file_name):
                print(Fore.GREEN + "\n" + emoji.emojize(":check_mark_button: Question saved successfully!") + Style.RESET_ALL)
            else:
                print(Fore.RED + "\n" + emoji.emojize(":cross_mark: Failed to save question.") + Style.RESET_ALL)

            # Pause before returning to menu
            input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

        elif choice == '2':
            # Reset the questions
            reset_all_questions(questions, file_name)
            questions = load_saved_quiz_questions(file_name)
            input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

        elif choice == '3':
            # Exit screen message
            display_header()
            print(Fore.CYAN + "\nThank you for using the Quiz Creator!")
            print(f"Your questions are saved in {file_name}")
            print(Fore.YELLOW + "\n" + emoji.emojize("Exiting program... :right_arrow:") + Style.RESET_ALL)
            time.sleep(1.5)
            break

        else:
            # Handle invalid menu selection
            print(Fore.RED + "\nInvalid choice! Please select 1, 2, or 3." + Style.RESET_ALL)
            time.sleep(1.5)

# running the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nProgram interrupted. Exiting..." + Style.RESET_ALL)