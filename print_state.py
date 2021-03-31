#!/usr/bin/env python3
import json

def get_char(char, color = None):
    return {'char': char, 'color': color}

def add_num(layout, num, line, col):
    n = str(num)
    if int(num) < 10:
        layout[line][col] = get_char(n)
    else:
        layout[line][col] = get_char(n[0])
        layout[line][col+1] = get_char(n[1])

def add_str(layout, string, line, col, color = None):
    l, c = (line, col)
    for char in string:
        if char == '\n':
            l += 1
            c = col
        elif char == ' ':
            c += 1
        else:
            layout[l][c] = get_char(char, color)
            c+=1

def get_abv(tile):
    tt = tile['tile_type']
    if tt == 'Mountains':
        return 'Mntn'
    if tt == 'Pasture':
        return 'Pstr'
    if tt == 'Forest':
        return 'Frst'
    if tt == 'Fields':
        return 'Flds'
    if tt == 'Hills':
        return 'Hill'
    if tt == 'Desert':
        return 'Dsrt'

def print_hex(tile, index, layout, line, col, robber):
    fmt = r"""
    c4    s0    n
    c3 /5 c2 \0 n
    c2 r5 c4 r0 n
    c1 /5 c6 \0 n

    s5 c4 b c4 s1 n
    |4 c4 i c4 |1 n
    r4 c3 t c5 r1 n
    |4 c4 d c4 |4 n
    s4 c4   c4 s2 n

    c1 \3 c6 /2 n
    c2 r3 c4 r2 n
    c3 \3 c2 /2 n
    c4    s3
    """

    l, c = (line, col)
    for word in fmt.split():
        if word == 'b' and robber == index:
            layout[l][c] = get_char('B')
        elif word == 'i':
            add_num(layout, index, l, c)
        elif word == 't':
            add_str(layout, get_abv(tile), l, c)
        elif word == 'd':
            layout[l][c] = get_char(hex(tile['roll_number'])[2])
        elif word == 'n':
            l += 1
            c = col
        elif word[0] == 'c':
            c += int(word[1])
        elif word[0] == 's':
            add_num(layout, tile['settlements'][int(word[1:])], l, c)
        elif word[0] == 'r':
            add_num(layout, tile['roads'][int(word[1:])], l, c)
        elif word[0] == '/' or word[0] == '\\' or word[0] == '|':
            layout[l][c] = get_char(word[0])
            
def get_state_string(state):
    # Make empty layout
    layout = []
    for i, line in enumerate(range(45)):
        layout.append([])
        for col in range(80):
            layout[i].append({'char': ' ', 'color': None})

    # Draw Hexagons
    hid = 0
    for ud in range(5):
        for lr in range(9):
            line = ud * 8
            col = lr * 4
            if ud % 2 == 0 and lr % 2 == 0:
                if (ud == 0 or ud == 4) and (lr == 0 or lr == 8):
                    continue
                print_hex(state['hexes'][hid], hid, layout, line, col, state['robber'])
                hid += 1
            elif ud % 2 == 1 and lr % 2 == 1:
                print_hex(state['hexes'][hid], hid, layout, line, col, state['robber'])
                hid += 1
    
    # Draw Harbors
    add_str(layout, "3?--\n|\n|\n|", 0, 8)
    add_str(layout, "--2G\n   |\n   |\n   |", 0, 21)
    add_str(layout, "--2O\n  |\n  |\n  |", 8, 34)
    add_str(layout, "2L--\n \\\n  \\\n   \\", 12, 0)
    add_str(layout, "\\\n 3?\n/", 21, 42)
    add_str(layout, "   /\n  /\n /\n2B--", 29, 0) 
    add_str(layout, "  |\n  |\n  |\n--2W", 33, 34) 
    add_str(layout, "|\n|\n|\n3?--", 41, 8)
    add_str(layout, "  |\n  |\n  |\n--3?", 41, 22) 

    board = ""
    for line in layout:
        for char in line:
            board += char['char']
        board += "\n"
    return board

def print_state(state):
    print(get_state_string(state))
    return

if __name__ == '__main__':
    state = {}
    with open('state.json', 'r') as fs:
        text = fs.read()
        state = json.loads(text)

    print_state(state)

