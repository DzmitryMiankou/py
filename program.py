from random import randrange

def multiplicationNumber(a, b):
    result = a * b
    txt = input(f"{a} * {b} = ")
    if txt.isdigit():
        if int(txt) == result:
            print(f":-) {a} * {b} = {result}")
            return genericRandomNum(1, 10)
        else:
            return print(f":-( {a} * {b} = {result}")
    else:
        return print('Вы ввели не число')


        
def genericRandomNum(start, end):
    return multiplicationNumber(randrange(start, end), randrange(start, end))

genericRandomNum(1, 10)
