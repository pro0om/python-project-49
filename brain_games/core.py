import prompt
from brain_games.const import MAX_ROUND


def run_game(get_question_and_answer, game_instruction):
    print('\n<< Welcome to the Brain Games! >>\n')
    name = prompt.string('What is your name my friend?\n'
                         'My name is ')
    print(f"\nHello, {name}, let's start!\n\n"
          f"{game_instruction}\n"
          f"If you wanna win, your answer should be right {MAX_ROUND} times\n")
    for _ in range(MAX_ROUND):
        question, answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer:  ')

        if user_answer.capitalize() == answer:
            print('Correct!\n\n')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{answer}'. "
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

    return
