#!/usr/bin/env python3

import api
from print_state import get_state_string 
import pprint
import sys
import json

def scmd(args):
    script = []
    if args[0] == 'ap':
        script.append('new_game')
        script.append('add_player name "Aaron" color [255,0,0] order 0')
        script.append('add_player name "James" color [0,0,255] order 1')
        script.append('add_player name "Kyle" color [255,0,255] order 2')
        script.append('add_player name "Jack" color [0,255,0] order 3')
        script.append('print players')

    ret = ''
    for command in script:
        ret = process_command(command)

    return ret

def process_command(command):
    if command == "":
        return get_state_string(api.state)

    args = command.split()
    command = '/' + args[0]

    args_dict = {}
    arg_n = 1
    arg_len = len(args)
    while arg_n < arg_len - 1:
        arg = args[arg_n]
        value = json.loads(args[arg_n + 1])
        args_dict[arg] = value
        arg_n += 2

    if command == '/s':
        return scmd(args[1:])
    elif command == '/print':
        if len(args) < 2:
            return get_state_string(api.state)
        if not args[1] in api.state:
            return 'Cannot print ' + args[1]

        pp = pprint.PrettyPrinter(indent=4)
        return pp.pformat(api.state[args[1]])
    else:
        (code, message) = api.process(command, args_dict)
        if code == 200:
            api.get_notifications(command, args_dict)
            return str(code) + ': ' + str(message) + '\n' + get_state_string(api.state)
        else:
            return str(code) + ': ' + str(message) + '\n'


if __name__ == '__main__':
    save_path = './state.json'

    arg_n = 1
    arg_len = len(sys.argv)
    while arg_n < arg_len:
        arg = sys.argv[arg_n]
        if arg.startswith("-"):
            if arg == "--save_path" or arg == "-s":
                save_path = sys.argv[arg_n + 1]
                if not os.path.exists(save_path):
                    print("Specified save path does not exist")
                    exit(1)
            else:
                exit(1)
            arg_n += 1
        arg_n += 1

    api.init(save_path)
    while(1):
        print(">>", end="")
        command = input()
        if command == 'exit':
            exit(0)

        print(process_command(command))