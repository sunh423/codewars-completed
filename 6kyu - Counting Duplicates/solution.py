#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
def duplicate_count(text):
    set_accounted = set()
    d_text = dict(enumerate(text.lower()))
    dupe_count = 0
    for pt1 in d_text:
        for pt2 in range(pt1+1,len(text)):
            if d_text[pt1] == d_text[pt2] and d_text[pt1] not in set_accounted:
                dupe_count += 1
                set_accounted.add(d_text[pt1])
    return dupe_count
