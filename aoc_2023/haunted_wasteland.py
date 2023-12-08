import argparse
from itertools import cycle
from math import lcm
from time import time
from typing import Dict, Tuple

DAY = 8

def parse_instructions(string: str) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    inst, data = string.split('\n\n')
    d = {c:(l[1:],r[:-1]) for c, (l,r) in ((_, pair.split(', ')) 
            for _, pair in (line.split(' = ') for line in data.splitlines()))}
    return inst, d

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        inst, d = parse_instructions(f.read())
    cur = 'AAA'
    for i, c in enumerate(cycle(inst)):
        if cur == 'ZZZ':
            return i
        cur = d[cur][0 if c == 'L' else 1]
    

def part_2(filepath: str) -> int:
    with open(filepath, "r") as f:
        inst, d = parse_instructions(f.read())
    curs = list(filter(lambda x:x[2] == 'A', d.keys()))
    cycle_len = [0] * len(curs)
    for i in range(len(curs)):
        for c in cycle(inst):
            if curs[i][2] == 'Z' and cycle_len[i] == 0:
                cycle_len[i] += 1
            elif curs[i][2] == 'Z':
                break
            elif cycle_len[i] != 0:
                cycle_len[i] += 1
            curs[i] = d[curs[i]][0 if c == 'L' else 1]
    return lcm(*cycle_len)
    

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
