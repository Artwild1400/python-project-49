import random

DESCRIPTION = "What is the result of the expression?"

OPERATIONS = ['+', '-', '*']

def generate_round():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    operation = random.choice(OPERATIONS)

    question = f"{number1} {operation} {number2}"
    correct_answer = str(eval(question))

    return question, correct_answer
