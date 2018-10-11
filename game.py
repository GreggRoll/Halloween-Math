import random
import operator

ops = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv
        }
num1 = random.randint(0,12)
num2 = random.randint(1,10)
op = random.choice(list(ops.keys()))

def randomCalc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
    num1 = random.randint(0,12)
    num2 = random.randint(1,10)
    op = random.choice(list(ops.keys()))
    return num1, op, num2

def questionText():
    pass

def askQuestion():
    answer = randomCalc()
    return answer

def getInput():
    guess = float(input())
    return guess

def quiz():
    print('Welcome. This is a 10 question math quiz\n')
    score = 0
    for i in range(10):
        correct = askQuestion()
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!\n')
    return f'Your score was {score}/10'

