def calculate_vp(state, notifications):
    # check to make sure game actually started
    if len(state['players']) < 3:
        return
    for actor in state['players']:
        if actor is None:
            return

    # update player vp
    winner = -1
    for order, actor in enumerate(state['players']):
        actor['victory_points'] = player_vp(state, order)
        if actor['victory_points'] >= 10:
            winner = order

    if winner != -1:
        for order, actor in enumerate(state['players']):
            if not actor['name'] in notifications:
                notifications[actor['name']] = []
            if order == winner:
                notifications[actor['name']].append({'action': 'win', 'winner': True})
            else:
                notifications[actor['name']].append({'action': 'win', 'winner': False})

def player_vp(state, order):
    actor = state['players'][order]
    vp = 0

    vp += len(actor['settlements'])
    vp += 2*len(actor['cities'])

    if state['longest_road'] == order:
        vp += 2
    if state['largest_army'] == order:
        vp += 2

    for card in actor['developments']:
        if card == 'vp':
            vp += 1

    for card in actor['dev_queue']:
        if card == 'vp':
            vp += 1

    return vp

def update_largest_army(state):
    biggest = 0
    largest_army = -1
    for order, actor in enumerate(state['players']):
        if actor['army'] > biggest:
            largest_army = order
            biggest = actor['army']
        elif actor['army'] == biggest:
            largest_army = -1

    if largest_army != -1 and biggest >= 3:
        state['largest_army'] = largest_army

def update_longest_roads(state):
    for order, actor in enumerate(state['players']):
        actor['longest_road'] = player_longest_road(state, order)

    longest = 0
    long_bois = []
    for order, actor in enumerate(state['players']):
        if actor['longest_road'] > longest:
            longest = actor['longest_road']
            long_bois = []
            long_bois.append(order)
        elif actor['longest_road'] == longest:
            long_bois.append(order)
    
    if longest < 5:
        state['longest_road'] = -1
    elif len(long_bois) > 1 and state['longest_road'] not in long_bois:
        state['longest_road'] = -1
    elif len(long_bois) == 1:
        state['longest_road'] = long_bois[0]

def player_longest_road(state, order):
    actor = state['players'][order]
    longest = 0
    for road in actor['roads']:
        for intersection in state['roads'][road]['settlements']:
            longest = max(longest, find_longest_road_from(state, order, intersection, road))
    return longest

def find_longest_road_from(state, order, intersection, from_road):
    owner = state['settlements'][intersection]['owner']
    if owner != -1 and owner != order:
        return 1

    length = 1
    for road in state['settlements'][intersection]['roads']:
        if state['roads'][road]['owner'] == order and road != from_road:
            next_inter = -1
            for inter in state['roads'][road]['settlements']:
                if inter != intersection:
                    next_inter = inter
            length =  max(length, 1 + find_longest_road_from(state, order, next_inter, road))

    return length


    

