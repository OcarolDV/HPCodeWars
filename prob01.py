import math

def beePop(t):
    if t <= 0:
        return False
    pop = 100*math.sqrt(t) + 201 / (t+1) + 1
    print (t, int((round(pop, 0))))

beePop(7)
beePop(38)
beePop(24)
beePop(0)
