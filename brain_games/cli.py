import prompt


def welcome_user():
    print('\n<< Welcome to the Brain Games! >>\n')
    name = prompt.string('What is your name my friend?\nMy name is ')
    return print(f"\nHello, {name}, let's start!")
