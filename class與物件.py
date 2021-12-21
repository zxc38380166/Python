class phone:
    def __init__(self,os,number,is_waterproof): #self 為class的本身 (os,numer,is_waterproof為要傳入的值)
        self.os = os    
        self.number = number
        self.is_waterproof = is_waterproof
phone1 = phone("ios",123,True)                  #將值帶入class中
phone2 = phone("andriod",456,False) 
print( phone1.os )  # 印出第一個物件的值
print( phone2.os )  # 印出第二個物件的值