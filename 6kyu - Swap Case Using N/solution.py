#https://www.codewars.com/kata/5f3afc40b24f090028233490/train/python
from itertools import cycle

def swap(s,n):
    iter = cycle("{0:b}".format(n))
    superlist = [[k,v] for [(k,v)] in list(map(list,(zip(char,next(iter)) if char.isalpha() else zip(char,"0") for char in s)))]
    for i in range(len(superlist)):
        if superlist[i][1] is "1":
            if superlist[i][0].isupper():
                superlist[i] = superlist[i][0].lower()
            else:
                superlist[i] = superlist[i][0].upper()
        else:
            superlist[i] = superlist[i][0]
    return ''.join(superlist)