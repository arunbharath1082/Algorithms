def kandane(arr):
    sum1=arr[0]
    temp=0
    for i in arr:
        temp=temp+i
        if temp>sum1:
            sum1=temp
        elif temp<0:
            temp=0
    return sum1


if __name__=="__main__":
    arr=[1,2,3,-4,-3]
    value=kandane(arr)
    print(value)
