#https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python](https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python)
def namelist(names):
    new_list = [item['name'] for item in names]
    if len(new_list) == 1:
        return new_list[0]
    elif len(new_list) == 2:
        return f"{new_list[0]} & {new_list[1]}"
    elif len(new_list) > 2:
        r = len(new_list)
        return f"{', '.join([new_list[i] for i in range(r-2)])}, {new_list[r-2]} & {new_list[r-1]}"
    else:
        return ''