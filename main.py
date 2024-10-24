#Step 1 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["glupamaca"]


import random
chosen_word = random.choice(word_list)
chosen_word_list = []
number = 0
lives = 6
display = []
for letter in chosen_word:
    number += 1
    chosen_word_list.append(letter)
    display.append("_")
#print (chosen_word)
while display.count("_") > 0 and lives > 0:
    guess = input("Guess a letter ? ").lower()
    for position in range (number):
        if chosen_word_list[position] == guess:
            display[position] = guess
    if chosen_word_list.count(guess) == 0:
        lives -= 1
    
#print(chosen_word_list)
    print(display)
    print(f"{stages[lives]}")
#print(number)
if lives == 0:
    print ("\n\n\n\nGame over - you lost!")
else:
    print("\n\n\n\nGame over - you won!")

