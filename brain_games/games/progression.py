from brain_games.const import PROGRESSION_INSTRUCTION, STRING_SIZE, STEP_SIZE
from brain_games.utility import get_random_num
from brain_games.core import run_game


def get_numbers_string(num):
    left_size = get_random_num(1, STRING_SIZE - 1)
    right_size = STRING_SIZE - 1 - left_size
    random_step = get_random_num(1,STEP_SIZE)
    right_list, left_list = [], []
    start_point1, start_point2 = num, num
    for _ in range(right_size):
        start_point1 += random_step
        right_list.append(start_point1)
    for _ in range(left_size):
        start_point2 -= random_step
        left_list.insert(0, start_point2)
    right_string = ' '.join(map(str, right_list))
    left_string = ' '.join(map(str, left_list))
    result = f'{left_string} .. {right_string}'
    return result


def get_numbers_and_answer():
    check_number = get_random_num()
    numbers_string = get_numbers_string(check_number)
    return numbers_string, str(check_number)


def run_progression_game():
    run_game(get_numbers_and_answer, PROGRESSION_INSTRUCTION)
