import math
r=eval(input("输入圆柱体半径r(r>0)："))
h=eval(input("输入圆柱体高度h(h>0)："))
volume=math.pi*r*r*h
print("半径为{}高为{}的圆柱体体积为:{:.2f}".format(r,h,volume))
