def kandane(arr): ##maximum subarray sum
    sum1=arr[0]
    temp=0
    for i in arr:
        temp=temp+i
        if temp>sum1:
            sum1=temp
        elif temp<0:
            temp=0
    return sum1


def maxSubarrayProduct(arr, n):
 
    # max positive product
    # ending at the current position
    max_ending_here = arr[0]
 
    # min negative product ending
    # at the current position
    min_ending_here = arr[0]
 
    # Initialize overall max product
    max_so_far = arr[0]
 
    # /* Traverse through the array.
    # the maximum product subarray ending at an index
    # will be the maximum of the element itself,
    # the product of element and max product ending previously
    # and the min product ending previously. */
    for i in range(1, n):
        temp = max(max(arr[i], arr[i] * max_ending_here),
                   arr[i] * min_ending_here)
        min_ending_here = min(
            min(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)
        max_ending_here = temp
        max_so_far = max(max_so_far, max_ending_here)
 
    return max_so_far


if __name__=="__main__":
    arr=[6,-3,-10,0, 2]
    value=kandane(arr)
    value2=maxSubarrayProduct(arr,len(arr))
    print(value)
    print(value2)
