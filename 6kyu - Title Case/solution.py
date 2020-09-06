#https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python
def title_case(title, minor_words=''):
    new_string = ' '.join([word.title() if word not in minor_words.lower().split() else word for word in title.lower().split()])
    return new_string[:1].upper() + new_string[1:]
