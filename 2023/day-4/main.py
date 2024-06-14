#!/usr/bin/env python

from sys import argv

#def parse_literal():

input_file=argv[1] if len(argv) > 1 else "input.txt"

def extract_numbers(input):

    index_colon = input.find(':')
    index_bar = input.find('|')

    numbers_one = input[index_colon + 1:index_bar].strip().split()
    numbers_two = input[index_bar + 1:].strip().split()

    return list(map(int, numbers_one)), list(map(int, numbers_two))

def calculate_points(numbers):

    # number of matches in numbers[0] and numbers[1] -> 2^(#matches - 1)

    # I'm assuming that duplicates count

    winning_numbers = { x for x in numbers[0] }

    matches = 0

    for n in numbers[1]:
        if n in winning_numbers: matches+=1

    return 0 if matches == 0 else pow(2, matches - 1)

sum = 0

with open(input_file) as file:

    for line in file:

        numbers = extract_numbers(line)
        result = calculate_points(numbers)

        print(line)
        print(numbers)
        print(result)

        sum+= result

    print(f"total is: {sum}")

