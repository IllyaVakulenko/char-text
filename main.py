from os import getenv
from dotenv import load_dotenv
from char_map import CHAR_MAP

load_dotenv()

bg = getenv('BACKGROUND', ' ')
fg = getenv('FOREGROUND', '#')


def print_char(char_matrix):
    print('\n'.join(''.join(
        fg if pixel else bg
        for pixel in row)
        for row in char_matrix)
    )


text = "40123?"

for char in text:
    if char in CHAR_MAP:
        print_char(CHAR_MAP[char])
    else:
        print_char(CHAR_MAP["?"])
