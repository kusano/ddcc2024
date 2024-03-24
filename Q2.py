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

g = 9.8*1000

Ts = [0, 3, 2, 5, 1, 6]
for t in Ts:
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
    sr = [(tr_tmp+(0 if t==0 else 90000))%180000]*4
    et = math.hypot(HX[t], HY[t])/500

    if t in [2, 5, 1, 6, 4]:
        if t in [2, 5]:
            tr = -math.pi/4
        else:
            tr = 0
        v = 500 # mm/s
        vx = v*math.sin(tr)
        vy = v*math.cos(tr)
        et = HY[t]/vy
        if t in [5, 6]:
            et *= 1.1
        best = 1e10
        for a in range(-10000,10000):
        #for a in range(-10,10):
            if a==0:
                continue
            a = a/100000
            #a /= 100
            #t2 = -vx/((1/2)*(5/7)*g*math.sin(a)*math.cos(a))
            fa = (1/2)*(5/7)*g*math.sin(a)*math.cos(a)
            fb = vx
            fc = -HX[t]
            sign = 1 if a>0 else -1
            t2 = (-fb+sign*(fb**2-4*fa*fc)**.5)/(2*fa)
            #print(a, a/math.pi*180, abs(t2-et))
            if abs(t2-et)<best:
                best = abs(t2-et)
                besta = a
        #print("besta:", besta/math.pi*180, HX[t])
        d = 800*math.sin(besta)
        Lh = min(25000, max(-25000, int(1000*d/2)))
        Rh = min(25000, max(-25000, -int(1000*d/2)))
        tr = int(tr/math.pi*180*1000)

        if t==6:
            sr[0:3] = [0]*3

    Nu = 10
    Wt = int(et*2*1000)
    if t==5:
        Wt -= 1000
    if t==Ts[-1]:
        Wt = 10000

    print(f"{Th},{Ch},{Lh},{Rh},{tr},{sr[0]},{sr[1]},{sr[2]},{sr[3]},{Nu},{Wt}")
