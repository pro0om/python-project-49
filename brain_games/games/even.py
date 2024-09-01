from brain_games.const import EVEN_INSTRUCTION
from brain_games.utility import get_random_num
from brain_games.core import run_game


def is_even(num):
    return num % 2 == 0


def get_check_number_and_answer():
    check_number = get_random_num()
    answer = 'Yes' if is_even(check_number) else 'No'
    return check_number, answer


def run_even_game():
    run_game(get_check_number_and_answer, EVEN_INSTRUCTION)
