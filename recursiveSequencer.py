import random
"""
 counting the number of elements that are 
 equal to the maximum element in the given sequence
 
 """
def max_count_recursive(num, max_num, max_count):
    if num == 0:
        print(num)
        return max_count
    if num > max_num:
        max_num = num
        print(max_num)
        max_count = 1
    elif num == max_num:
        max_count += 1
        print(num ,max_count)
    return max_count_recursive(random.randint(0, 20), max_num, max_count)

print(max_count_recursive(random.randint(0, 20), 0, 0))
