#https://www.codewars.com/kata/57e3f79c9cb119374600046b/train/python
def hello(name="World"):
    if not name:
        name = "World"
    return f"Hello, {name.title()}!"
