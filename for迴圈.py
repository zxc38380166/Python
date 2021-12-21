# for letter1 in "小白你好":   #迴圈中放入得式字串則幾個字就執行幾次
#     print(letter1)
# for letter2 in  [1,2,3,4]: #迴圈中放入列表則列表有幾個值就執行幾次
#     print(letter2)   
# for letter3 in range(5):  # range() 中帶入多少值就執行幾次
#     print(letter3)

# 運算過程為 1*2*2*2*2*2
def power(x,y):
    z = 1
    for index in range(y):
        z = z * x
    return z

print(power(2,5))