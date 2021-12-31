class Phone:
    def __init__(self,os,number,is_waterproof): #self是物件的本身
        self.os = os                    #定義物件本身的屬性
        self.number = number
        self.is_waterproof = is_waterproof

    def is_ios(self):                  #在類別中也可以定義函式供呼叫
        if self.os == "ios":            #若自身的os為"ios"則回傳True
            return True
        else:
            return False

    def add(self,number1,number2):      #類別中的函式也可以拿來做運算
        return number1+number2

phone1 = Phone("ios",123,True)  #帶入屬性的值
phone2 = Phone("andriod",456,False)

print( phone1.os)
print( phone2.number)
print( phone1.is_ios() )                #呼叫類別中的函式
print( phone2.is_ios() )
print( phone2.add(5,6) )                #呼叫類別中的函式用來運算