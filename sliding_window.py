def sliding_window(nums, x):
    if not nums:
        print("Empty list provided.")
        return -1
    left=0
    window_sum=0
    max_sum=0
    for right in range(len(nums)):
        window_sum+=nums[right]
        if right - left +1>x:
            window_sum-=nums[left]
            left+=1
        max_sum=max(max_sum,window_sum)
    return max_sum
result=sliding_window([1,2,3,4,5,3,22,4,4,5,6], 2)
print(result)