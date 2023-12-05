import argparse
from time import time
from typing import List, Tuple

def parse_almanac(almanac_text: str) -> Tuple[List[int], List[List[List[int]]]]:
    almanac_text = almanac_text.strip().split('\n\n')
    seeds = [int(s) for s in almanac_text[0].split(': ')[1].split()]
    # almanac[section][row][dest|source|range]
    almanac = [[[int(val) for val in row.split()] 
                for row in section.split(':\n')[1].split('\n')] 
                for section in almanac_text[1:]]
    return seeds, almanac

def map_seed(seed: int, almanac: List[List[List[int]]]) -> int:
    def apply_map(seed, row):
        return seed + (row[0] - row[1]) \
            if seed >= row[1] and seed < (row[1] + row[2]) else -1
    for section in almanac:
        new_seed = max(apply_map(seed, row) for row in section)
        if new_seed != -1:
            seed = new_seed
    return seed

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        file_content = f.read()
    seeds, almanac = parse_almanac(file_content)
    return min(map_seed(s, almanac) for s in seeds)

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
