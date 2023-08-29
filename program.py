from random import randrange

def multiplicationNumber(a, b):
    result = a * b
    txt = input(f"{a} * {b} = ")
    if int(txt) == result:
        print(f"Ok. :-) {a} * {b} = {result}")
        return genericRandomNum(1, 9)
    else:
        return print(f"No. :-( {a} * {b} = {result}")
        


def genericRandomNum(start, end):
    return multiplicationNumber(randrange(start, end), randrange(start, end))


genericRandomNum(1, 9)
