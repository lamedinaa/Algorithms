#!/bin/python3

import math
import os
import random
import re
import sys


def hourglassSum(arr):
    # Write your code here
    columnas = len(arr)
    rows = len(arr[0])

    moveColumns = columnas-3
    moveRows = rows - 3
    sumHourGlassAMax = float("-inf")
    for i in range(0,moveRows+1):
        for j in range(0,moveColumns+1):
            sumHourGlassA = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            if sumHourGlassAMax<sumHourGlassA:
                sumHourGlassAMax = sumHourGlassA
    
    return sumHourGlassAMax


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
