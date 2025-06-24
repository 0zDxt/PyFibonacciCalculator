# Script : Fibonacci

import argparse
import shutil

width = shutil.get_terminal_size().columns

parser = argparse.ArgumentParser(description="Process with an integer, enter the number Fibonacci terms you want to calculate.")

# Positional argument:
parser.add_argument('number', type=int, help="an integer as the length of the list")
 
args = parser.parse_args()

i = args.number

print("*" * width)
print(f"\n\t\t\tHere are the {i} first terms of the Fiboncci list\n")
print("*" * width)

if i <= 0:
    print("You should enter a positive integer.")
    exit(1)
else:
    a, b = 0, 1
    for i in range(i):
        print(a)
        a, b = b, a + b

print("WIP...")
