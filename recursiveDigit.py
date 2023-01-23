import random
""" 
summing digits for a random number
"""
def digitSum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + digitSum(num // 10)

num = random.randint(1, 10000000)
print(num, digitSum(num))

