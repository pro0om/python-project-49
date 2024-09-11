from brain_games.const import GCD_INSTRUCTION
from brain_games.utility import get_random_num
from brain_games.core import run_game


def get_result_by_common_divisor(number1, number2):
    if number1 == number2:
        answer = abs(number1)
        return answer

    # divisors1 = []
    # divisors2 = []
    # for i in range(number1 + 1):
    #     if number1 % i == 0:
    #         divisors1 += [i]
    # for i in range(number2 + 1):
    #     if number2 % i == 0:
    #         divisors2 += [i]
    #
    # return divisors2


def get_numbers_and_answer():
    number1, number2 = get_random_num(), get_random_num()
    numbers = f" {number1} {number2}"
    result = get_result_by_common_divisor(number1, number2)
    return numbers, str(result)


def run_gcd_game():
    run_game(get_numbers_and_answer, GCD_INSTRUCTION)
