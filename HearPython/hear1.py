import  math
from  turtle import  *
def hearA(k):
    return 15*math.sin(k)**3
def heraB(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(9000)
bgcolor("pink")
for i in range(1000):
    goto(hearA(i)*20,heraB(i)*20)
    for j in range(5):
        color("red")
    goto(0,0)
done()