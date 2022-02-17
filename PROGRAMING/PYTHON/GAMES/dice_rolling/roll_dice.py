import sys
from random import choice

DICE_WALLS = ['1','2','3','4','5','6']
DICE_ART = {
    '1': (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    '2': (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    '3': (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    '4': (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    '5': (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    '6': (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DICE_HEIGHT = len(DICE_ART['1'])
DICE_WIDTH = len(DICE_ART['1'][0])
DICE_FACE_SEPARATOR = "\n"

def get_input():
    if len(sys.argv) == 2 and sys.argv[-1].isdigit():
        return sys.argv[-1]
    return False

def roll_dice(dice):
    return choice(dice)

def make_a_dice(dice_number):
    return DICE_ART[dice_number]

def manage_dices(all_dices):
    final = list(zip(*all_dices))
    final = [' '.join(item) for item in final]
    return DICE_FACE_SEPARATOR.join(final)

def main():
    all_dices = []
    number_of_dice = get_input() # Getting number 6 sided dices to roll
    if  number_of_dice in DICE_WALLS:
        print(f'{("Rolling dices ["+number_of_dice+"]").center(25,"-")}')
        number_of_dice = int(number_of_dice)
        while number_of_dice:
            all_dices.append(make_a_dice(roll_dice(DICE_WALLS)))
            number_of_dice -= 1
        else:
            all_dices = manage_dices(all_dices)
            print(all_dices)
    else:
        print('Please enter a number of dices to roll')


if __name__ == '__main__':
    main()
