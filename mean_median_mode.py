
#################################################
# Calculating the mean, median, and mode
#
# Input Format-
# N - number of elements in the array
# arr - space-separated integers describing the array's elements.
#
# Output Format -
# Mean
# Median
# Mode
#################################################

import sys

N = int(input())
arr = list(map(int, input().split()))

if N != len(arr):
    print('Invalid input')
    sys.exit(1)

if(N == 0):
    print(0)
    print(0)
    print(0)
else:
    # mean
    print(sum(arr)/N)
    # median
    sorted_arr = sorted(arr)
    if(N%2==0):
        print((sorted_arr[int(N/2)]+sorted_arr[int(N/2)-1])/2)
    else:
        print(sorted_arr[int((N-1)/2)])
    # mode
    frq_lst = dict()
    for e in set(sorted_arr):
        frq_lst[e] = 0
    max_val = 0
    mode_val = None
    for e in sorted_arr:
        frq_lst[e] = frq_lst[e]+1
        if frq_lst[e] > max_val:
            max_val = frq_lst[e]
            mode_val = e
    print(mode_val)

