'''
Binary subarray:
930. Binary Subarrays With Sum 

Nice subarray:
1248. Count Number of Nice Subarrays
1763. Longest Nice Substring
'''
#930. Binary Subarrays With Sum solution
from typing import List
def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    def sub_arr(k):
        if k < 0:
            return 0
        left = 0
        count = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            count += (right - left + 1)
        return count
    return sub_arr(goal) - sub_arr(goal - 1)

nums = [0,0,0,0,0]
goal = 0
print(numSubarraysWithSum(nums,goal))

#1248. Count Number of Nice Subarrays
def numberOfSubarrays(nums: List[int], k: int) -> int:
    def sub_arr(target):
        if target < 0:
            return 0
        left,count,odd = 0,0,0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd += 1
            while odd > target:
                if nums[left] % 2 == 1:
                    odd -= 1
                left += 1
            count += (right - left + 1)
        return count
    return sub_arr(k) - sub_arr(k-1)

nums = [1,1,2,1,1]
k = 3
print(numberOfSubarrays(nums,k))