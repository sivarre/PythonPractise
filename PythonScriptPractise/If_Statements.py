import numpy as np
from numpy.random import randn

#print(randn())

x=randn()

answer=None
if x>=1:
    answer = "Greater than 1"
elif x>=-1:
    answer = "Between 0 and 1 "
else:
    answer= "Less than -1"
print(x)
print(answer)
