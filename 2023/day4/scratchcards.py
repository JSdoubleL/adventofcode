import argparse
from time import time

def score_card(game: str) -> int:
    winning, yours = [side.split()
                      for side in game.strip().split(': ')[1].split(' | ')]
    return int(2 ** (sum(1 for n in yours if n in winning) - 1))

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        return sum(score_card(line) for line in f)

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
