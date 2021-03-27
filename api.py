import json
import os
from logic import player

state = {}
save_path = './state.json'
notifications = {}

def set_state(path):
    global state
    with open(path, 'r') as fs:
        text = fs.read()
        state = json.loads(text)

def save_state(path):
    global state
    with open(path, 'w') as fs:
        fs.write(json.dumps(state))

def init(path='./state.json'):
    global save_path
    save_path = path
    if os.path.exists(save_path):
        set_state(save_path)
    else:
        set_state('./defaults/default_state.json')
        save_state(save_path)

def process(path, args):
    global state
    global save_path
    global notifications

    (code, message, notify) = (404, "API endpoint does not exist", [])
    try: 
        if path == '/get_notifications':
            if not 'name' in args:
                return (400, "Cannot get notifications for nameless player")
            if not args['name'] in notifications:
                return (400, "Player has no notification queue")
            message = notifications[args['name']]
            notifications[args['name']] = []
            return (200, message)

        elif path == '/add_player':
            if not 'name' in args:
                return (400, "Player needs a name")
            if not 'color' in args:
                return (400, "Player needs a color")
            if not 'order' in args:
                return (400, "Player must provide a their position in the turn order")
            (code, message, notify) = player.add_player(state, args['name'], args['color'])
            if code == 200:
                notifications[args['name']] = []

        elif path == '/player_ready':
            if not 'name' in args:
                return (400, "Player needs a name")
            (code, message, notify) = player.player_ready(state, args['name'])

        elif path == '/remove_player':
            if not 'name' in args:
                return (400, "Player needs a name")
            (code, message, notify) = player.remove_player(state, args['name'])
            if code == 200:
                del notifications[args['name']]

        elif path == '/change_player_color':
            if not 'name' in args:
                return (400, "Player needs a name")
            if not 'color' in args:
                return (400, "Player needs a color")
            (code, message, notify) = player.change_player_color(state, args['name'], args['color'])

    except:
        return (500, "Internal server error")

    for name, action in notify:
        notifications[name].append(action)

    return (code, message)

    
