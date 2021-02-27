from pathlib import Path
import random


path = Path('./word_list.txt')


def archive_lines():
    if path.is_file():
        with open(path, 'r') as f:
            lines = (f.readlines())
            return lines
    else:
        raise Exception("Word list archive doesn't exist 😞")


def read_random_word():
    lines = archive_lines()
    n_words = len(lines)
    word_line = random.randint(0, n_words)
    return lines[word_line]



