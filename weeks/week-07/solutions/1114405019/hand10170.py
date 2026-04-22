#!/usr/bin/env python3

import sys

for line in sys.stdin:
    S, D = map(int, line.split())
    room = S
    guests = D
    while guests > room:
        guests -= room
        room += 1
    print(room)