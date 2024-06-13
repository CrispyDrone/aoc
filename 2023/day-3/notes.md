# Notes
## Part 1

+ I'm assuming the input could potentially be __very__ large, which is why I
  have this incremental algorithm that keeps a buffer of 3 lines only.

+ Oof. I should write tests (even work test-driven tbh) so I can verify edge
  cases. I had off-by-one errors 2 times during the first part of the
assignment:

  + It didn't detect `262/....` as being adjacent to `/` because it was
    checking the character to the right of `/` instead (I'm only checking the
character immediately to the left and right of a number). This only happened if
the number was at the start of a line.

  + It thought `...370` had a character on the right even though it doesn't.
    Apparently, it was the newline character `\n`...

### Possible improvements

+ Rewrite the loop using a queue?
+ Use a divide and conquer algorithm?
  + I don't know how to read from a certain position in the file so I can split
    the input appropriately

## Part 2

+ Oof. Again, a small error in my logic, which might have been caught by tests.
  I don't like how the exercise gives very little explanation. There's a lot of
assumptions being made about the input. I guess it won't contain an asterisk
that's touching 3 numbers? So, this is not allowed for example:

  ```
  .119*..
  ....*93
  ....493
  
  ```

