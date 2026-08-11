import random


def dice_roll(min :int=1, max :int=20):
    """
    return a random integer within the given range.

    :min (int): minimum value
    :max (int): maximum value
    :return (int): random value
    """
    return random.randint(min, max)


def game_dice_roll(
        min :int=1, 
        max :int=1, 
        critical_roll :bool=True,
        difficulty_value :int=True,
        inverse :bool=False
    ):
    """
    give a random integer within given range and according to given rule set

    :min (int): minimum value
    :max (int): maximum value
    :critical_roll (bool): does the roll have critical value ?
    :difficulty_value (int): value to complete test 
    :return (int): random value
    :return (bool): is the test succed ?
    :return (bool): is value critical ?
    """
    result :int = random.randint(min, max)

    if not inverse:
        if result == min and critical_roll:
            return result, False, True
        elif result == max and critical_roll:
            return result, True, True
        elif result >= difficulty_value:
            return result, True, False
        else:
            return result, False, False
    else:
        if result == min and critical_roll:
            return result, True, True
        elif result == max and critical_roll:
            return result, False, True
        elif result > difficulty_value:
            return result, True, False
        else:
            return result, False, False


############################################################################################
# test
############################################################################################
# print(dice_roll(2, 6))
