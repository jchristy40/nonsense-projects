import sys, random

print('a simple name generator for birds . . . \n')
print('quickly find the ideal name for your bird \n\n')

first = ('bird', 'birdie', 'birdman', 'birdissi', 'agamemnon', 'balmoral', 'battle axe', 'goblino', 'master', 'megalo', 'majestic', 'feather-dog', 'beak', 'talon', 'pidgey', 'issi', 'little')

last = ('battle axe', 'bigg boi', 'huge chest', 'the proud', 'intrepid chicken', 'the impertinent', 'man', 'birdey')

while True:
    firstname = random.choice(first)
    lastname = random.choice(last)

    print('\n')
    print('{} {}'.format(firstname,lastname), file=sys.stderr)
    print('\n')

    try_again = input('\npress enter to try again. type "n" to quit\n')
    if try_again.lower() == 'n':
        break

input('\npress Enter to exit')