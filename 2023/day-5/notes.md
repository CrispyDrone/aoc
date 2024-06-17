# Notes
## Part 1

+ I really need to write a parser class

## Part 2

+ The ranges seem quite large, I don't think I can just use the same algorithm as I did in part one.

  + ~~I think you can skip over all the values that belong to the same map (as they will only result in a higher value)~~ -> this is true only for a single mapping step. Then, the range can be distributed differently.

  + Well, for starters go through one range and then calculate the minimum. So don't go and calculate all values for all ranges, and only then determine the minimum (as you did in part 1).

  + I think you can operate with ranges instead of individual values. So, you have a range, then an "operation" is applied to it (the map) and the original range gets split up into potentially multiple ranges. In the very end, you just select the minimum of the various ranges we ended up with.

    + Should we do "depth first" (meaning do all mappings for one range before we move on to the next range) or "breadth first" (do a single mapping for all ranges, followed by the 2nd mapping,...)? Let's do the "breadth" first so we don't have to adjust the logic too much
