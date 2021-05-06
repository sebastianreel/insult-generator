# Sebastian Reel
# Python Practice
# Randomized Insult Generator
#-----------------------------#

# first get the user's name and age for insult parameteres
print("What is your name? ")
name = input(name)
print("Hello " + name)
print()

print("What is your age, " + name + "?")
age = int(input("Age: "))
print()

# now define a function with insults and parameters
from random import choice
def printInsult (name, age):
  adjectives = ["big", "poopy", "dumb", "silly", "stinky", "cranky", "weird", "trashy"]
  nouns = ["turnip", "dog", "fart", "hairball", "chicken", "wet-wipe", "hag", "whale"]
  if(age < 16):
    ageA = "young "
    print (name + ", you are a " + ageA + choice(adejctives) + " " + choice(nouns))
  else:
    ageA = "old "
    print (name + ", you are an " + ageA + choice(adjectives) + " " + choice(nouns))
printInsult(name, age)
