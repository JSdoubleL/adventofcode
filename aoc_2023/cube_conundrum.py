import argparse
from numpy import prod
from time import time
from typing import Dict

DAY = 2
REF_AMOUNT = {'red': 12, 'green': 13, 'blue': 14}

def parse_game(game: str) -> Dict[str, int]:
    _, description = game.split(':')
    games = [{c.strip().split(' ')[1]:int(c.strip().split(' ')[0]) for c in g.split(',')} 
             for g in description.split(';')]
    return games

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        result = 0
        for i, line in enumerate(f):
            games = parse_game(line)
            if all(REF_AMOUNT[c] >= g.get(c, 0) for g in games for c in REF_AMOUNT):
                result += i + 1
        return result

def part_2(filepath: str) -> int:
    with open(filepath, "r") as f:
        result = 0
        for line in f:
            games = parse_game(line)
            result += prod([max(g.get(c, 0) for g in games) for c in REF_AMOUNT])
        return result

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    input_file = parser.parse_args().input_file
    print(f" " * 8, "{:<10s}|{:>10s}".format("ANSWER", "TIME"), 
          "\n", "-" * 42, sep="")
    t = time()
    print(f"Part 1: {part_1(input_file):<10d}", 
          f"|{((time() - t) * 1000):10.2f} milliseconds", sep="")
    t = time()
    print(f"Part 2: {part_2(input_file):<10d}", 
          f"|{((time() - t) * 1000):10.2f} milliseconds", sep="")
