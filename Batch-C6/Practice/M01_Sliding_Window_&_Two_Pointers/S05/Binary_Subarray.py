'''
Binary subarray
1493. Longest Subarray of 1's After Deleting One Element
1004. Max Consecutive Ones III 
930. Binary Subarrays With Sum  
'''
from typing import List
def longestSubarray(nums: List[int]) -> int:
    left = 0
    zeros = 0
    max_len = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len,right - left + 1)
    return max_len-1

nums = [0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))

def longestOnes(nums: List[int], k: int) -> int:
    left,zeros = 0,0
    max_len = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len,right - left + 1)
    return max_len

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums,k))

def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    def sub_arr(k):
        if k < 0:
            return 0
        left = 0
        curr_sum = 0
        count = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            count += (right - left + 1)
        return count
    return sub_arr(goal) - sub_arr(goal - 1)

nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums,goal))