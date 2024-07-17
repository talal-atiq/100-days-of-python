#importing modules:
import random
import hangman_art
import hangman_words


print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Assigning conditions:
end_of_game = False
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Creating blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

  
    if guess in display:
      print(f"You already guessed {guess} this letter.")
  

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

#Printing the ASCII arts of lives:
    print(hangman_art.stages[lives])
input()    
