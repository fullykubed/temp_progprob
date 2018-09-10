from itertools import chain

INNER_SPACER = " " #character to be printed on the interior of the diamond
OUTER_SPACER = " " #character to be printed on the exterior of the diamond
START_CHAR = "A" #the beginning alphabetic character

#utiltiy for creating an arbitrary iterable of alpha characters
def character_range(c1,c2, step=1):
    for c in range(ord(c1), ord(c2), step):
        yield chr(c)

#prints a level of the diamond with the indicidated char
# - maxDiamondWidth is the number of characters in the largest level
# - levels start at 0 and end at (maxDiamondWidth - 1)
def printWithSpacers(char, level, maxDiamondWidth):

    numOuterSpacers = (maxDiamondWidth - 1) // 2

    if char == START_CHAR:
        outer = numOuterSpacers * OUTER_SPACER
        print(outer + char + outer)

    else:
        numOuterSpacers = abs(numOuterSpacers - level)
        outer = numOuterSpacers * OUTER_SPACER

        numInnerSpacers = maxDiamondWidth - (2 * (numOuterSpacers + 1))
        inner = numInnerSpacers * INNER_SPACER

        print(outer + char + inner + char + outer)

def printDiamond(endChar):

    #input checking / cleaning
    if not endChar.isalpha():
        raise ValueError("Ending character must be an alphabetic character")
    endChar = endChar.upper()

    #construct iterable of characters starting at START_CHAR going up to endChar and then back down tot START_CHAR
    diamond_chars = chain(character_range(START_CHAR, endChar), character_range(endChar, START_CHAR, -1), START_CHAR)

    #calculate the maximum line length
    maxLineLength = (ord(endChar) - ord(START_CHAR)) * 2 + 1

    #main driver of the algo
    for level, char in enumerate(diamond_chars):
        printWithSpacers(char, level, maxLineLength)
