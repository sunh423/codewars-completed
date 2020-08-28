#https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(iterable):
    array_index = dict(enumerate([item for item in iterable]))
    if len(iterable) > 1:
        for k,v in array_index.items():
            print(k)
            if array_index.get(k) == array_index.get(k+1, array_index[0]):
                 array_index[k] = None
        return [v for k,v in array_index.items() if v is not None]
    elif iterable == "":
        return []
    else:
        return [iterable]
    
