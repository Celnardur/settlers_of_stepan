#!/usr/bin/env python3

def output_digit(n, ns):
    if n < 10:
        return ns + " "
    else:
        return ns

def parse_token(t):
    i = t[0]
    if i == 'n':
        return "\n"
    elif len(t) < 2:
        return t
    ns = t[1:]
    
    if not ns.isdigit():
        return t
    
    n = int(ns)
    
    if i == 'p':
        output = ""
        for i in range(n):
            output += " "
        return output
    elif i == 's':
        return output_digit(n, ns)
    elif i == 'r':
        return output_digit(n, ns)
    elif i == 't':
        return 'TTTT'
    elif i == '/':
        return '/'
    elif i == '\\':
        return '\\'
    elif i == '|':
        return '|'
    else:
        return t

    return ""


in_str = ""
with open("fmt_output.txt", "r") as fs:
    in_str = fs.read()

tokens = in_str.split()
output = ""
for t in tokens:
    output += parse_token(t)

print(output)







