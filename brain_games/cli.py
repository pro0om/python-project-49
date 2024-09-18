import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\nMy name is ')
    return print(f"\nHello, {name}, let's start!")
