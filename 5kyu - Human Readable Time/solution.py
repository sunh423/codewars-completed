#https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    SS = seconds % 60
    seconds = seconds - SS
    minutes = seconds / 60
    MM = minutes % 60
    minutes = minutes - MM
    HH = minutes / 60 
    SS = str(int(SS))
    MM = str(int(MM))
    HH = str(int(HH))
    if len(SS) == 1:
        SS = "0" + SS
    if len(MM) == 1:
        MM = "0" + MM
    if len(HH) == 1:
        HH = "0" + HH
    return f"{HH}:{MM}:{SS}"
