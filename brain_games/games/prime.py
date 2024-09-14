from brain_games.const import PRIME_INSTRUCTION
from brain_games.utility import get_random_num
from brain_games.core import run_game


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            return False
    return True


def get_check_number_and_answer():
    check_number = get_random_num()
    answer = 'Yes' if is_prime(check_number) else 'No'
    return check_number, answer


def run_prime_game():
    run_game(get_check_number_and_answer, PRIME_INSTRUCTION)
