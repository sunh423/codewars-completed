#https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
def stock_list(listOfArt, listOfCat):
    result = []
    return_result = ""
    nothing = True
    for c in listOfCat:
        count = 0
        for books in listOfArt:
            if c == books[0]:
                numeral = books.split(" ")
                count += int(numeral[1])
            if count != 0:
                nothing = False
        result.append(f'({c} : {count})')
        return_result = " - ".join(result)
    if nothing == True:
        return ''
    else:
        return return_result
