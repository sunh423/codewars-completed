def likes(names):
    like_string = ""
    if len(names) == 0:
        like_string = 'no one likes this'
    elif len(names) == 1:
        like_string = f'{names[0]} likes this'
    elif len(names) == 2:
        like_string = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        like_string = f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) >= 4:
        like_string = f'{names[0]}, ' + f'{names[1]} and ' + str(len(names) - 2) + ' others like this'
    return like_string
