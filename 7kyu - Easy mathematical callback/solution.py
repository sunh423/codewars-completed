#https://www.codewars.com/kata/54b7c8d2cd7f51a839000ebf/train/python
def process_array(arr, callback):
    return [callback(a) for a in arr]