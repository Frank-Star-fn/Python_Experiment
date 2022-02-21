import random as rd

target=rd.randint(1,100)
print("猜数字")
cnt=0

while True:
    guess=eval(input("输入猜测的数值："))
    cnt+=1
    if guess>target:
        print("太大了！")
    elif guess<target:
        print("太小了！")
    else:
        print("好棒，{}次就猜中了！".format(cnt))
        break
    
