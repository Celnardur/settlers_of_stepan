import json
import os

state = {}
state_path = './state.json'

def set_state(path):
    global state
    with open(path, 'r') as fs:
        text = fs.read()
        state = json.loads(text)

def save_state(path):
    global state
    with open(path, 'w') as fs:
        fs.write(json.dumps(state))

def init():
    global state_path
    if os.path.exists(state_path):
        set_state(state_path)
    else:
        set_state('./defaults/default_state.json')
        save_state(state_path)

