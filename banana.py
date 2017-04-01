#!/usr/bin/env python3
import sys

def resolve(id, name):
    with open("hosts") as f:
        print(f.readlines())

print("INIT 1 0")
run = 1

while run:
    command, query = sys.stdin.readline().split(maxsplit=1)
    sys.stdout.write(query)
    if (command == "RESOLVE"):
        resolve(*query.split())
    elif (command == "CANCEL"):
        pass
