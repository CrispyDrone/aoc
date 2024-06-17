#!/usr/bin/env python

import re
from sys import argv

file_name = argv[1] if len(argv) > 1 else "input.txt"

p = re.compile(r"map\s*:")

def extract_seeds(input):
   
    index_colon = input.find(':')
    index_newline = input.find('\n', index_colon+1)

    if index_newline == -1:
        seeds = input[index_colon+1:]
    else:
        seeds = input[index_colon+1:index_newline]

    return list(map(int, seeds.strip().split()))

def extract_seed_ranges(input):
    
    seeds = extract_seeds(input)
    # TODO: return low and high instead of low and length
    return list(zip(seeds[::2], seeds[1::2]))
    
def parse_one_category(input):

    lines=[]
    parsing=False

    while not parsing:
        line = input.readline()
        if not line: break
        if line.isspace(): continue
        if is_new_category(line): parsing=True

    while parsing:
        pos = input.tell()
        line = input.readline()
        if not line: break
        if line.isspace(): continue
        if is_new_category(line): 
            input.seek(pos)
            parsing=False
        else: lines.append(line.strip())

    return [ list(map(int, x.split())) for x in lines ]

def is_new_category(input):

    return p.search(input) != None

def map_one_seed_value(value, mappings):

    mapped_value = value

    for mapping in mappings:

        #print(mapping)
        dest, source, length = mapping

        if value >= source and value < source + length:
            mapped_value = value - source + dest
            break

    return mapped_value

def interval_subtract(a, b):
    #TODO
    pass

def interval_union(a, b):
    #TODO
    pass

def map_one_seed_range(value_range, mappings):

    # I should create an interval type for this and then define a subtract and union operation...

    #TODO
    pass
    
def part_one(input):
        
        first_line = input.readline()
        seeds = extract_seeds(first_line)

        source = seeds
        target = []

        while True:

            maps = parse_one_category(input)

            if not maps: break

            for v in source:

                mapped_value = map_one_seed_value(v, maps)
                target.append(mapped_value)
            
            source = target
            target = []

        return min(source)

def part_two(input):
        
        first_line = input.readline()
        seeds = extract_seed_ranges(first_line)

        source = seeds
        target = []

        while True:

            maps = parse_one_category(input)

            if not maps: break

            for v in source:

                mapped_range = map_one_seed_range(v, maps)
                target.extend(mapped_range)
            
            source = target
            target = []

        return min([x[0] for x in source])

if __name__ == '__main__':
    with open(file_name) as file:
        location_min_value = part_one(file)
        print(f"part one: lowest location value {location_min_value}")

        location_min_value_two = part_two(file)
        print(f"part two: lowest location value {location_min_value_two}")

