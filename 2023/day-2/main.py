#!/usr/bin/env python

import functools

colors={ 'red': 12, 'green': 13, 'blue': 14 }

def parse_draws(line):

    # TODO: could use a regex here? /s\(game\)\s\(\d\+\):\(.*\)/
    colon_index = line.find(':')
    game_id=line[5:colon_index]
    #print(game_id, line, end='')

    draws=list(map(str.strip, line[colon_index+1:].split(';')))

    all_draws=[]

    for draw in draws:
        # TODO: again use a regex
        balls=list(map(str.strip, draw.split(',')))
        
        for ball in balls:
            kvp = ball.split(' ', 1)
            number=int(kvp[0])
            color=kvp[1]

            all_draws.append((color, number))

    return (game_id, all_draws)

#def process(line):
#    
#    # TODO: could use a regex here? /s\(game\)\s\(\d\+\):\(.*\)/
#    colon_index = line.find(':')
#    game_id=line[5:colon_index]
#    print(game_id, line, end='')
#
#    draws=list(map(str.strip, line[colon_index+1:].split(';')))
#
#    for draw in draws:
#        # TODO: again use a regex
#        balls=list(map(str.strip, draw.split(',')))
#        
#        for ball in balls:
#            kvp = ball.split(' ', 1)
#            number=int(kvp[0])
#            color=kvp[1]
#
#            #print(f'{number} {color} balls')
#
#            if number > colors[color]:
#                print(f'{number} {color} balls exceeds {colors[color]}!')
#                return
#        
#
#    #print(draws)
#
#    return game_id
#
#
#def calculate_power(line):
#    
#    # TODO: could use a regex here? /s\(game\)\s\(\d\+\):\(.*\)/
#    colon_index = line.find(':')
#    game_id=line[5:colon_index]
#    print(game_id, line, end='')
#
#    draws=list(map(str.strip, line[colon_index+1:].split(';')))
#
#    maxes={"red": 0, "green": 0, "blue": 0}
#
#    for draw in draws:
#        # TODO: again use a regex
#        balls=list(map(str.strip, draw.split(',')))
#        
#        for ball in balls:
#            kvp = ball.split(' ', 1)
#            number=int(kvp[0])
#            color=kvp[1]
#
#            #print(f'{number} {color} balls')
#
#            if number > maxes[color]:
#                #print(f'{number} {color} balls exceeds {colors[color]}!')
#                maxes[color] = number
#
#    print(maxes)
#
#    return functools.reduce(lambda x, y: x*y, maxes.values())

sum=0
total_power=0

with open("input.txt") as file:
    for line in file:
        #result = process(line)
        #sum += int(result) if result else 0

        #power=calculate_power(line)
        #total_power += power

        game_id, draws = parse_draws(line)

        # assignment 1 -> cannot exceed max values; sum all valid game ids
        # assignment 2 -> minimum required balls; calculate "power" (product) and sum all powers

        maxes={"red": 0, "green": 0, "blue": 0}
        valid=True

        for draw in draws:

            color = draw[0]
            number = draw[1]

            if number > colors[color]:
                valid=False

            if number >= maxes[color]:
                maxes[color] = number

        if valid:
            sum += int(game_id)

        total_power += functools.reduce(lambda x, y: x*y, maxes.values())

print(f'sum: {sum}')
print(f'power: {total_power}')
