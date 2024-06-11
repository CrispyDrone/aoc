#!/usr/bin/env python

# TODO: can use a trie data structure here!

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def str2number(str):
    match str:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"

def process(line):
    
    digit_first=""
    digit_last=""

    for i in range(len(line)):

        char = line[i]

        if str.isdigit(line[i]):
            digit_last=char
        else:
            for digit in digits:
                sub = line[i:]
                # ~~potentially problematic, we need to skip the length of digit in the loop, so convert to while loop?~~ -> No, we should not. See "twone" case! We don't want to skip over two and in doing so miss out on identifying one!
                if sub.find(digit) == 0:
                    digit_last=str2number(digit)
                    break

        if not digit_first:
            digit_first=digit_last
    
    return digit_first + digit_last

sum=0

with open('input.txt') as input:
    for line in input:
        result = process(line)
        sum+=int(result)

        print(line)
        print(result)
        print()

print(sum)

