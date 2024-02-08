#  Approach -1
# using two arrays left greater and right greater
# Time complexity O(n)
# Space Complexity O(n)

def rainwater(arr):

    n=len(arr)
    left=[0]*n
    right=[0]*n

    left[0]=arr[0]

    for i in range(1,n):
        left[i]=max(left[i-1],arr[i])

    right[n-1] = arr[n-1] 

    for i in range(n-2, -1, -1): 
        right[i] = max(right[i + 1], arr[i]) 

    water=0

    for i in range(n):
        water+=min(left[i],right[i])-arr[i]

    return water



if __name__=="__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(rainwater(arr))


    