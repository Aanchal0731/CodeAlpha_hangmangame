#generate a random word
import random
import hangman_visuals
import word_file

chosen_word = random.choice(word_file.words)
print('======================================')
lives = 6 

#generate as many blanks as letters in a word 
display = []   #take an empty 
for letter in chosen_word:
    display += '_'
print(display)   

#check if guessed letter is in word or not?
game_over = False
while not game_over:
    guessed_letter = input('Guess a letter:').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
           display[position] = guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives -= 1 
        if lives == 0:
            game_over = True
            print('You Lose!')
    if '_' not in display:
        game_over = True
        print('You Win!')
    print(hangman_visuals.visuals[lives])
          
