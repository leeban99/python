# Write your code here :-)
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair = 0
    edict = dict()
    print(edict)
    print(ar)

    for i in range(n):
        count = 0
        for j in range(n):
            if(ar[i] == ar[j]):
                count = count +1
        edict[ar[i]] = count
    print(edict)
    for key in edict:
        pair=pair + edict[key]//2
    return pair


if __name__ == "__main__":
    # n = int(input())

    # ar = list(map(int, input().rstrip().split()))
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    # print(ar)

    result = sockMerchant(9, ar)

    print(result)
