import math 
from turtle import*
def heart(k):
    return 15*math.sin(k)**3
def heart2(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(10000)
bgcolor('blaCK')
for i in range(60000):
    goto(heart(i)*20,heart2(i)*20)
    for j in range(5):
        color("red")
    goto(0,0)
done()