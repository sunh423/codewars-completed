#https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python
def number(lines):
    return [f"{str(k)}: {v}" for k,v in dict(zip([i for i in range(1,len(lines)+1)], lines)).items()]
