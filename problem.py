import numpy as np

def chain(n,m) :
    start = [n,m]
    repeat = False
    while (repeat == False):
        start.append(sum(start[-2:]) % 10)
        if (start[-2] == n) and (start[-1] == m):
            repeat = True
    print(start)
    return start


og = np.arange(100)
num = og.tolist()

while (len(num) > 0):
    m = num[0] % 10
    n = (num[0] - m)//10

    cur_chain = chain(n,m)
    for i in range (len(cur_chain)-2):
        got = cur_chain[i]*10+cur_chain[i+1]
        num.remove(got)

        
