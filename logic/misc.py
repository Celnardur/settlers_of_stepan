import random

def shuffle_board(state):
    tile_types = [
        "Mountains",
        "Mountains",
        "Mountains",
        "Pasture",
        "Pasture",
        "Pasture",
        "Pasture",
        "Forest",
        "Forest",
        "Forest",
        "Forest",
        "Fields",
        "Fields",
        "Fields",
        "Fields",
        "Hills",
        "Hills",
        "Hills",
        "Desert",
    ]

    random.shuffle(tile_types)
    for i, tile in enumerate(state['hexes']):
        tile['tile_type'] = tile_types[i]

    shuffle_numbers(state)

    for i, tile in enumerate(state['hexes']):
        if tile['tile_type'] == 'Desert':
            state['robber'] = i


def shuffle_numbers(state):
    # generate roll numbers
    rolls = []
    for i in range(2, 13):
        if i == 7:
            continue
        if i != 2 and i != 12:
            rolls.append(i)
        rolls.append(i)

    bad = True
    while(bad):
        bad = False
        # randomly assign
        random.shuffle(rolls)
        roll = 0 
        for tile in state['hexes']:
            if tile['tile_type'] == 'Desert':
                tile['roll_number'] = -1
            else:
                tile['roll_number'] = rolls[roll]
                roll += 1

        # check for adjacent 'red numbers'
        for tile in state['hexes']:
            for adj in tile['adj_tiles']:
                if is_red(tile['roll_number']) and is_red(state['hexes'][adj]['roll_number']):
                    bad = True

def is_red(number):
    if number == 6 or number == 8:
        return True
    else:
        return False

