import random
from words import list_of_words

hangman = [
"""
+---+
    |
    |
    |
    ===
""", 
"""
+---+
  | |
  O |
    |
    ===
""", 
"""
+---+
  | |
  O |
 /| |
    ===
""", 
"""
+---+
  | |
  O |
 /|\|
    ===
""", 
"""
+---+
  | |
  O |
 /|\|
 /  ===
""", 
"""  
+---+
  | |
  O |
 /|\|
 / \  ===
"""
]

word = random.choice(list_of_words).upper()

correct_guess = []
incorrect_guess = []
attempt = 6
hangman_count = -1

while attempt >0:
    output =''
    for letter in word:
        if letter in correct_guess:
            output += letter
        else:
            output += '_ '
            
    if output == word:
        break
    
    print("Guess the word: ", output)
    print(attempt, " Attempts left")
    
    guess = input().upper()
    
    if guess in correct_guess or guess in incorrect_guess:
        print("Already guessed", guess)
    elif guess in word:
        print("Correct letter, guess more")
        correct_guess.append(guess)
    else:
        print("Your guess is wrong")
        hangman_count += 1
        attempt -=1
        incorrect_guess.append(guess)
        print(hangman[hangman_count])
        
if attempt>0:
    print("You guessed the right word. You WIN!!!")
else:
    print("Wrong letter guessed. The correct word is {}".format(word))
