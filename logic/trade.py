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

def propose_trade(state, notifications, name, trade):
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

    if len(trade.keys()) > 2:
        return (400, "Can only have two parties to a trade")

    approver = ''
    for key in trade.keys():
        if key != acting['name']:
            approver = key

    order = player.find_player(state, approver)
    if order == -1:
        return (400, "You can't trade with a nonexistent player")

    item = {
        'approval_needed': approver,
        'trade': trade,
    }
    state['trades'].append(item)

    if approver not in notifications:
        notifications[approver] = []
    notifications[approver].append({
        'action': 'trade_request',
        'from': acting['name'],
        'to': approver,
        'trade': trade,
    })
    return (200, "Trade request sent, awaiting approval")

def accept_trade(state, notifications, name, trade):
    if state['move_robber'] != -1:
        return (400, "The robber must be moved before you can trade")
    
    order = player.find_player(state, name)
    if order == -1:
        return (400, "Player with that name does not exist")

    approver = state['players'][order]
    if approver['taxes_due']:
        return (400, "Must pay taxes before you can trade")

    proposer = ''
    for key in trade.keys():
        if key != approver['name']:
            proposer = state['players'][player.find_player(state, key)]

    # check that trade is actually proposed
    item = {
        'approval_needed': name,
        'trade': trade,
    }
    if item not in state['trades']:
        return (400, "Cannot accept that trade, It doesn't exist")
    
    # check to see if players have enough resources to make trade
    for trader, give in trade:
        order = player.find_player(trader)
        actor = state['players'][order]
        for res, amt in give.items():
            if res not in actor['resources']:
                return (400, res + " is not a valid resource")
            if actor['resources'][res] < amt:
                return (400, actor['name'] + " does not have enough resources")

    # take resources from each player
    for trader, give in trade:
        player.take_resources(state, trader, give)

    # give resources to each player
    for trader, give in trade:
        for res, amt in give.items():
            if trader != approver['name']:
                approver['resources'][res] += amt
            else:
                proposer['resources'][res] += amt

    # remove trade from list
    state['trades'].remove(item)

    # notify proposer of trade completion
    if proposer['name'] not in notifications:
        notifications[proposer['name']] = []
    notifications[proposer['name']].append({
        'action': 'trade_accept',
        'from': acting['name'],
        'to': approver,
        'trade': trade,
    })

    return (200, "Trade executed")

def reject_trade(state, notifications, name, trade):
    return (400, "Not implemented")

