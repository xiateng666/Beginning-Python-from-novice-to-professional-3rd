# import语句必须放在首行
# 常用math函数
import math
import cmath

# 绝对值 output:10
print(abs(-10))

# 四舍五入
# output:3.0
print(round(3.499))
# output:4.0
print(round(3.5001))

# floor ceil
# floor 向下取整
# ceil 向上取整
print(math.floor(3.9999))
print(math.ceil(3.000001))

# sqrt 实数与复数形式
print(math.sqrt(12))
print(cmath.sqrt(-12))
