import random

word = input("What would you like to repeat? ")
times = int(input("How many times would you like to repeat this? "))
secondary = input("What is your secondary message to repeat? ")
i = 0
while i < times:
  i += 1
  print(str(word) + " ", end = '')
  if random.randint(0,100) == 8:
    print(str(secondary) + " ", end = '')