def check_guessed_letter(letter, word):
    letter_position = []  # This means that the word doesn't have the letter
    for index in range(0, len(word)):
        if letter == word[index]:
            letter_position.append(index)
    return letter_position


def display(letter_position, word, last_display=[]):
    display = last_display
    if len(display) == 0:
        for index in range(len(word) - 1):
            display.append("_")
    else:
        for index in range(len(word)-1):
            if index in letter_position:
                display[index] = (word[index])
    return display

