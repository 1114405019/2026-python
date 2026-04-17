#!/usr/bin/env python3

import sys

def main():
    try:
        for line in sys.stdin:
            line = line.rstrip('\n')
            if not line:
                continue
            freq = {}
            for char in line:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            char_list = list(freq.items())
            char_list.sort(key=lambda x: (x[1], -ord(x[0])))
            for char, count in char_list:
                ascii_val = ord(char)
                print(f"{ascii_val} {count}")
    except EOFError:
        pass

if __name__ == "__main__":
    main()