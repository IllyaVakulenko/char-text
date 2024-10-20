from char_map import CHAR_MAP

THEME = {
    "background": " ",
    "foreground": "#"
}

bg = THEME["background"]
fg = THEME["foreground"]


def print_char(char_matrix):
    for row in char_matrix:
        line = ''.join(fg if pixel else bg for pixel in row)
        print(line)


text = "40123?"

for char in text:
    if char in CHAR_MAP:
        print_char(CHAR_MAP[char])
    else:
        print_char(CHAR_MAP["?"])
