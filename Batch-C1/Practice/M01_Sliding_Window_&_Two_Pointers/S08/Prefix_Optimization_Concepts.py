'''
1480 : Running Sum of 1d Array
724 : Find Pivot Index
1991 : Find the Middle Index in Array
1732 : Find the Highest Altitude
523. Continuous Subarray Sum
'''
'''
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
'''
#Brute-force
nums = [1,2,3,4]
res = [0] * (len(nums))
for i in range(len(nums)):
    curr_sum = 0
    for j in range(0,i+1):
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)

#optimal solution
nums = [1,2,3,4]
for i in range(1,len(nums)):
    nums[i] = nums[i-1] + nums[i]
print(nums)

#1732 : Find the Highest Altitude

'''
724 : Find Pivot Index
523. Continuous Subarray Sum
1652. Defuse the Bomb
1248. Count Number of Nice Subarrays
1763. Longest Nice Substring
'''