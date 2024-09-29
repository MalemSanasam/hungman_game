import json
import random
class Hangman_Game:
  def hangman_game(self):
    with open("hangman_word.json") as file:
      load_data = json.load(file)
      print("Levels:\n 1)Easy\n 2)Medium\n 3)Hard")
      level = input("select the difficulty level: ").strip().capitalize()
      if level == "Easy":
          secret_word = load_data["difficulty_levels"]["easy"]
          self.guess_secret_word(random.choice(secret_word))
  def guess_secret_word(self, secret_word):    
    attempt = 6
    guess_word = ["_"]*len(secret_word)
    print("_".join(guess_word))
    # print(secret_word)
    while attempt > 0 and "_" in guess_word:
      print(f"Available attempt {attempt}")
      guess = input("Guess the secret word: ")    
      if guess not in secret_word:
        print("Invalid guess!!! Try again")
        attempt-=1
      elif guess in secret_word:
        attempt-=1
        for index, letter in enumerate(secret_word):
          if letter == guess:
            guess_word[index] = guess  
        print(' '.join(guess_word)) 
      if "_" not in guess_word:
        print("Congratulation🥳🥳🥳, YOU WIN!!!") 
      elif attempt == 0:
        print("You lose😟😖😖")         
def main():
  game = Hangman_Game()
  print("Welcome to the Hangman Game")
  print("1. Play with Fiends.")
  print("2. Play with computer.")
  option = int(input("Enter the option: "))
  if option == 1:
    player_num = int(input("Enter the number of player: "))
    game.hangman_game()
  elif option == 2:
    Hangman_Game.hangman_game()
  else:
    print("Invalid option!!!")    
if __name__=="__main__":
  main()