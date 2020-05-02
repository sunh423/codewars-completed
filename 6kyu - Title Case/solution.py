#https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python
def title_case(title, minor_words=''):
    current_index = 0
    if len(title) != 0:
        title[0].upper()
    title_list = title.split()
    title_list = [words.capitalize() for words in title_list]
    minor_words_list = minor_words.split()
    minor_words_list = [words.capitalize() for words in minor_words_list]
    for words_1 in title_list[1:]:
        current_index += 1
        for words in minor_words_list:
            if words_1 == words:
                title_list[current_index] = words_1.lower()
    title = " ".join(title_list)
    return title
    
