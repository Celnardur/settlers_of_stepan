import json
import os
import random
from logic import player
from logic import build
from logic import resources
from logic import trade
from logic import development
from output import led_strip
from output import gpio
from output import seven_segment

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
    random.seed()

def process(path, args):
    global state
    global save_path
    global notifications

    (code, message) = (404, "API endpoint does not exist")

    if path == '/get_notifications':
        if not 'name' in args:
            return (400, "Cannot get notifications for nameless player")
        if not args['name'] in notifications:
            return (200, [])
        message = notifications[args['name']]
        notifications[args['name']] = []
        return (200, message)
    
    elif path == '/get_state':
        (code, message) = (200, state)

    elif path == '/get_player':
        if not 'name' in args:
            return (400, "Player needs a name")
        actor = player.find_player(state, args['name'])
        if actor == -1:
            (code, message) = (400, "That player does not exist")
        else:
            (code, message) = (200, state['players'][actor])

    elif path == '/new_game':
        set_state('./defaults/default_state.json')
        random.shuffle(state['developments'])
        save_state(save_path)
        return (200, "New game created")
    
    elif path == '/add_player':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'color' in args:
            return (400, "Player needs a color")
        if not 'order' in args:
            return (400, "Player must provide a their position in the turn order")
        (code, message) = player.add_player(state, args['name'], args['color'], args['order'])
        save_state(save_path)

    elif path == '/player_ready':
        if not 'name' in args:
            return (400, "Player needs a name")
        (code, message) = player.player_ready(state, args['name'])

    elif path == '/remove_player':
        if not 'name' in args:
            return (400, "Player needs a name")
        (code, message) = player.remove_player(state, args['name'])
        save_state(save_path)

    elif path == '/change_player_color':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'color' in args:
            return (400, "Player needs a color")
        (code, message) = player.change_player_color(state, args['name'], args['color'])
        save_state(save_path)

    elif path == '/randomize_players':
        (code, message) = player.randomize_players(state)
        save_state(save_path)

    elif path == '/build_settlement':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'pos' in args:
            return (400, "Need a position for the settlement")
        (code, message) = build.build_settlement(state, args['name'], args['pos'])
        save_state(save_path)

    elif path == '/build_road':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'pos' in args:
            return (400, "Need a position for the road")
        (code, message) = build.build_road(state, args['name'], args['pos'])
        save_state(save_path)

    elif path == '/build_city':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'pos' in args:
            return (400, "Need a position for the road")
        (code, message) = build.build_city(state, args['name'], args['pos'])
        save_state(save_path)

    elif path == '/draw_dev':
        if not 'name' in args:
            return (400, "Player needs a name")
        (code, message) = build.draw_dev(state, args['name'])
        save_state(save_path)

    elif path == '/end_turn':
        if not 'name' in args:
            return (400, "Player needs a name")
        (code, message) = resources.end_turn(state, notifications, args['name'])
        save_state(save_path)

    elif path == '/move_robber':
        if not 'mover' in args:
            return (400, "Player who move robber must be given")
        if not 'to' in args:
            return (400, "Pos to move robber to must be given")
        if not 'victim' in args:
            args['victim'] = None

        mover = args['mover']
        to = args['to']
        victim = args['victim']
        (code, message) = resources.move_robber(state, notifications, mover, to, victim)
        save_state(save_path)

    elif path == '/pay_taxes':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'taxes' in args:
            return (400, "Player needs a name")
        (code, message) = resources.pay_taxes(state, args['name'], args['taxes'])
        save_state(save_path)

    elif path == '/maritime_trade':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'give' in args:
            return (400, "Need resources to trade")
        if not 'get' in args:
            return (400, "Need resources to trade")
        (code, message) = trade.maritime_trade(state, args['name'], args['give'], args['get'])
        save_state(save_path)

    elif path == '/propose_trade':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'trade' in args:
            return (400, "Must propose a trade")
        (code, message) = trade.propose_trade(state, notifications, args['name'], args['trade'])
        save_state(save_path)

    elif path == '/accept_trade':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'trade' in args:
            return (400, "Must propose a trade")
        (code, message) = trade.accept_trade(state, notifications, args['name'], args['trade'])
        save_state(save_path)

    elif path == '/reject_trade':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'trade' in args:
            return (400, "Must propose a trade")
        (code, message) = trade.reject_trade(state, notifications, args['name'], args['trade'])
        save_state(save_path)

    elif path == '/play_knight':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'to' in args:
            return (400, "Need a position to move robber to")
        if not 'victim' in args:
            return (400, "Need a victim to steal resource from")
        name = args['name']
        to = args['to']
        victim = args['victim']
        (code, message) = development.play_knight(state, notifications, name, to, victim)
        save_state(save_path)

    elif path == '/play_build_road':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'one' in args or not 'two' in args:
            return (400, "Need two positions to build roads")
        (code, message) = development.play_build_road(state, args['name'], args['one'], args['two'])
        save_state(save_path)

    elif path == '/play_year_of_plenty':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'one' in args or not 'two' in args:
            return (400, "Need two resources for year of plenty")
        name = args['name']
        one = args['one']
        two = args['two']
        (code, message) = development.play_year_of_plenty(state, name, one, two)
        save_state(save_path)

    elif path == '/play_monopoly':
        if not 'name' in args:
            return (400, "Player needs a name")
        if not 'resource' in args:
            return (400, "Need a resources to have a monopoly")
        name = args['name']
        resource = args['resource']
        (code, message) = development.play_monopoly(state, notifications, name, resource)
        save_state(save_path)

    elif path == '/test_led_strip':
        led_strip.test()
        (code, message) = (200, "Testing led strip")

    elif path == '/set_led_strip':
        led_strip.set(state)
        (code, message) = (200, "Setting led strip")

    elif path == '/test_gpio':
        if not 'address' in args:
            return (400, "Need an i2c address to test gpio")
        (code, message) = gpio.test(args['address'])

    elif path == '/test_7seg':
        if not 'address' in args:
            return (400, "Need an i2c address to test gpio")
        seven_segment.test(args['address'])
        (code, message) = (200, "Testing 7seg")

    return (code, message)

# only gets called if process returns 200 code
def get_notifications(path, args):
    global state
    global notifications

    notify = []
    if path == '/add_player':
        notify = player.add_player_notifications(state, args['name'], args['order'])

    elif path == '/player_ready':
        notify = player.player_ready_notifications(state, args['name'])

    elif path == '/remove_player':
        if not 'name' in args:
            return (400, "Player needs a name")
        notify = player.remove_player_notifications(state, args['name'])

    # handle vp logic here

    for name, action in notify:
        if not name in notifications:
            notifications[name] = []
        notifications[name].append(action)

