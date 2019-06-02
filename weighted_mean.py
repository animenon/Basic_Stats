
#################################################
# Calculating a weighted mean
#
# Input Format
# N - the number of elements in arrays 
# X - space-separated integers which  form array of length N 
# W - space-separated integers describing the weights of respective elements of array X.
#
# Output Format
# Weighted mean(rounded to a scale of 1 decimal place).
#
#################################################

import sys

N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

if (len(X) != N) or (N != len(W)):
    sys.exit(1)

print(round(sum([X[i]*W[i] for i in range(N)])/sum(W), 1))

