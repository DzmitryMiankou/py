from random import randrange

def multiplicationNumber(txt, a, b):
    result = a * b  
    if int(txt) == result:
        print(f"+++++++++++++ :-) {a} * {b} = {result}")
        return genericRandomNum(1, 10)
    else:
        return print(f"------------- :-( {a} * {b} = {result}")

def inputDataNumber(a, b):
    txt = input(f"{a} * {b} = ")
    if txt.isdigit():
        return multiplicationNumber(txt, a, b)
    else:
        return print('Вы ввели не число')
      
def genericRandomNum(start, end):
    return inputDataNumber(randrange(start, end), randrange(start, end))

genericRandomNum(1, 10)