char_map = {
    "0": [[0, 1, 1, 1, 0,],
          [1, 0, 0, 0, 1,],
          [1, 0, 0, 1, 1,],
          [1, 0, 1, 0, 1,],
          [1, 1, 0, 0, 1,],
          [1, 0, 0, 0, 1,],
          [0, 1, 1, 1, 0,],
          [0, 0, 0, 0, 0,]],
    "?": [[0, 1, 1, 1, 0,],
          [1, 0, 0, 0, 1,],
          [0, 0, 0, 1, 0,],
          [0, 0, 1, 0, 0,],
          [0, 0, 1, 0, 0,],
          [0, 0, 0, 0, 0,],
          [0, 0, 1, 0, 0,]]
}

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


text = "0?"

for char in text:
    if char in char_map:
        print_char(char_map[char])
