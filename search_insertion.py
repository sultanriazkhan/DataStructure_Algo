def binary_search_insert(arr, target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid= low+(high-low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        return -2
n=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(n):
    element=int(input("Enter element: "))
    arr.append(element)
target=int(input("Enter the target element: "))
result=binary_search_insert(arr, target)
if result!=-2:
    print("Element is present at index",result)
elif result==-2:
    for i in range(len(arr)):
        if arr[i]>target:
            print("Element is not present in array, it can be inserted at index",i)
            break