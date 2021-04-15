from logic import player

def build_settlement(state, name, pos):
    if pos < 0 or pos >= len(state['settlements']):
        return (400, "Settlement position does not exist")

    if state['settlements'][pos]['owner'] != -1:
        return (400, "Settlement or city already built in selected position")

    for settlement in state['settlements'][pos]['adj_settlements']:
        if state['settlements'][settlement]['owner'] != -1:
            return (400, "Settlement cannot be built adjacent to another settlement")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot build on this turn")

    acting = state['players'][order]
    if len(player['settlements']) >= 5:
        return (400, "Can't build more than 5 settlements")

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

    #TODO: add vp logic

    return (400, "Not implemented")

def build_road(state, name, pos):
    if pos < 0 or pos >= len(state['road']):
        return (400, "Road position does not exist")

    proposed = state['road'][pos]

    if proposed['owner'] != -1:
        return (400, "Road already built in selected position")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if len(state['players'][order]['roads']) >= 15:
        return (400, "You cannot build more than 15 roads")

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

    # TODO: add vp logic
    
    return (200, "Road built")


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




