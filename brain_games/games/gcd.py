from brain_games.const import GCD_INSTRUCTION
from brain_games.utility import get_random_num
from brain_games.core import run_game


def get_result_by_common_divisor(number1, number2):
    if number1 > number2:
        max_divisor = number2
        second_num = number1
    else:
        max_divisor = number1
        second_num = number2
    comparison_num = max_divisor
    while max_divisor > 0:
        if second_num % max_divisor == 0:
            answer = max_divisor
            if comparison_num % answer == 0:
                return answer
        max_divisor -= 1


def get_numbers_and_answer():
    number1, number2 = get_random_num(), get_random_num()
    numbers = f"{number1} {number2}"
    result = get_result_by_common_divisor(number1, number2)
    return numbers, str(result)


def run_gcd_game():
    run_game(get_numbers_and_answer, GCD_INSTRUCTION)
