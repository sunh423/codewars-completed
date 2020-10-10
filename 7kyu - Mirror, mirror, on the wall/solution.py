#https://www.codewars.com/kata/5f55ecd770692e001484af7d/train/python
def mirror(data: list) -> list:
    return [v for k,v in enumerate(sorted(data)) if k != len(data)-1] + sorted(data, reverse=True) if len(data) > 0 else []