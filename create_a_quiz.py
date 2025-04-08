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