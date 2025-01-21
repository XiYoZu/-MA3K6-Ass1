import numpy as np


start = [1,1]
repeat = False
while (repeat == False):
    start.append(sum(start[-2:]) % 10)
    if (start[-2] == 1) and (start[-1] == 1):
        repeat = True
print(start)
