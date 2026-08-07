'''
1480 – Running Sum of 1d Array
303 – Range Sum Query - Immutable
724 – Find Pivot Index
1991 – Find the Middle Index in Array
1732 – Find the Highest Altitude
560 – Subarray Sum Equals K
'''
'''
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
'''
nums = [1,2,3,4]
res = [0] * (len(nums))
for i in range(len(nums)):
    curr_sum = 0
    for j in range(0,i+1):
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)

nums = [1,2,3,4]
for i in range(1,len(nums)):
    nums[i] = nums[i] + nums[i-1]
print(nums)