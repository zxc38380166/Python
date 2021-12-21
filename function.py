def hello(name,age):
    print("hello" + name + "你今年幾歲" + str(age))
hello("小白",22) 
def add(nu1,nu2):
    print(nu1+nu2)  #執行計算後
    return 10       #再回傳一個值

value = add(3,4)
print(value)