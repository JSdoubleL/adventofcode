import argparse
from time import time

DAY = -1

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        raise NotImplementedError("part_1 has not been implemented")

def part_2(filepath: str) -> int:
    with open(filepath, "r") as f:
        raise NotImplementedError("part_2 has not been implemented")

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
