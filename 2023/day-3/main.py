#!/usr/bin/env python

from sys import argv
import re

p = re.compile(r"(\d+)")

input_file=argv[1] if len(argv) > 1 else "input.txt"

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

def part_one():

    sum=0

    with open(input_file) as input:
    
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

from collections import deque
import functools

def find_number_at_index(index, line):

    if index < 0 or index > len(line) - 1:
        return None, None

    if not line[index].isdigit(): return None, None

    start = index + 1
    end = index - 1

    while line[start - 1].isdigit(): start -= 1
    while line[end + 1].isdigit(): end += 1

    number = line[start:end + 1]
    # print(start, end, number)

    return end, int(number)

def find_surrounding_numbers(index, buffer):

    #print(f"finding numbers for {index}")

    # no current line yet
    if not len(buffer[1]): return []

    numbers = []

    # ugh, I hate this code!

    if len(buffer[0]):

        search = True
        search_index = index - 1

        while search:

            end, n = find_number_at_index(search_index, buffer[0])

            if n: 
                numbers.append(n)
                search_index = end + 2
            else:
                search_index += 1

            search = search_index <= index + 1

        #end, n = find_number_at_index(index - 1, buffer[0])

        #if n: 
        #    #print(f'{n} ending at {end}')
        #    numbers.append(n)

        #if not end or end < index:
        #    end, n = find_number_at_index(index + 1, buffer[0])
        #    if n: 
        #        #print(f'{n} ending at {end}')
        #        numbers.append(n)

    end, n = find_number_at_index(index - 1 , buffer[1])
    if n: 
        #print(f'{n} ending at {end}')
        numbers.append(n)

    end, n = find_number_at_index(index + 1 , buffer[1])

    if n: 
        #print(f'{n} ending at {end}')
        numbers.append(n)

    if len(buffer[2]):

        #end, n = find_number_at_index(index - 1, buffer[2])
        #if n: 
        #    #print(f'{n} ending at {end}')
        #    numbers.append(n)

        #if not end or end < index:
        #    end, n = find_number_at_index(index + 1, buffer[2])
        #    if n: 
        #        #print(f'{n} ending at {end}')
        #        numbers.append(n)
        search = True
        search_index = index - 1

        while search:

            end, n = find_number_at_index(search_index, buffer[2])

            if n: 
                numbers.append(n)
                search_index = end + 2
            else:
                search_index += 1

            search = search_index <= index + 1

    if len(numbers) == 2:
        product = numbers[0] * numbers[1]
        print(f"found {numbers} with product {product}")
        return numbers
    else:
        return []
    #return numbers if len(numbers) == 2 else []

def part_two():

    #queue = deque(["hello", "there", "general", "kenobi"])

    #while queue:
    #    value = queue.popleft()
    #    print(value)

    sum=0

    with open(input_file) as input:
    
        buffer=[],[],[]
        star_queue=[]
    
        # TODO: Rewrite this with a queue instead of this for loop? Also, how to use "next" on an iterator?
    
        for line in input:
    
            #print(line)
    
            buffer = buffer[1], buffer[2], line
    
            for s in star_queue:
                numbers = find_surrounding_numbers(s, buffer)
                if numbers: sum += functools.reduce(lambda x, y: int(x)*int(y), numbers)
    
            star_queue.clear()

            star_index = 0
    
            while True:
    
                star_index = line.find('*', star_index)

                if star_index < 0: 
                    break
    
                #print(f"found * at {star_index}")

                star_queue.append(star_index)

                star_index += 1
    
        buffer = buffer[1], buffer[2], []
    
        for s in star_queue:
            numbers = find_surrounding_numbers(s, buffer)
            if numbers: sum += functools.reduce(lambda x, y: x*y, numbers)
    
    print(sum)

# part_one()
part_two()

