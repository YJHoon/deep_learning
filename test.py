import random
import math

def expntl(x):
    return (-x*math.log(random.randint(1,32767)/(32767+1.0)))

def func(): 
    n=0
    Ta=200.0
    Ts=100.0
    simulation_time = 10000.0 
    next_arrival_time = 0.0 
    next_departure_time = simulation_time 
    elapsed_time = 0.0
    B = s = 0.0
    C = L = U = W = X = tb = 0
    tn = elapsed_time
    while elapsed_time < simulation_time :
        if next_arrival_time < next_departure_time :
            elapsed_time = next_arrival_time
            s += n*(elapsed_time - tn)
            n += 1
            tn = elapsed_time
            next_arrival_time = elapsed_time + expntl(Ta) 
            if n==1:
                tb = elapsed_time
                next_departure_time = elapsed_time + expntl(Ts) 
        else :
            elapsed_time = next_departure_time 
            s += n*(elapsed_time - tn)
            n -= 1
            tn = elapsed_time
            C += 1 
            if n>0 :
                next_departure_time = elapsed_time + expntl(Ts) 
            else :
                next_departure_time = simulation_time 
                B += elapsed_time - tb

    X = C / elapsed_time
    #print("throughput = %.6f" % X)
    U = B / elapsed_time
    #print("utilization = %.6f" % U)
    L = s / elapsed_time
    #print("mean customer no. in store = %.6f" % L)
    W = L/ X
    #print("mean residence time per customer = %.6f" % W) 
    return [X,U,L,W]

def main(): 
    a=[0,0,0,0]
    for i in range(0,10000):
        b = func()
        a[0] = a[0] + b[0] 
        a[1] = a[1] + b[1] 
        a[2] = a[2] + b[2] 
        a[3] = a[3] + b[3]
    a[0] /= 10000 
    a[1] /= 10000 
    a[2] /= 10000
    a[3] /= 10000
    print("throughput = %.6f" % a[0])
    print("utilization = %.6f" % a[1])
    print("mean customer no. in store = %.6f" % a[2]) 
    print("mean residence time per customer = %.6f" % a[3])

main()
