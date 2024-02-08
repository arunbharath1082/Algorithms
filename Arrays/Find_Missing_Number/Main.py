# Approach-1

# Using Summation of all the numbers

def missing(arr):
    length=len(arr)
    value=(length+1)*(length+2)//2
    return value-sum(arr)


# Approach-2
# Using XOR method
def getMissingNo(a, n):
    x1 = a[0]
    x2 = 1
 
    for i in range(1, n):
        x1 = x1 ^ a[i]
 
    for i in range(2, n + 2):
        x2 = x2 ^ i
 
    return x1 ^ x2


if __name__=="__main__":
    arr=[1,2,3,5]
    print(missing(arr))
