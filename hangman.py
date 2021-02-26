import read_txt_archive as read_txt
import getpass
import random

print('''

888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"    

''')

print("Welcome to the hangman game!")
play_option = int(input("Which do you prefer: 1- Type a word; or 2- Play with a random word."))
if play_option == 1:
    secret_word = getpass.getpass(prompt='Type a secret word: ').lower()
elif play_option == 2:
    word_line = random.randint(0, read_txt.archive_lines())

print(word_line)

