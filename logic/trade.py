from logic import player

def maritime_trade(state, name, give, get):
    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can trade")

    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    if order != state['turn'][1]:
        return (400, "Player cannot trade on this turn")

    acting = state['players'][order]
    if acting['taxes_due']:
        return (400, "Must pay taxes before you can trade")

    # check for negitive trade amounts
    for key, amt in give.items():
        if amt < 0:
            return (400, "Cannot trade negitive amounts")
    for key, amt in get.items():
        if amt < 0:
            return (400, "Cannot trade negitive amounts")

    # find trade ratios
    ratios = {'Brick': 4, 'Lumber': 4, 'Ore': 4, 'Grain': 4, 'Wool': 4}
    for settlement in acting['settlements']:
        harbor = state['settlements'][settlement]['harbor']
        if harbor == -1:
            continue
        harbor = state['harbors'][harbor]
        res = harbor['resource']
        if res == '?':
            for key in ratios:
                if ratios[key] > 3:
                    ratios[key] = 3
        else:
            ratios[res] = 2

    # check give amounts match ratios and calculate expected return
    expected = 0
    for res, amt in ratios.items():
        if res not in give:
            continue
        if give[res] % amt == 0:
            expected += give[res] / amt
        else:
            return (400, "Proposed trade resource amounts do not match ratios")

    if expected == 0:
        return (400, "You cannot trade nothing")
    
    # check requested amount matches 
    requested = sum(get.values())
    if requested != expected:
        return (400, "That trade is illegal")
    
    # execute trade
    code, message = player.take_resources(state, name, give)
    if code != 200:
        return (400, "Player cannot trade those resources")
    
    for res, amt in get.items():
        acting['resources'][res] += amt

    return (200, "Trade Executed")

def propose_trade(state, notifications, trade):
    return (400, "Not implemented")

def accept_trade(state, notifications, trade):
    return (400, "Not implemented")

def reject_trade(state, notifications, trade):
    return (400, "Not implemented")
