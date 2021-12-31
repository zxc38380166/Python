class Phone:
    def __init__(self,os,number,is_waterproof): #self是物件的本身
        self.os = os                    #定義物件本身的屬性
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = Phone("ios",123,True)  #帶入屬性的值
phone2 = Phone("andriod",456,False)
print(phone1.os)
print(phone2.number)
        