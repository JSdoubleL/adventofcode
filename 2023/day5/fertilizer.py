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

def apply_map_row(seed: int, row: List[int]) -> int:
    return seed + (row[0] - row[1]) \
        if seed >= row[1] and seed < (row[1] + row[2]) else -1

def map_seed(seed: int, almanac: List[List[List[int]]]) -> int:
    for section in almanac:
        new_seed = max(apply_map_row(seed, row) for row in section)
        if new_seed != -1:
            seed = new_seed
    return seed

def flatten_ranges(ranges: List[Tuple[int]]) -> List[Tuple[int]]:
    ranges.sort(key=lambda x:x[0])
    result, i = [], 0
    while i < len(ranges):
        if i != len(ranges) - 1 and sum(ranges[i]) >= ranges[i+1][0] + 1:
            result.append((ranges[i][0], sum(ranges[i+1]) - ranges[i][0]))
            i += 2
        else:
            result.append(ranges[i])
            i += 1
    return result

def apply_map_row_range(seed: Tuple[int], row: List[int]) -> List[Tuple[int]]:
    result = [None, []]
    s_start, s_end = seed[0], sum(seed)
    r_start, r_end, diff = row[1], row[1] + row[2], row[0] - row[1]
    if s_end < r_start or s_start >= r_end: # disjoint ranges
        return [None, [seed]]
    if s_start < r_start: # leading non-overlapping seed range
        result[1].append((s_start, r_start - s_start))
    if r_end < s_end: # trailing non-overlapping seed range
        result[1].append((r_end, s_end - r_end))
    result[0] = (max(s_start, r_start) + diff, 
                 min(r_end, s_end) - max(s_start, r_start))
    return result 

def map_seed_2_electric_boogaloo(seed: int, almanac: List[List[List[int]]]) -> int:
    def recursive_func(seed: Tuple[int], sec_n: int) -> Tuple[int]:
        if sec_n < len(almanac):
            mapped_ranges = []
            cur_seeds = [seed]
            for row in almanac[sec_n]:
                result = [apply_map_row_range(s, row) for s in cur_seeds]
                mapped_ranges.extend([r[0] for r in result if r[0] is not None])
                cur_seeds = [s for r in result for s in r[1]]
            mapped_ranges.extend([s for s in cur_seeds])
            return min(recursive_func(r, sec_n + 1) 
                       for r in flatten_ranges(mapped_ranges))
        return seed[0]
    return recursive_func(seed, 0)

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        file_content = f.read()
    seeds, almanac = parse_almanac(file_content)
    return min(map_seed(s, almanac) for s in seeds)

def part_2(filepath: str) -> int:
    with open(filepath, "r") as f:
        file_content = f.read()
    seeds, almanac = parse_almanac(file_content)
    return min(map_seed_2_electric_boogaloo((seeds[i], seeds[i+1]), almanac) 
               for i in range(0, len(seeds), 2))
               
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
