#!/usr/bin/env python3
import json

def get_char(char, color = None):
    return {'char': char, 'color': color}

def add_num(layout, num, line, col, color = None):
    n = str(num)
    if int(num) < 10:
        layout[line][col] = get_char(n, color)
    else:
        layout[line][col] = get_char(n[0], color)
        layout[line][col+1] = get_char(n[1], color)

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

def get_color(s):
    if s == 'Mountains' or s == 'Ore':
        return [75, 75, 255]
    if s == 'Pasture' or s == 'Wool':
        return [255, 255, 255]
    if s == 'Forest' or s == 'Lumber':
        return [0, 255, 0]
    if s == 'Fields' or s == 'Grain':
        return [255, 255, 0]
    if s == 'Hills' or s == 'Brick':
        return [255, 0, 0]
    if s == 'Desert':
        return [255, 127, 0]
    return None

def get_player_color(name, players):
    for player in players:
        if player['name'] == name:
            return player['color']

    return None


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

def print_hex(state, tile, index, layout, line, col, robber):
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
            layout[l][c] = get_char('B', [0x80, 0, 0x80])
        elif word == 'i':
            add_num(layout, index, l, c)
        elif word == 't':
            add_str(layout, get_abv(tile), l, c, get_color(tile['tile_type']))
        elif word == 'd':
            layout[l][c] = get_char(hex(tile['roll_number'])[2])

        elif word == 'n':
            l += 1
            c = col
        elif word[0] == 'c':
            c += int(word[1])
            
        elif word[0] == 's':
            settlement = tile['settlements'][int(word[1:])]
            owner = state['settlements'][settlement]['owner']
            if owner == -1:
                add_num(layout, settlement, l, c)
            else:
                color = state['players'][owner]['color']
                add_num(layout, settlement, l, c, color)

        elif word[0] == 'r':
            road = tile['roads'][int(word[1:])]
            owner = state['roads'][road]['owner']
            if owner == -1:
                add_num(layout, road, l, c)
            else:
                color = state['players'][owner]['color']
                add_num(layout, road, l, c, color)
        elif word[0] == '/' or word[0] == '\\' or word[0] == '|':
            road = tile['roads'][int(word[1:])]
            owner = state['roads'][road]['owner']
            if owner == -1:
                layout[l][c] = get_char(word[0])
            else:
                color = state['players'][owner]['color']
                layout[l][c] = get_char(word[0], color)


def print_player(layout, player, line, col):
    l = line
    add_str(layout, "Name: " + player['name'], line, col)
    
    l += 1
    add_str(layout, "Color: " + str(player['color']), l, col, player['color'])

    l += 1
    add_str(layout, "Resource: ", l, col)
    c = col + 10
    for res, amt in player['resources'].items():
        add_str(layout, res[0] + str(amt), l, c, get_color(res))
        c += 3

    l += 1
    add_str(layout, "Dev: ", l, col)
    for i, dev in enumerate(player['developments']):
        add_str(layout, dev[0], l, col +5 + i*2)

    l += 1
    add_str(layout, "Army: " + str(player['army']), l, col)
    
    l += 1
    add_str(layout, "Longest Road: " + str(player['longest_road']), l, col)

    l += 1
    add_str(layout, "VP: " + str(player['victory_points']), l, col)

            
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
                print_hex(state, state['hexes'][hid], hid, layout, line, col, state['robber'])
                hid += 1
            elif ud % 2 == 1 and lr % 2 == 1:
                print_hex(state, state['hexes'][hid], hid, layout, line, col, state['robber'])
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

    # Show Players
    l = 2
    for player in state['players']:
        if player != None:
            print_player(layout, player, l, 50)
        l += 10

    # generate string
    board = ""
    for line in layout:
        for char in line:
            if char['color'] != None:
                c = char['color']
                board += '\x1b[38;2;'
                board += str(c[0]) + ';' + str(c[1]) + ';' + str(c[2]) + 'm'
                board += char['char']
                board += '\x1b[0m'
            else:
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

