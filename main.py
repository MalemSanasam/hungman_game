import json
import random
class Hangman_Game:
  # playing with bot and selecting the difficulty level
  def hangmanWithBot(self,load_data):
      # instructions
      print(load_data["instructions"])
      #attempt
      attempt = load_data["max_attempts"]
      # select levels
      print("Levels:\n 1)Easy\n 2)Medium\n 3)Hard")
      level = input("select the difficulty level: ").strip().capitalize()
      if level == "Easy":
          context = "Fruits"
          print(context)
          secret_word = load_data["difficulty_levels"]["easy"]
          self.guess_secret_word(random.choice(secret_word), attempt)
      elif level == "Medium":
        context = "Animals"
        print(context)
        secret_word = load_data["difficulty_levels"]["medium"]
        self.guess_secret_word(random.choice(secret_word), attempt)
      elif level == "Hard":
        secret_word = load_data["difficulty_levels"]["hard"]
        self.guess_secret_word(random.choice(secret_word), attempt)  
  # The player guessing the secret word          
  def guess_secret_word(self, secret_word:str, attempt:int):    
    guess_word = ["_"]*len(secret_word)
    # print(secret_word)
    # print(len(guess_word))
    print("".join(guess_word))
    while attempt > 0 and "_" in guess_word:
      print(f"Available attempt {attempt}")
      # displaying hint if the attempt had used 3 times
      if attempt <= 3:
        self.display_hint(secret_word)
      # start guessing the word by the player  
      guess = input("Guess the secret word: ")   
      if guess not in list(secret_word):
        print("Invalid guess!!! Try again")
        attempt-=1  
      elif guess in secret_word:
            for index, letter in enumerate(secret_word):
              if letter == guess:
                if guess_word[index] == "_":
                  guess_word[index] = guess  
                else:
                  attempt-=1
            print(''.join(guess_word))
      # declaring winner and losser   
      if "_" not in guess_word:
        print("Congratulation🥳🥳🥳, YOU WIN!!!") 
      elif attempt == 0:
        print("You lose😟😖😖")
        print(f"THE SECRET WORD : {secret_word.upper()}")          
  def display_hint(self, secret_word:str):
    with open("hangman_word.json") as file:
      load_data = json.load(file)
      hint = load_data["hints"]
      for key, value in hint.items():
        if key == secret_word:
          print(f"HINT: {value}")
      if secret_word not in hint.keys():
        print("Hint is not available.")         
def main():
  print("------------------HANGMAN GAME-----------------------")
  try:
    with open("hangman_word.json") as file:
      load_data = json.load(file)
  except FileNotFoundError as ffe:
    print(f"Alert!!! Check your current directory location, {ffe}")    
  game = Hangman_Game()
  game.hangmanWithBot(load_data)
if __name__=="__main__":
  main()