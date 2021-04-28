from logic import player
import random
import math

def end_turn(state, notifications, name):
    # Check player
    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player does not exist")

    if order != state['turn'][1]:
        return (400, "You cannot end the turn")

    # Check robber and taxes
    if state['move_robber'] != -1:
        return (400, "The robber must be moved before the turn can end")

    for actor in state['players']:
        if actor['taxes_due']:
            return (400, "All players must pay taxes before the turn can end")

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
        
        # add notification for resources
        name = state['players'][order]['name']
        if not name in notifications:
            notifications[name] = []
        res = state['players'][order]['resources']
        notifications[name].append({'action': 'end_round_2', 'resources': res})
        
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
    print(roll)

    # create notifications
    notify = {}
    for order, actor in enumerate(state['players']):
        notify[order] = {
            'action': 'end_turn', 
            'roll': roll, 
            'resources': {'Brick': 0, 'Lumber': 0, 'Ore': 0, 'Grain': 0, 'Wool': 0},
            'move_robber': False,
            'pay_taxes': False,
        }

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
                notify[settlement['owner']]['resources'][res] += 1
            if settlement['type'] == 'city':
                state['players'][settlement['owner']]['resources'][res] += 2
                notify[settlement['owner']]['resources'][res] += 2

    # logic for rolling a 7
    #if roll == 7: # hope and pray
    #    state['move_robber'] = state['turn'][1]
    #    notify[state['turn'][1]]['move_robber'] = True
    #    for order, actor in enumerate(state['players']):
    #        res_total = sum(actor['resources'].values())
    #        if res_total > 7:
    #            actor['taxes_due'] = True
    #            notify[order]['pay_taxes'] = True

    # add notifications
    for order, action in notify.items():
        name = state['players'][order]['name']
        if not name in notifications:
            notifications[name] = []
        notifications[name].append(action)

    return (200, "Advanced Turn")

def move_robber(state, notifications, mover, to, victim):
    if to < 0 or to >= len(state['hexes']):
        return (400, "Tile position does not exist")

    if state['robber'] == to:
        return (400, "Must move robber to different position")

    mover = player.find_player(state, mover)
    if mover == -1:
        return (400, 'Nonexistent player given as mover')

    if mover != state['turn'][1]:
        return (400, "Must move robber on your turn")

    if state['players'][mover]['taxes_due']:
        return (400, "Must pay taxes before moving the robber")

    if mover != state['move_robber']:
        return (400, "Mover is not allowed to move the robber")

    # robber can be moved to hex with no player adjacent
    # eaither the victim must be adjacent or no player adjacent
    # find adjacent players
    adj = []
    for intersection in state['hexes'][to]['settlements']:
        if state['settlements'][intersection]['owner'] != -1:
            adj.append(state['settlements'][intersection]['owner'])

    if victim == None and len(adj) > 0:
        return (400, "Must chose victim if robber is moved there")

    stolen = None
    if victim != None:
        victim = player.find_player(state, victim)
        if victim == -1:
            return (400, 'Nonexistent player given as victim')

        if not victim in adj:
            return (400, "Must chose victim with adjacent settlement")

        if state['players'][victim]['taxes_due']:
            return (400, "Victim must pay taxes before he can be stolen from")

        steal_from = []
        for res, amt in state['players'][victim]['resources'].items():
            for i in range(amt):
                steal_from.append(res)
        
        if len(steal_from) > 0:
            stolen = random.choice(steal_from)
            state['players'][victim]['resources'][stolen] -= 1
            state['players'][mover]['resources'][stolen] += 1
        
            thief = state['players'][mover]['name']
            notify = {'action': 'steal', 'thief': thief, 'resource': stolen}
            victim_name = state['players'][victim]['name']
            if victim_name not in notifications:
                notifications[victim_name] = []
            notifications[victim_name].append(notify)

    state['robber'] = to
    state['move_robber'] = -1
    return (200, stolen)

def pay_taxes(state, name, taxes):
    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player does not exist")

    actor = state['players'][order]
    if not actor['taxes_due']:
        return (400, "You don't need to pay taxes")

    current_sum = sum(actor['resources'].values())
    taxes_sum = 0
    for res, amt in taxes.items():
        if amt < 0:
            return (400, "Can't pay negitive resources in taxes")
        taxes_sum += amt
    
    taxes_due = math.floor(current_sum/2) 
    if taxes_due > taxes_sum:
        return (400, "That's not enough resources")
    if taxes_due < taxes_sum:
        return (400, "Select less resources, pay less taxes")

    (code, message) = player.take_resources(state, name, taxes)
    if code != 200:
        return (400, "You cant pay those resources")

    actor['taxes_due'] = False
    return (200, "Taxes paid")


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



