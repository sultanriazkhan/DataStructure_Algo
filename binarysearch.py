def binarysearchalgo(arr, x):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
    return -7
arr=[2,3,4,5,6,7,8,12,56,78,89]

result=binarysearchalgo(arr,14)
if result!=-7:
    print("Element is present at index",result)
else:
    print("Element is not present in array")

