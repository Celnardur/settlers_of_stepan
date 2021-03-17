#!/usr/bin/env python3
import json
import pprint

def add_once(l, i):
    for a in l:
        if a == i:
            return
    l.append(i)

def left(n):
    if n <= 0:
        return 5
    else:
        return n - 1

def right(n):
    if n >= 5:
        return 0
    else:
        return n + 1

hexes = {}
with open('default_hexes.json', 'r') as fs:
    text = fs.read()
    hexes = json.loads(text)

roads = []
for i in range(72):
    roads.append({
        "settlements": [],
        "hexes": [],
        "owner": -1,
    })

settlements = []
for i in range(54):
    settlements.append({
        'roads': [],
        'hexes': [],
        'type': 'none',
        'owner': -1,
    })

for hex_id, tile in enumerate(hexes):
    for i, road in enumerate(tile['roads']):
        add_once(roads[road]['hexes'], hex_id)
        add_once(roads[road]['settlements'], tile['settlements'][i])
        add_once(roads[road]['settlements'], tile['settlements'][right(i)])

    for i, settlement in enumerate(tile['settlements']):
        add_once(settlements[settlement]['hexes'], hex_id)
        add_once(settlements[settlement]['roads'], tile['roads'][i])
        add_once(settlements[settlement]['roads'], tile['roads'][left(i)])

harbors = []
with open('harbors.json', 'r') as fs:
    text = fs.read()
    harbors = json.loads(text)

developments = []
with open('developments.json', 'r') as fs:
    text = fs.read()
    developments = json.loads(text)


state = {}
state['hexes'] = hexes
state['roads'] = roads
state['settlements'] = settlements
state['harbors'] = harbors
state['developments'] = developments
state['players'] = []
state['robber'] = 9
state['longest_road'] = -1
state['largest_army'] = -1
state['turn'] = 0

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(state)
print(json.dumps(state))


