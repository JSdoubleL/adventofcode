import argparse
from time import time
from typing import List

def process_window(cur: str, m: List[bool]) -> int:
    numbers = []
    for i, c in enumerate(cur):
        if c.isdigit() and (i == 0 or not cur[i-1].isdigit()):
            numbers.append([i, None])
        if c.isdigit() and (i == len(cur) - 1 or not cur[i+1].isdigit()):
            numbers[-1][1] = i + 1
    return sum(int(cur[n[0]:n[1]]) for n in numbers 
               if any(m[max(0, n[0] - 1):min(n[1] + 1, len(cur))]))

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        engine = [line.strip() for line in f]
    result = 0
    n = len(engine[0])
    bool_mask = [[not c.isdigit() and c != '.' for c in line] for line in engine]
    for i, line in enumerate(engine):
        cur_mask = [any(b[j] for b in bool_mask[max(0, i-1):min(i+2, len(engine))]) 
                    for j in range(n)]
        result += process_window(line, cur_mask)
    return result

def part_2(filepath: str) -> int:
    with open(filepath, "r") as f:
        pass

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    input_file = parser.parse_args().input_file
    print(f" " * 8, "{:<10s}|{:>10s}".format("ANSWER", "TIME"), 
          "\n", "-" * 42, sep="")
    t = time()
    print(f"Part 1: {part_1(input_file):<10d}", 
          f"|{((time() - t) * 1000):10.2f} milliseconds", sep="")
    # t = time()
    # print(f"Part 2: {part_2(input_file):<10d}", 
    #       f"|{((time() - t) * 1000):10.2f} milliseconds", sep="")
