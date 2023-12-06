import argparse
from math import ceil, sqrt
from numpy import prod
from time import time
from typing import List, Tuple

DAY = 6

def parse_races(string: str) -> List[Tuple[int, int]]:
    return list(zip(*[map(int, line.split()[1:]) for line in string.splitlines()]))

def parse_races_2_electric_boogaloo(string: str) -> List[int]:
    return list(int("".join(line.split()[1:])) for line in string.splitlines())

def num_winning(time: int, dist: int) -> int:
    quadratic = sqrt(time ** 2 - 4 * dist)
    if quadratic % 1 == 0: # fuck this edge case in particular
        quadratic -= 1
    low, high = ceil((time - quadratic) / 2), ceil((time + quadratic) / 2)     
    return high - low
    #int((high * (high - 1) / 2) - (low * (low - 1) / 2)) # sadly didn't need this formula :(

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        races = parse_races(f.read())
    return prod([n for n in (num_winning(time, dist) for time, dist in races) if n != 0])

def part_2(filepath: str) -> int:
    with open(filepath, "r") as f:
        race = parse_races_2_electric_boogaloo(f.read())
    return num_winning(race[0], race[1])

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
