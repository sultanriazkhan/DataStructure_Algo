def two_sum(arr, target):
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            return [left,right]
        elif sum<target:
            left+=1
        else:
            right-=1
result=two_sum([1,2,3,4,5,6], 5)
print(f"Result at index: {result}")