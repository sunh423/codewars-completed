#https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
def move_zeros(array):
    return sorted(
        list(
            map(lambda y: int(y) if isinstance(y, float) else y, array)
        ), key=lambda x: x is 0
    )
