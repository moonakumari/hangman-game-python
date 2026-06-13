# TASK 1: Hangman Game
import random

words = ["apple", "banana", "python", "mango", "laptop"]

word = random.choice(words)

display = ["_"]*len(word)

wrong_guess = 0
max_guess = 6

print("Welcome to Hangman Game!")

while True:
    print("word:", display)

    guess = input("Enter letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("correct guess") 
        
    else:
        wrong_guess += 1
        print("wrong guess")

    if "_" not in display:
       print("you win! word is:", word)
       break

    if wrong_guess == max_guess:
        print("you lose! word was:", word)
        break

