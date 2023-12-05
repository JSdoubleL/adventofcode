import aoc_2023
import argparse
from importlib import import_module
from os.path import join, dirname, realpath
from pkgutil import iter_modules
from time import time

def input_file(day: int, test: bool) -> str:
    return join(dirname(realpath(__file__)), "aoc_2023", "inputs", f"day{day}", 
                "test.txt" if test else "input.txt")

def title(m_name: str) -> str:
    bar = ">" * ((30 - len(m_name)) // 2)
    full_title = f"{bar} {m_name.replace('_', ' ').title()} {bar}" 
    return full_title if len(m_name) % 2 == 0 else full_title + ">"

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', action='store_true', 
                    help="use test inputs instead of full inputs")
test = parser.parse_args().test

day_modules = [(title(m_info[1]), import_module(f"aoc_2023.{m_info[1]}")) 
               for m_info in iter_modules(aoc_2023.__path__)]
day_modules.sort(key=lambda x:x[1].DAY)

print("=" * 11, " AoC 2023 ", "=" * 11, sep="")
print(f" " * 8, "{:<10s}|{:>10s}".format("ANSWER", "TIME"), sep="")
print("-" * 32, sep="")
for module_title, module in day_modules:
    print(module_title)
    t = time()
    print(f"Part 1: {module.part_1(input_file(module.DAY, test)):<10d}", 
            f"|{((time() - t) * 1000):10.2f} ms", sep="")
    t = time()
    print(f"Part 2: {module.part_2(input_file(module.DAY, test)):<10d}", 
            f"|{((time() - t) * 1000):10.2f} ms", sep="")
