#!/usr/bin/env python3

"""Play fizzbuzz between two integers

fizzbuzz 2 7
2
fizz
4
buzz
fizz
7
"""

import sys

def do_fizzbuzz(n):
    """Perform one round of fizz buzz

    >>> do_fizzbuzz(1)
    '1'
    >>> do_fizzbuzz(3)
    'fizz'
    >>> do_fizzbuzz(5)
    'buzz'
    >>> do_fizzbuzz(15)
    'fizz buzz'
    """

    output = []
    flag1 = n%3
    flag2 = n%5
    if not flag1:
        output += ['fizz']
    if not flag2:
        output += ['buzz']
    elif flag1:
        output = [str(n)]
    return " ".join(output)

if __name__ == "__main__":
    for _ in range(int(sys.argv[1]), int(sys.argv[2])+1):
        print(do_fizzbuzz(_))

