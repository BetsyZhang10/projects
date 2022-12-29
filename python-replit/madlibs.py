# use f-strings to create a string concentation
#declare variables
# intro
print(
  "Welcome to my small madlibs project! This madlibs was created to learn how to generate user inputs and\ndeclare variables.\n"
)

print(
  "The project was made following the freecodecamp\ntutorial on YouTube which you can check out here:\nhttps://youtu.be/8ext9G7xspg\nThis will also be amongst the first projects\nI have made using Python. Have fun!\n"
)
print("Sincerely, SOUL.\n")

# starting prompt
print(
  "Welcome. To begin the game, please answer the following prompts.\nBonus points: be funny!\n"
)

# get user input
noun1 = input("your name: ")
noun2 = input("your age: ")
verb1 = input("What do you do when you're bored? : ")
noun3 = input("your favorite food: ")
dream = input("You've always wanted to: ")
print("Madlibs 1\n")

# madlibs sentence
print("Here are your results:\n")

madlibs1 = f"My name is {noun1}.\nI am {noun2} years old.\nHere is a bit about myself.\nWhen I am bored, I like to {verb1}.\nMy favorite food is {noun3}.\nMy dream is to {dream}."

print(madlibs1)
