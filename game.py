import random
import operator

def randomCalc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,}
    num1 = random.randint(0,10)
    num2 = random.randint(1,10)
    op = random.choice(list(ops.keys()))
    nums = [num1, op, num2]
    return nums

def questionText(nums):
    return f"{nums[0]} {nums[1]} {nums[2]}"


def getAnswer(nums):
    if nums[1] == '+':
        answer = nums[0] + nums[2]
    if nums[1] == '-':
        answer = nums[0] - nums[2]
    if nums[1] == '*':
        answer = nums[0] * nums[2]
    return answer


