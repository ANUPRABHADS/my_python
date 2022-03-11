from random import randint
from guess_art import logo
easy_level=10
hard_level=5

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = randint(1,100)
  turns=set_turns()
  guess=0
  while guess!=number:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess=int(input("Make a Guess : "))
    turns= check_answer(guess, number, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != number:
      print("Guess again.")
  
 
def set_turns():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy': 
    return easy_level
  else:
    return hard_level

def check_answer(guess,number,turns):
  if guess<number:
    print("guess number is too small")
    return turns-1
  elif guess>number:
    print(" too large")
    return turns-1
  elif guess==number:
    print(f"You got it. The answer was {number}")

game()