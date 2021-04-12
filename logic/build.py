from logic import player

def build_settlement(state, name, pos):
    if pos < 0 or pos >= len(state['settlements']):
        return (400, "Settlement position does not exist")

    if state['settlements'][pos]['owner'] != -1:
        return (400, "Settlement already built in selected position")

    for settlement in state['settlements'][pos]['adj_settlements']:
        if state['settlements'][settlement]['owner'] != -1:
            return (400, "Settlement cannot be built adjacent to another settlement")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot build on this turn")

    if len(state['players'][order]['settlements']) >= 5:
        return (400, "Can't build more than 5 settlements")

    # check for adjacent owned roads and resources if not opening round
    if not (state['turn'][0] == 0 or state['turn'][0] == 1):
        owned_adj_roads = 0
        for road in state['settlements'][pos]['roads']:
            if road['owner'] == order:
                owned_adj_roads += 1
        if owned_adj_roads == 0:
            return (400, "Settlement cannot be built with no connecting road")
        
        (code, message) = player.take_resources(state, name, 
                {'Brick': 1, 'Grain': 1, 'Lumber': 1, 'Wool': 1})
        if code != 200:
            return (400, "Player does not have enough resources to build settlement")

    state['settlements'][pos]['owner'] = order
    state['players'][order]['settlements'].append(pos)

    #TODO: add round 2 logic
    #TODO: add vp logic

    return (400, "Not implemented")

