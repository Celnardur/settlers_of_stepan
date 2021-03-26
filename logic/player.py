def add_player(state, name, color, order):
    for player in state['players']:
        if player != None and player['name'] == name:
            return (400, "Player already exists with that name.", [])
        if player != None and player['color'] == color:
            return (400, "Player already exists with that color.", [])

    if order > 4 or order < 0:
        return (400, "Can't have more than 4 players", [])
    if name == "":
        return (400, "Can't have an empty name", [])
    if len(color) != 3:
        return (400, "Color must have 3 values", [])
    for value in color:
        if value < 0 or value > 255:
            return (400, "RGB color values must be between 0 and 255", [])

    while len(state['players']) <= order):
        state['players'].append(None)

    if state['players'][order] != None
        return (400, "Player already in that spot in the turn order", [])

    state['players'][order] = {
        "roads": [],
        "settlements": [],
        "developments": [],
        "name": name,
        "color": color,
        "victory_points": 0,
    }

    notify = []
    for player in state['players']:
        if player != None and player['name'] != name:
            n = {}
            n['to'] = player['name']
            n['action'] = 'player_created'
            n['name'] = name
            notify.append(n)

    return (200, "Player added", notify)

def player_ready(state, name):
    if len(state['players']) < 3:
        return (400, "Not enough players to start game", [])

    notify = []
    for player in state['players']:
        if player == None:
            return (400, "Need all player slots to be filled to start the game", [])
        elif player['name'] != name:
            n = {}
            n['to'] = player['name']
            n['action'] = 'player_ready'
            n['name'] = name
            notify.append(n)

    return (200, "Ready notifications created", notify)

def find_player(state, name):
    for order, player in enumerate(state['players']):
        if player != None and player['name'] == name:
            return order
    return -1

def remove_player(state, name):
    for order, player in enumerate(state['players']):
        if player != None and player['name'] == name:
            if len(player['roads']) > 0 or len(player['settlements']) > 0:
                return (400, "Cannot remove player during game", [])
            if order == 3:
                state['players'].pop(3)
            else:
                state['players'][order] = None
            return (200, "Player removed", [])

    return (200, "Player already removed", [])

def change_player_color(state, name, color):
    order = find_player(state, name)
    if order == -1:
        return (400, "Player not found", [])
    if len(color) != 3:
        return (400, "Color must have 3 values", [])
    for value in color:
        if value < 0 or value > 255:
            return (400, "RGB color values must be between 0 and 255", [])
    
    state['players'][order]['color'] = color
    return (200, "Player Color changed", [])
    
    

