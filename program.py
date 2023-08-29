from random import randrange

class MathOperation:
    def __init__(self, start, end):
        self.a = randrange(start, end)
        self.b = randrange(start, end)
        
    def start(self):
        return self.checkInput()   
     
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
            self.updateInit()
            return self.checkInput()
        else:
            return print(f"------------- :-( {self.a} * {self.b} = {result}")
        
    def updateInit(self): 
        self.__init__( 1, 10)
        
intervalNumber = MathOperation(1, 10)
intervalNumber.start()



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



    