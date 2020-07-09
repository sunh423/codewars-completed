#https://www.codewars.com/kata/5848565e273af816fb000449/train/python
def encrypt_this(text):
    new_list = []
    encrypted = ""
    ascii_table = {chr(i): str(i) for i in range(65,91)}
    ascii_table.update({chr(i): str(i) for i in range(97,123)})
    text_list = text.split()
    for index_word in range(len(text_list)):
        pre_modified_word = list(text_list[index_word])
        post_modified_word = pre_modified_word.copy()
        if len(pre_modified_word) >= 1:
            k = post_modified_word[0]
            post_modified_word[0] = ascii_table[k]
        if len(pre_modified_word) >= 3:
            post_modified_word[1] = pre_modified_word[-1]
            post_modified_word[-1] = pre_modified_word[1]
        new_list.append("".join(post_modified_word))
    encrypted = " ".join(new_list)
    return encrypted
    pass
