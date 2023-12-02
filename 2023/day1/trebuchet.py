import argparse
from time import time

DIGITS = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 
          'eight':8, 'nine':9}

def part_1(filename: str) -> int:
    with open(filename, "r") as f:
        result = 0
        for line in f:
            first, last = None, None
            for c in line:
                if c.isdigit():
                    first = int(c)
                    break
            for c in reversed(line):
                if c.isdigit():
                    last = int(c)
                    break
            result += first * 10 + last
        return result
    
def part_2(filename: str) -> int:
    def process_digit(c: str, reverse: bool = False) -> int:
        if not reverse and c[-1].isdigit():
            return int(c[-1])
        elif reverse and c[0].isdigit():
            return int(c[0])
        for k, v in DIGITS.items():
            if k in c: 
                return v     
        return -1  

    with open(filename, "r") as f:
        result = 0
        for line in f:
            first, last = None, None
            for i in range(-4, len(line)):
                p = process_digit(line[max(i-5, 0):min(i+5, len(line))])
                if p >= 0:
                    first = p
                    break
            for i in range(len(line) + 4, 0, -1):
                p = process_digit(line[max(i-5, 0):min(i+5, len(line))], True)
                if p >= 0:
                    last = p
                    break
            result += first * 10 + last
        return result

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
