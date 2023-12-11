import argparse
import heapq
import numpy as np
from time import time
from itertools import product
from typing import List, Tuple

DAY = 10

def check_dir(i: int, j: int, p: List[str]) -> List[Tuple[int, int]]:
    up, left, right, down = (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)
    left_con, right_con, up_con, down_con = ['L', 'F', '-'], ['J', '7', '-'], \
        ['|', 'L', 'J'], ['|', '7', 'F']    
    if p[i][j] == 'S':
        mod = 1 if p[i+1][j] != 'x' else 2
        result = []
        if p[i][j-mod] in left_con:
            result.append(right)
        if p[i][j+mod] in right_con:
            result.append(left)
        if p[i+mod][j] in up_con:
            result.append(down)
        if p[i-mod][j] in down_con:
            result.append(up)
    else:
        result = (
            [up, down] if p[i][j] == '|' else
            [up, right] if p[i][j] == 'L' else
            [up, left] if p[i][j] == 'J' else
            [left, down] if p[i][j] == '7' else
            [right, down] if p[i][j] == 'F' else
            [left, right] if p[i][j] == '-' else
            []
        )
    return [(max(0, min(d[0], len(p) - 1)), max(0, min(d[1], len(p[0]) - 1))) for d in result]

def part_1(filepath: str) -> int:    
    with open(filepath, "r") as f:
        p = f.read().splitlines()
    si, sj = -1, -1
    for i, j in product(range(len(p)), range(len(p[0]))):
        if p[i][j] == 'S':
            si, sj = i, j
            break
    max_dist = 0
    h = [(0, (si, sj))]
    seen = [[False for _ in range(len(p[0]))] for _ in range(len(p))]
    #debug = [['.' for _ in range(len(p[0]))] for _ in range(len(p))]
    seen[si][sj] = True
    while len(h) != 0:
        d, (ui, uj) = heapq.heappop(h)
        results = check_dir(ui, uj, p)
        if len(results) != 0:
            for v in results:
                if not seen[v[0]][v[1]]:
                    seen[v[0]][v[1]] = True
                    heapq.heappush(h, (d + 1, v))
                    #debug[v[0]][v[1]] = str(d + 1)
                    if d + 1 > max_dist:
                        max_dist = d + 1
    #print("\n".join(["".join(row) for row in debug]))
    return max_dist

def lay_pipe(i: int, j: int, exp_p: List[List[str]]) -> None:
    up, down = (i - 1, j), (i + 1, j)
    if exp_p[up[0]][up[1]] == 'x' and exp_p[down[0]][down[1]] == 'x': # check up/down
        exp_p[i][j] = '-'
    else:
        exp_p[i][j] = '|'

def part_2(filepath: str) -> int:  
    exp_p = []
    with open(filepath, "r") as f:
        for line in f:
            exp_p.append(['x' if i % 2 == 0 else line[(i - 1) // 2] 
                          for i in range(2 * len(line) + 1)])
            exp_p.append(['x' for _ in range(2 * len(line) + 1)]) 
    exp_p.insert(0, ['x' for _ in range(len(exp_p[0]))])
    n, m = len(exp_p), len(exp_p[0])
    count_seen_og = 1
    si, sj = -1, -1 
    for i, j in product(range(n), range(m)):
        if exp_p[i][j] == 'S':
            si, sj = i, j
            break

    seen = [[False for _ in range(m)] for _ in range(n)]
    seen[si][sj] = True
    h = [(si, sj)]
    while len(h) != 0:
        ui, uj = h.pop()
        if exp_p[ui][uj] == 'x':
            lay_pipe(ui, uj, exp_p)
            assert exp_p[ui][uj] != 'x'
        nxt = check_dir(ui, uj, exp_p)
        if len(nxt) != 0:
            for vi, vj in nxt:
                if not seen[vi][vj]:
                    if exp_p[vi][vj] != 'x':
                        count_seen_og += 1
                    seen[vi][vj] = True
                    h.append((vi, vj))

    si, sj = 0, 0 
    h = [(si, sj)]
    while len(h) != 0:
        ui, uj = h.pop()
        nxt = [(i, j) for i, j in [(ui - 1, uj), (ui, uj - 1), (ui, uj + 1), (ui + 1, uj)] 
               if 0 <= i < n and 0 <= j < m]
        for vi, vj in nxt:
            if not seen[vi][vj]:
                seen[vi][vj] = True
                h.append((vi, vj))
                if not exp_p[vi][vj] == 'x':
                    count_seen_og += 1
    return (((n - 1) // 2) * ((m - 1) // 2))  - count_seen_og


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
