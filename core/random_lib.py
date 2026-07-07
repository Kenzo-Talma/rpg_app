import random


def dice_roll(min=1, max=20):
    """
    return a random integer within the given range.

    :min (int): minimum value
    :max (int): maximum value
    :return (int): random value
    """
    return random.randint(min, max)

############################################################################################
# test
############################################################################################
# print(dice_roll(2, 6))
