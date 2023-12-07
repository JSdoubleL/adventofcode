import argparse
from collections import Counter
from time import time
from typing import Dict, Union

DAY = 7

def parse_hand_part_1(s: str) -> Dict[str, Union[int, str]]:
    hand, bid = s.split()    
    hand = hand.translate(str.maketrans({'A':'Z', 'K':'Y', 'Q':'X', 'J':'W', 'T':'V'}))
    c = Counter(hand)
    h_type = None
    # types: Five of a kind (6), Four of a kind (5), Full house (4), 
    #       Three of a kind (3), Two pair (2), One pair (1), High card (0)
    if max(c.values()) == 5:
        h_type = 6
    elif max(c.values()) == 4:
        h_type = 5
    elif max(c.values()) == 3:
        h_type = 4 if min(c.values()) == 2 else 3
    elif max(c.values()) == 2:
        h_type = 2 if len(c.values()) == 3 else 1
    else:
        h_type = 0
    return {"hand": hand, "bid": bid, "type": h_type}

def parse_hand_part_2(s: str) -> Dict[str, Union[int, str]]:
    hand, bid = s.split()    
    hand = hand.translate(str.maketrans({'A':'Z', 'K':'Y', 'Q':'X', 'J':'1', 'T':'V'}))
    c = Counter(hand)
    wild = c['1']
    c.pop('1', None)
    h_type = None
    try:
        if max(c.values()) + wild == 5:
            h_type = 6
        elif max(c.values()) + wild == 4:
            h_type = 5
        elif max(c.values()) + wild == 3:
            h_type = 4 if min(c.values()) == 2 else 3
        elif max(c.values()) + wild == 2:
            h_type = 2 if len(c.values()) == 3 else 1
        else:
            h_type = 0
    except:
        h_type = 6
    return {"hand": hand, "bid": bid, "type": h_type}

def part_1(filepath: str) -> int:
    with open(filepath, "r") as f:
        hands = [parse_hand_part_1(line) for line in f]
    hands.sort(key=lambda x:(x["type"], x["hand"]))
    return sum(i * int(h["bid"]) for i, h in enumerate(hands, 1))

def part_2(filepath: str) -> int:
    with open(filepath, "r") as f:
        hands = [parse_hand_part_2(line) for line in f]
    hands.sort(key=lambda x:(x["type"], x["hand"]))
    return sum(i * int(h["bid"]) for i, h in enumerate(hands, 1))

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
