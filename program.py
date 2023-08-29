from random import randrange

class MathOperation:
     def __init__(self, a, b):
        self.a = randrange(a, b)
        self.b = randrange(a, b)

     def checkInput(self):
        txt = input(f"{self.a} * {self.b} = ")
        if txt.isdigit():
            return self.multiplicationNumber(txt)
        else:
            return print('Вы ввели не число')
        
     def multiplicationNumber(self, txt): 
        result = self.a * self.b
        if int(txt) == result:
            print(f"+++++++++++++ :-) {self.a} * {self.b} = {result}")
            self.a = randrange(1, 10)
            self.b = randrange(1, 10)
            return self.checkInput()
        else:
            return print(f"------------- :-( {self.a} * {self.b} = {result}")
        
intervalNumber = MathOperation(1, 10)
intervalNumber.checkInput()



#function program

'''def multiplicationNumber(txt, a, b):
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

genericRandomNum(1, 10)'''



    