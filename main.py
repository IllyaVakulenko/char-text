from char_map import char_map

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
    if char in char_map:
        print_char(char_map[char])
    else:
        print_char(char_map["?"])
