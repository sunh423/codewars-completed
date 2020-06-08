#https://www.codewars.com/kata/5b358a1e228d316283001892/train/python
def get_strings(city):
    char_counts = []
    city = city.lower()
    for char in city:
        repetition = ""
        counted_raw = ""
        if char.isalpha() and char not in char_counts:
            for i in range(city.count(char)):
                repetition += "*"
                counted_raw = f"{char}:{repetition}"
            if counted_raw not in char_counts:
                char_counts.append(counted_raw)
    return ",".join(char_counts)
