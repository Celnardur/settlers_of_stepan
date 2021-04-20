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
    actor = state['players'][order]
    if state['turn'][0] == 0:
        if len(actor['settlements']) < 1 or len(actor['roads']) < 1:
            return (400, "Need to build 1 settlement and 1 road this turn")
    if state['turn'][0] == 1:
        if len(actor['settlements']) < 2 or len(actor['roads']) < 2:
            return (400, "Need to build 1 settlement and 1 road this turn")

    # reset dev card tracker
    state['card_played'] = False

    # round 2 goes in the oppsite direction
    if state['turn'] == [0, len(state['players']) - 1]:
        state['turn'] = [1, len(state['players']) - 1]
        return (200, "Advanced Turn")

    # round 2 logic
    if state['turn'][0] == 1:
        # starting resources after round 2
        order = state['turn'][1]
        settlement = state['players'][order]['settlements'][1]
        for tile in state['settlements'][settlement]['hexes']:
            res = resource_from_tile(state, tile)
            if res != None:
                state['players'][order]['resources'][res] += 1

        # round 2 goes in the oppsite direction
        if state['turn'][1] == 0:
            state['turn'] = [2, 0]
        else:
            state['turn'][1] -= 1
        
        return (200, "Advanced Turn")

    # advance turn counter
    if state['turn'][1] == len(state['players']) - 1:
        state['turn'] = [state['turn'][0] + 1, 0]
    else:
        state['turn'][1] += 1

    # roll for resources if after round 2
    if state['turn'][0] < 2:
        return (200, "Advanced Turn")
    
    roll = random.randrange(1, 7) + random.randrange(1, 7)

    # find tiles that have the right roll number
    matches = []
    for i, tile in enumerate(state['hexes']):
        if tile['roll_number'] == roll and i != state['robber']:
            matches.append(tile)

    # give resources to adj intersections of match
    for tile in matches:
        res = tt_to_resource(tile['tile_type'])
        for intersection in tile['settlements']:
            settlement = state['settlements'][intersection]
            if settlement['type'] == 'settlement':
                state['players'][settlement['owner']]['resources'][res] += 1
            if settlement['type'] == 'city':
                state['players'][settlement['owner']]['resources'][res] += 2

    # TODO: add logic for taxes and robber
    if roll == 7: # hope and pray
        pass

    return (200, "Advanced Turn")

def resource_from_tile(state, tile):
    tt = state['hexes'][tile]['tile_type']
    return tt_to_resource(tt)

def tt_to_resource(tt):
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



