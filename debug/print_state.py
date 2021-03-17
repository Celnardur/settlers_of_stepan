#!/usr/bin/env python3
import json


def print_board(state):
    return

state = {}
with open('default_state.json', 'r') as fs:
    text = fs.read()
    state = json.loads(text)

print(state['hexes'])

