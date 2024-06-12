#!/usr/bin/env python

import re

sum=0
p = re.compile(r"(\d+)")

def parse_next_number(index, line):
    # get index and number in the line, returns -1 if we can move on to the next line
    m = p.search(line, index)
    if m:
        return m.start(), m.group(0)

    else: return -1, None

def is_symbol(char):
    if char is None: return False
    return not (char.isdigit() or char == '.' or char == '\n')

def find_surrounding_symbol(number_tuple, buffer):

    # no current line yet
    if not len(buffer[1]): return False

    #print(f'checking {number_tuple[1]}')

    min_x = max(0, number_tuple[0] - 1)
    #print(number_tuple[0] + len(number_tuple[1]))
    #print(len(buffer[1]) - 1)
    max_x = min(number_tuple[0] + len(number_tuple[1]), len(buffer[1]) - 1)

    #print(f'{min_x} until {max_x}')
    #print(buffer[1][min_x: max_x])

    for i in range(min_x, max_x + 1):

        s_1 = buffer[0][i] if len(buffer[0]) else None
        s_2 = buffer[2][i] if len(buffer[2]) else None

        if is_symbol(s_1):
            #print(f"1: {number_tuple[1]} touching symbol {s_1}")
            return True

        if is_symbol(s_2):
            #print(f"2: {number_tuple[1]} touching symbol {s_2}")
            return True

    if is_symbol(buffer[1][min_x]):
        #print(f"3: {number_tuple[1]} touching symbol {buffer[1][min_x]}")
        return True

    if is_symbol(buffer[1][max_x]):
        #print(f"4: {number_tuple[1]} touching symbol {buffer[1][max_x]}")
        return True

    return False

with open("input.txt") as input:

    buffer=[],[],[]
    numbers_queue=[]

    # TODO: Rewrite this with a queue instead of this for loop? Also, how to use "next" on an iterator?

    for line in input:

        print(line)

        buffer = buffer[1], buffer[2], line

        for n in numbers_queue:
            if find_surrounding_symbol(n, buffer): 
                #print(f"adding {int(n[1])}")
                sum+= int(n[1])

        numbers_queue.clear()

        index = 0

        while True:

            #index, number = parse_next_number(index + (0 if number == None else len(number)), line)
            index, number = parse_next_number(index, line)

            if index < 0: 
                break

            #print(f"found number {number}")
            numbers_queue.append((index, number))
            index += len(number)

    buffer = buffer[1], buffer[2], []

    for n in numbers_queue:
        if find_surrounding_symbol(n, buffer): 
            #print(f"adding {int(n[1])}")
            sum+= int(n[1])

print(sum)
