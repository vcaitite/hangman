import read_txt_archive as read_txt
import utils
import ascii_arts
import getpass
from replit import clear

# Giving welcome and printing the logo
print(ascii_arts.welcome_image)
print("Welcome to the hangman game!")

# Asking the player to choose an option of the game and defining the word
play_option = int(input("Which do you prefer: 1- Type a word; or 2- Play with a random word.  "))
secret_word = ""
if play_option == 1:
    secret_word = getpass.getpass(prompt='Type a secret word: ').lower()
elif play_option == 2:
    secret_word = read_txt.read_random_word()

# Printing display:
display = utils.display([], secret_word)
print(display)
lives = 6

# While loop to let the user guess again until complete
# the word or complete the number of tries.
while "_" in display and lives > 0:
    # Asking the user to guess a letter:
    letter_guess = input("Guess a letter please: ").lower()
    # Clear the screen
    clear()
    # Catches the position of a letter in the secret word
    letter_position = utils.check_guessed_letter(letter_guess, secret_word)
    if len(letter_position) == 0:
        lives -= 1
        print("This letter is not in the secret word")
    elif letter_guess in display:
        print("Pay attention, you had already typed this word!")
    # Updating (or not) the display
    display = utils.display(letter_position, secret_word, display)
    # Printing the display and the stages:
    print(display)
    print(ascii_arts.stages[lives])


# Printing the result
if "_" not in display:
    print(ascii_arts.win)
else:
    print(ascii_arts.lose)

# Printing the solution
print(f"The secrete word was: " + secret_word)

