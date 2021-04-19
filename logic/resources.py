from logic import player
import random

def end_turn(state, name):
    # Check player
    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player does not exist")

    if order != state['turn'][1]:
        return (400, "You cannot end the turn")
    
    # check to make sure appropiate number of settlements and roads are built
    player = state['players'][order]
    if state['turn'][0] == 0:
        if len(player['settlements']) < 1 or len(player['roads']) < 1:
            return (400, "Need to build 1 settlement and 1 road this turn")
            

    # advance turn counter
    if state['turn'][1] == len(state['players']) - 1:
        state['turn'] = [state['turn'][0] + 1, 0]
    else:
        state['turn'][1] += 1

    # TODO: add get resources at end of each round 2

    # roll for resources if after round 2
    if state['turn'][0] < 2:
        return (200, "Advanced Turn")
    
    roll = random.randrange(1, 7) + random.randrange(1, 7)

    matches = [tile for tile, h in enumerate(state['hexes']) 
            if h['roll_number'] == roll and state['robber']]

    return (200, "Advanced Turn")

def resource_from_tile(state, tile):
    tt = state['hexes'][tile]['tile_type']
    if tt == 'Mountains':
        return 'Ore'
    if tt == 'Pasture':
        return 'Wool'
    if tt == 'Forest':
        return 'Lumber'
    if tt == 'Fields':
        return 'Grain'
    if tt == 'Hills':
        return 'Brick'
    return None


def force_turn(state):
    if state['turn'][1] == len(state['players']) - 1:
        state['turn'] = [state['turn'][0] + 1, 0]
    else:
        state['turn'][1] += 1

def infinte_resources(state):
    for player in state['players']:
        player['resources'] = {'Brick': 50, 'Grain': 50, 'Lumber': 50, 'Ore': 50, 'Wool': 50}

def strip_resources(state):
    for player in state['players']:
        player['resources'] = {'Brick': 0, 'Grain': 0, 'Lumber': 0, 'Ore': 0, 'Wool': 0}



