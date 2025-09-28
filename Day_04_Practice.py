import random

#HEADS OR TAILS PRACTICE - 1

number = random.randint(0, 1)
print(number)
if number == 0:
    print("Heads")
else:
    print("Tails")



#BANKER ROULLETE PRACTICE - 2

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

friends_index = random.randint(0, 4)
print(friends[friends_index])