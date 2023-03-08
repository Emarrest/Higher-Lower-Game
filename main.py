import art
from game_data import data
import random

score = 0
flag = True

def compare(value1, value2):
  global flag
  global score
  """Compares two values taken from a dictionary and checks the guess provided by the user
   and if the user guesses the greatest one the score increments """
  if value1 > value2:
    print(f"you lost, final score {score}")                     # <- providing output
    flag = False
  elif value2 > value1:                                         # <- comparing the values
    score += 1
    print(f"You correct, current score {score}")                # <- providing output for the result of the comparison
  elif value1 == value2:
    print("They have the same followers, let's try again")      # <- If the values are equal then it's going to restart
  else:
    print("Invalid input, shutting game")                       # <- preventing invalid input
    flag = False

def random_value(person):
    person = {}
    person = random.choice(data)
    return person

temp1 = ""
person2 = random_value(temp1)

print(art.logo)

while flag == True:
  person1 = person2
  followers1 = person1['follower_count']
  if person1 == person2:
    person2 = random.choice(data)

  followers2 = person2['follower_count']

  name = person1['name']
  description = person1['description']
  country = person1['country']
  first_guy = ""
  first_guy = name + " a "  + description + " from " +  country

  name2 = person2['name']
  description2 = person2['description']
  country2 = person2['country']
  second_guy = ""
  second_guy = name2 + " a " + description2 + " from " + country2
  print(f"Compare A: {first_guy}")                                    # <- outputting the two values found

  print(art.vs)

  print(f"Against B: {second_guy}")
  response = input("Who has more followers? Type 'A' or 'B': ")
  if response == "A":
    compare(value1 = followers2, value2 = followers1)
  elif response == "B":
    compare(value1 = followers1, value2 = followers2)

# * random value from a list of dictionaries
# * converting dictionary to int
# * compare function
# * runtime score(output)
# * increment comments

# -> Main logo
# Compare A: Maluma, a Musician, from Colombia.
# Who has more followers? Type 'A' or 'B':

# -> VS logo

# Against B: Beyoncé, a Musician, from United States.
# Who has more followers? Type 'A' or 'B':

# * Correct answer
# You're right! Current score: 1.

# ! Wrong answer or invalid input
# Sorry, that's wrong. Final score: 1.