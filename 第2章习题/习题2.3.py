import math

# x1,y1,x2,y2 = map(int, input().split())

x1,y1,x2,y2 = map(float, input().split())

print("%.2f" % ( math.sqrt(pow(abs(x1-x2),2)+pow(abs(y1-y2),2)) ))


'''
0 0 0.5 0.5
0.71

1 1 2 2
1.41
'''
