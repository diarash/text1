#!/usr/bin/env python3
#by diianasuchiapa@gmail.com
#GNU/GPL License
import numpy as np
data_list = np.arange(1, 11, 1)
for x in data_list:
    print("value: "+str(x))
 
x="1"
z=0
try:
    
    z=int(x)+1
    print("ok")
except:
    print("Error in sum of z.")
print(z)

