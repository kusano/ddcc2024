import math

q = [0, 225, 325, 610, 0, 610, 275, 765, 325, 920, 0, 920, -325, 920, 250, 455, 0, 455, 0, 765, -250, 765]
HX = [0]*7
HY = [0]*7
for i in range(7):
    HX[i], HY[i] = q[2*i:2*i+2]
SX = [0]*7
SY = [0]*7
for i in range(4):
    SX[i], SY[i] = q[14+2*i:14+2*i+2]

for t in [0, 3, 1, 2]:
    Th = t+1
    Ch = 0
    Lh = 0
    Rh = 0
    if t==0:
        Ch = 1000
        Lh = -25000
        Rh = -25000
    tr_tmp = int(math.atan2(HX[t], HY[t])/(2*math.pi)*360*1000)
    tr = max(-45000, min(45000, tr_tmp))
    sr = [(tr_tmp+(0 if t==0 else 9000))%18000]*4
    if t==2:
        d = 25000
        Lh = d
        Rh = -d
        tr = -45000
    Nu = 10
    Wt = int((55.-(2+.5*10)*4)/3*1000)
    print(f"{Th},{Ch},{Lh},{Rh},{tr},{sr[0]},{sr[1]},{sr[2]},{sr[3]},{Nu},{Wt}{';'if t==6 else''}")
