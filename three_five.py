"""
A program that prints thu numbers from 1 to 100

1. If number multiple of 3: Three
1. If number multiple of 5: Five
1. If number multiple of booth 3 and 5: ThreeFive
1. If any another result print the real number
"""

from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def multiple(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'ThreeFive'
    elif multiple_of_5(pos):
        say = 'Five'
    elif multiple_of_3(pos):
        say = 'Three'

    return say


if __name__ == '__main__':
    assert multiple(1) == '1'
    assert multiple(2) == '2'
    assert multiple(4) == '4'

    assert multiple(3) == '3'
    assert multiple(6) == '6'
    assert multiple(9) == '9'

    assert multiple(5) == '5'
    assert multiple(10) == '10'
    assert multiple(20) == '20'

    assert multiple(15) == '15'
    assert multiple(30) == '30'
    assert multiple(45) == '45'
