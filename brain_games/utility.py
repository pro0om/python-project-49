import random
from brain_games.const import MIN_NUMBER, MAX_NUMBER


def get_random_num(start=MIN_NUMBER, stop=MAX_NUMBER):
    return random.randint(start, stop)
