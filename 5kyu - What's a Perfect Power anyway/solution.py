#https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python
def isPP(n):
    solution = []
    for i in range(2,n):
        sq_i = i
        power = 1
        while sq_i < n:
            sq_i *= i
            power += 1
            if sq_i == n:
                return [i, power]
    else:
        return None
