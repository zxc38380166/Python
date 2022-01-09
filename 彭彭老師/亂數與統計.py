import random   # random為隨機模組
number = [15,56,897,123,12,47]
data1 = random.sample(number,3)         # 從number中取得隨機3個值
print(data1)
random.shuffle(number)                  # 隨機調換順序,僅限直接操作陣列
print(number)
data2 = random.random()                 # 取得0~1之間的隨機亂數
print(data2)
data3 = random.uniform(60,100)          # 取得指定區間的隨機亂數
print(data3)
data4 = random.normalvariate(100,10)    # 常態性分配亂數 預設值為100標準差為10意指多數情況會取得90~110間的亂數
print(data4)

import statistics as stat
data5 = stat.mean(number)               # 取得陣列中的平均值
print(data5)