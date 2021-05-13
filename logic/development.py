from logic import player
from logic import resources
from logic import build
from logic import vp

def play_knight(state, notifications, name, to, victim):
    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can Play a knight")

    if state['card_played']:
        return (400, "Cannot play two dev cards per turn")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot play developments on this turn")

    if state['players'][order]['taxes_due']:
        return (400, "Must pay taxes before you can play developments")

    actor = state['players'][order]

    if 'knight' not in actor['developments']:
        return (400, "Player doesn't have a knight card")

    state['move_robber'] = order
    (code, message) = resources.move_robber(state, notifications, name, to, victim)
    if code != 200:
        return (400, message)

    actor['developments'].remove('knight')
    actor['army'] += 1
    state['card_played'] = True
    vp.update_largest_army(state)
    return (200, message)

def play_build_road(state, name, one, two):
    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can Play a Card")

    if state['card_played']:
        return (400, "Cannot play two dev cards per turn")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot play developments on this turn")

    if state['players'][order]['taxes_due']:
        return (400, "Must pay taxes before you can play developments")

    actor = state['players'][order]
    
    if 'road' not in actor['developments']:
        return (400, "Player doesn't have a Build Roads card")

    actor['resources']['Brick'] += 2
    actor['resources']['Lumber'] += 2

    (code, message) = build.build_road(state, name, one)
    if code != 200:
        actor['resources']['Brick'] -= 2
        actor['resources']['Lumber'] -= 2
        return (400, message)

    (code, message) = build.build_road(state, name, two)
    if code != 200:
        actor['resources']['Brick'] -= 1
        actor['resources']['Lumber'] -= 1
        return (400, message)

    actor['developments'].remove('road')
    state['card_played'] = True
    return (200, "Roads built")

def play_year_of_plenty(state, name, one, two):
    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can Play a Card")

    if state['card_played']:
        return (400, "Cannot play two dev cards per turn")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot play developments on this turn")

    if state['players'][order]['taxes_due']:
        return (400, "Must pay taxes before you can play developments")

    actor = state['players'][order]
    
    if 'plenty' not in actor['developments']:
        return (400, "Player doesn't have a Year of Plenty card")

    if one not in actor['resources'] or two not in actor['resources']:
        return (400, "Cannot request those resources")

    actor['resources'][one] += 1
    actor['resources'][two] += 1
    actor['developments'].remove('plenty')
    state['card_played'] = True
    return (200, "Resources have been given")

def play_monopoly(state, notifications, name, resource):
    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can Play a Card")

    if state['card_played']:
        return (400, "Cannot play two dev cards per turn")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot play developments on this turn")

    if state['players'][order]['taxes_due']:
        return (400, "Must pay taxes before you can play developments")

    actor = state['players'][order]
    
    if 'monopoly' not in actor['developments']:
        return (400, "Player doesn't have a Monoopoly card")

    for person in state['players']:
        if person['taxes_due']:
            return (400, "All players must pay taxes before you can play this card")

    if resource not in actor['resources']:
        return (400, "That's not a valid resource")

    for person in state['players']:
        if person['name'] != actor['name']:
            actor['resources'][resource] += person['resources'][resource]
            person['resources'][resource] = 0
            if person['name'] not in notifications:
                notifications[person['name']] = []
            notifications[person['name']].append({
                'action': 'monopoly',
                'name': actor['name'],
                'resource': resource
            })


    actor['developments'].remove('monopoly')
    state['card_played'] = True
    return (200, actor['resources'][resource])


    


