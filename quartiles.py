
#################################################
# Calculating the quartiles
#
# Input Format-
# N - number of elements in the array
# arr - space-separated integers describing the array's elements.
#
# Output Format -
# Q1
# Q2
# Q3
#################################################

N = int(input())
X = list(map(int, input().split()))

if(N != len(X)):
    print('Invalid Input')
    sys.exit(1)

def get_median(sorted_list):
    """ pass sorted list to get median """
    if(N%2==0):
        return (sorted_arr[int(N/2)-1]+sorted_arr[int(N/2)])/2
    else:
        return sorted_arr[int((N-1)/2)]

sorted_x = sorted(X)
if(N%2==0):
    
else:
    # odd
    L = sorted_arr[0:(int(N/2)-1)]
    M = sorted_arr[int((N-1)/2)] # median
    U = sorted_arr[(int(N/2)+1):N-1]

#Q1
print(get_median(L))

#Q2
print(M)

#Q3
print(get_median(U))
