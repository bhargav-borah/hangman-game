import random

words =  ["rainbow", "computer", "python", "mathematics","reverse","water" , "boat"]
used_chars = []

def display(game_map):
    print(end = "Word: ")
    for i in game_map:
        print(i, end = " ")
    print()

def update(game_map, char):
    for i in range(len(word)):
        if(word[i] == char):
            game_map[i] = char
   
def play(word):
    display(game_map)
    char = input("Enter your guess: ")
   
    if char not in used_chars:
        if char in word:
            print("Correct guess!")
            update(game_map, char)
            used_chars.append(char)
        else:
            print("Wrong guess!")
    else:
        print("You have already input this character")
   
   
def check_continuation():
    return not (len(word) == (len(game_map)-game_map.count("_")))

word = random.choice(words)

game_map = ["_" for i in word]

game_on = True
while game_on:
    play(word)
    game_on = check_continuation()
    if not game_on:
        print("Congrats!! You guessed the complete word")
        display(game_map)