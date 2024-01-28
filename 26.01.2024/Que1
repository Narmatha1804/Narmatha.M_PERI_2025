#!/bin/python3

import math
import os
import random
import re
import sys



if _name_ == '_main_':
    n = int(input().strip())
    d=[]
    s=[]
    for i in range(1,n+1):
        if n%i==0:
            d.append(str(i))
    for i in d:
        k=0
        for j in i:
            k+=int(j)
        s.append(k)
    u=max(s)
    y=s.index(u)
    print(d[y])
