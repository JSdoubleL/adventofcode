import argparse
from itertools import combinations
from time import time

DAY = 11

def part_1(filepath: str, exp_factor: int = 2) -> int:
    with open(filepath, "r") as f:
        universe = f.read().splitlines()
    empty_rows = [i for i, row in enumerate(universe) if len(set(row)) == 1]
    empty_columns = [i for i in range(len(universe[0])) 
                     if all(universe[j][i] != '#' for j in range(len(universe)))]
    galaxies = [(i, j) for i in range(len(universe)) 
                for j in range(len(universe[0])) if universe[i][j] == '#']
    result = 0
    for g1, g2 in combinations(galaxies, 2):
        rmin, rmax, cmin, cmax = min(g1[0],g2[0]), max(g1[0],g2[0]), min(g1[1],g2[1]), max(g1[1],g2[1])
        row_len = rmax - rmin + sum(exp_factor - 1 for i in empty_rows if rmin < i < rmax)
        column_len = cmax - cmin + sum(exp_factor - 1 for i in empty_columns if cmin < i <  cmax)
        result += row_len + column_len
    return result


def part_2(filepath: str) -> int:
    return part_1(filepath, 1000000)


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
