# Notes
## Part one
## Part two

+ I guess we can assume that the cards are sorted? So we don't have to go and look for card 2 in the input, it's going to be the card following card 1?

+ Assuming a very large input, we can't just maintain a single dictionary. We could use an array and have a running total. The array's length would have to be at least equal to the maximum number of winning numbers on a single card, so equal to the maximum number of numbers on a card. Is this constant per card? If not, the array would have to grow when required. And we'd have to maintain a "cursor" for the current card, and then use modular arithmetic to use the entire length of the array (behind the cursor)

+ iterating over a dictionary returns just the keys (when using `functools.reduce`)? I had to use `.values()`
