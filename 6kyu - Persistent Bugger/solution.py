#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
def persistence(n):
    count = 0
    while n > 9:
        n_array = [int(char) for char in str(n)]
        total = 1
        for i in n_array:
            total *= i
        count += 1
        n = total
    return count
