#https://www.codewars.com/kata/5f70c55c40b1c90032847588/train/python
from collections import Counter

def points(dice):
    count = Counter([num for num in dice])
    if 5 in count.values():
        return 50
    elif 4 in count.values():
        return 40
    elif 3 in count.values() and 2 in count.values():
        return 30
    elif len(count) == 5:
        if "3" not in count.keys() or "4" not in count.keys() or "5" not in count.keys():
            return 0
        else:
            return 20
    return 0