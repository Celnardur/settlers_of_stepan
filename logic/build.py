from logic import player

def build_settlement(state, name, pos):
    if pos < 0 or pos >= len(state['settlements']):
        return (400, "Settlement position does not exist")

    if state['settlements'][pos]['owner'] != -1:
        return (400, "Settlement or city already built in selected position")

    for settlement in state['settlements'][pos]['adj_settlements']:
        if state['settlements'][settlement]['owner'] != -1:
            return (400, "Settlement cannot be built adjacent to another settlement")

    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can build")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot build on this turn")

    acting = state['players'][order]
    if len(acting['settlements']) >= 5:
        return (400, "Can't build more than 5 settlements")

    if acting['taxes_due']:
        return (400, "Must pay taxes before you can build")

    # Can only build one settlement on each opening round
    if state['turn'][0] == 0 and len(acting['settlements']) > 0:
        return (400, "Cannot build more than one settlement on this turn")
    if state['turn'][0] == 1 and len(acting['settlements']) > 1:
        return (400, "Cannot build more than one settlement on this turn")

    # check for adjacent owned roads and resources if not opening round
    if not (state['turn'][0] == 0 or state['turn'][0] == 1):
        owned_adj_roads = 0
        for road in state['settlements'][pos]['roads']:
            if state['roads'][road]['owner'] == order:
                owned_adj_roads += 1
        if owned_adj_roads == 0:
            return(400, "Settlement cannot be built with no connecting road")
        
        (code, message) = player.take_resources(state, name, 
                {'Brick': 1, 'Grain': 1, 'Lumber': 1, 'Wool': 1})
        if code != 200:
            return (400, "Player does not have enough resources to build settlement")

    state['settlements'][pos]['owner'] = order
    state['settlements'][pos]['type'] = 'settlement'
    state['players'][order]['settlements'].append(pos)

    return (200, "Settlement AddeSettlement Addedd")

def build_road(state, name, pos):
    if pos < 0 or pos >= len(state['roads']):
        return (400, "Road position does not exist")

    proposed = state['roads'][pos]

    if proposed['owner'] != -1:
        return (400, "Road already built in selected position")

    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can build")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot build on this turn")

    if state['players'][order]['taxes_due']:
        return (400, "Must pay taxes before you can build")

    if len(state['players'][order]['roads']) >= 15:
        return (400, "You cannot build more than 15 roads")

    # Can only build one road on each opening round
    if state['turn'][0] == 0 and len(state['players'][order]['roads']) > 0:
        return (400, "Cannot build more than one road on this turn")
    if state['turn'][0] == 1 and len(state['players'][order]['roads']) > 1:
        return (400, "Cannot build more than one road on this turn")


    # check for adjacent roads or settlments
    legal = False
    for settlement in proposed['settlements']:
        adj = state['settlements'][settlement]

        if adj['owner'] == order:
            legal = True
            break
        
        # if adjacent spot owned by someone else can't check through it 
        if adj['owner'] != -1:
            continue

        # check for adj roads
        for road in adj['roads']:
            if state['roads'][road]['owner'] == order:
                legal = True
                break

    if not legal:
        return (400, "Can't place a road in that position")

    # extra check for placing next to second settlement for turn 2
    if state['turn'][0] == 1:
        # second settlement will always be in second position
        if len(state['players'][order]['settlements']) < 2:
            return (400, "Have to place second settlement before second road")
        second_settlement = state['players'][order]['settlements'][1]

        if not pos in state['settlements'][second_settlement]['roads']:
            return (400, "Have to build second road next to second settlement")
        
    # check for resources if past set-up
    if state['turn'][0] > 1:
        (code, message) = player.take_resources(state, name, {'Brick': 1, 'Lumber': 1})
        if code != 200:
            return (400, "You do not have enough resources to build a road")

    state['roads'][pos]['owner'] = order
    state['players'][order]['roads'].append(pos)

    return (200, "Road built")

def build_city(state, name, pos):
    if pos < 0 or pos >= len(state['settlements']):
        return (400, "City position does not exist")

    if state['turn'][0] < 2:
        return (400, "City cannot be built on rounds 1 and 2")

    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can build")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot build on this turn")

    acting = state['players'][order]
    if acting['taxes_due']:
        return (400, "Must pay taxes before you can build")

    if len(acting['cities']) >= 4:
        return (400, "Can't build more than 4 cities")

    if not pos in acting['settlements']:
        return (400, "City must be placed on top of existing settlement")

    (code, message) = player.take_resources(state, name, 
            {'Grain': 2, 'Ore': 3})
    if code != 200:
        return (400, "Player does not have enough resources to build city")

    state['settlements'][pos]['type'] = 'city'
    state['players'][order]['settlements'].remove(pos)
    state['players'][order]['cities'].append(pos)

    return (200, "City built")


def draw_dev(state, name):
    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can build")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot draw on this turn")

    if state['players'][order]['taxes_due']:
        return (400, "Must pay taxes before you can build")

    if len(state['developments']) == 0:
        return (400, "No developments left to draw")

    (code, message) = player.take_resources(state, name, 
            {'Grain': 1, 'Ore': 1, 'Wool': 1})
    if code != 200:
        return (400, "Player does not have enough resources to draw development")

    dev = state['developments'].pop()
    state['players'][order]['developments'].append(dev)

    return (200, dev)


# force these things for testing
def force_settlement(state, name, pos):
    order = player.find_player(state, name)
    state['settlements'][pos]['owner'] = order
    state['settlements'][pos]['type'] = 'settlement'
    state['players'][order]['settlements'].append(pos)


def force_road(state, name, pos):
    order = player.find_player(state, name)
    state['roads'][pos]['owner'] = order
    state['players'][order]['roads'].append(pos)




