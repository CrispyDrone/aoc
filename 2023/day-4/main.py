#!/usr/bin/env python

from sys import argv
import functools

#def parse_literal():

input_file=argv[1] if len(argv) > 1 else "input.txt"

def extract_numbers(input):

    index_colon = input.find(':')
    index_bar = input.find('|')

    numbers_one = input[index_colon + 1:index_bar].strip().split()
    numbers_two = input[index_bar + 1:].strip().split()

    return list(map(int, numbers_one)), list(map(int, numbers_two))

def count_matches(numbers):
    # number of matches in numbers[0] and numbers[1] -> 2^(#matches - 1)

    # I'm assuming that duplicates count

    winning_numbers = { x for x in numbers[0] }

    matches = 0

    for n in numbers[1]:
        if n in winning_numbers: matches+=1

    return matches

def calculate_points(numbers):

    matches = count_matches(numbers)

    return 0 if matches == 0 else pow(2, matches - 1)

def increment(iterable, start, length, increment):

    for i in range(start, start + length):
        if iterable.get(i):
            iterable[i]+=increment
        else:
            iterable[i]=increment

def part_one():

    sum = 0

    with open(input_file) as file:
    
        for line in file:
    
            numbers = extract_numbers(line)
            result = calculate_points(numbers)
    
            print(line)
            print(numbers)
            print(result)
    
            sum += result
    
        print(f"total is: {sum}")

# let's first just do it with a dictionary, and then you can use an array limited to max number of matches
def part_two():

    card_number = 1
    cards = {}

    with open(input_file) as file:

        for line in file:

            numbers = extract_numbers(line)
            matches = count_matches(numbers)

            print(line)
            print(matches)

            if cards.get(card_number): 
                cards[card_number]+=1
            else:
                cards[card_number]=1

            increment(cards, card_number + 1, matches, cards[card_number])
            print(cards)
            card_number+=1

        sum = functools.reduce(lambda x, y: x + y, cards.values())

        print(f"total number of scratch cards is: {sum}") # Answer: 9496801

def part_two_array():
    pass()

part_one()
part_two()
