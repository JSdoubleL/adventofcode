import argparse
from time import time

def score_card(card: str) -> int:
    winning, yours = [side.split()
                      for side in card.strip().split(': ')[1].split(' | ')]
    return sum(1 for n in yours if n in winning)

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        return sum(int(2 ** (score_card(line) - 1)) for line in f)

def part_2(filepath: str) -> int:
    with open(filepath, "r") as f:
        data = [line for line in f]
    card_counter = [1] * len(data)
    for i, card in enumerate(data):
        score = score_card(card)
        for j in range(1, score + 1):
            card_counter[i + j] += card_counter[i]
    return sum(card_counter)

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
