import json
import random

def hangman_art():
  pass


def hangman_game():
  pass


def main():
  print("Welcome to the Hangman Game")
  print("1. Play with Fiends.")
  print("2. Play with computer.")
  option = int(input("Enter the option: "))
  if option == 1:
    # print("Note: Minumum player 2 \n  Maximum player 4")
    player_num = int(input("Enter the number of player: "))
    player_num = int(input())
    hangman_game()
  elif option == 2:
    hangman_game()
  else:
    print("Invalid option!!!")    
if __name__=="__main__":
  main()