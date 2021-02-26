from pathlib import Path

path = Path('./word_list.txt')


def archive_lines():
    if path.is_file():
        with open(path, 'r') as f:
            n_lines = len(f.readlines())
            return n_lines
    else:
        print("Word list archive doesn't exist 😞")
    return 0
