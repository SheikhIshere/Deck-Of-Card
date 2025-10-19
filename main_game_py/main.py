from game_logic import Game
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    print("=" * 25)
    print("       WELCOME TO DECK OF CARD GAME!       ")
    print("=" * 25)
    print("\n")

def main():
    clear_screen()
    display_welcome()
    
    input("Press Enter to start the game...")
    clear_screen()
    
    game = Game()
    game.play()

if __name__ == "__main__":
    main()