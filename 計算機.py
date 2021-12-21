name = input( "請輸入你的名子:" )
age = input( "你今年幾歲?" )
print("哈囉:"+name+"你今年:"+age+"歲")

nb1 = input("請輸入一個數字:")
nb2 = input("請輸入一個數字:")
#將字串轉換成數字 float 能轉換小數 int 則不行
print( float(nb1)+int(nb2) )

nb3 = float(input("請輸入一個數字"))
op = input("請輸入運算符號")
nb4 = float(input("請輸入一個數字"))
if op=="+":
    print(nb3+nb4)
elif op == "-":
    print(nb3-nb4)
elif op =="/":
    print(nb3/nb4)
elif op =="*":
    print(nb3*nb4)
else:
    print("不支援運算")