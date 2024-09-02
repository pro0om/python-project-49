import random
from brain_games.const import CALC_INSTRUCTION, MATH_OPERATIONS
from brain_games.utility import get_random_num
from brain_games.core import run_game


def get_result_by_math_symbol(number1, number2, math_symbol):
    if math_symbol == '+':
        return number1 + number2
    if math_symbol == '-':
        return number1 - number2
    if math_symbol == '*':
        return number1 * number2


def get_math_question_and_answer():
    number1, number2 = get_random_num(), get_random_num()
    math_symbol = random.choice(MATH_OPERATIONS)
    math_expression = f" {number1} {math_symbol} {number2}"
    result = get_result_by_math_symbol(number1, number2, math_symbol)
    return math_expression, str(result)


def run_calc_game():
    run_game(get_math_question_and_answer, CALC_INSTRUCTION)
