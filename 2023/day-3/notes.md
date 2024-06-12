# Notes

+ Oof. I should write tests (even work test-driven tbh) so I can verify edge
  cases. I had off-by-one errors 2 times during the first part of the
assignment:

  + It didn't detect `262/....` as being adjacent to `/` because it was
    checking the character to the right of `/` instead (I'm only checking the
character immediately to the left and right of a number). This only happened if
the number was at the start of a line.

  + It thought `...370` had a character on the right even though it doesn't.
    Apparently, it was the newline character `\n`...

