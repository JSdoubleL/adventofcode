import argparse
from time import time
from typing import List

DAY = 9

def extrapolate_history(seq: str, back: bool = False) -> int:
    def diff_list(l: List[int]) -> List[int]:
        return [l[i +  1]  - l[i] for i in range(len(l) - 1)]
    
    vals = [list(map(int, seq.split()))]
    i, diff = 0, diff_list(vals[0])
    vals.append(diff)
    while len(set(diff)) != 1:        
        diff = diff_list(diff)
        vals.append(diff)
        i += 1    
    if back:
        cur = vals[-1][0]
        for i in range(len(vals) - 2, -1, -1):
            cur = vals[i][0] - cur
        return cur
    cur = vals[-1][-1]
    for i in range(len(vals) - 2, -1, -1):
        cur = cur + vals[i][-1]
    return cur


def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        return sum(extrapolate_history(line) for line in f)

def part_2(filepath: str) -> int:
    with open(filepath, "r") as f:
        return sum(extrapolate_history(line, True) for line in f)

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
