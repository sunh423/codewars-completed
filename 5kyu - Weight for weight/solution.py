# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python
def order_weight(strng):
    weight_list = []
    for weight in strng.split():
        modified_weight = 0
        for digit in weight:
            modified_weight += int(digit)
        weight_list.append([weight, modified_weight])
    return " ".join([k for k, v in sorted(weight_list, key=lambda x: (x[1], x))])
