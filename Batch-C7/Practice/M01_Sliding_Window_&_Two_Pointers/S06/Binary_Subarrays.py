'''
Binary--> 
It contains only 0's and 1's
Ex: 
[1,0,1,0,1,0]
[1]
[1,0]
[1,0,1]
[0]
[0,1]
[1]
[1,1]-->Not a sub-array
-----
-----
-----
'''
#Leetcode : 1493
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left,right = 0, 0
        ans = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                ans += 1
            while ans  > 1:
                if nums[left] == 0:
                    ans -=1
                left += 1
            max_len = max(max_len, right -left + 1)
        return max_len -1
        
#Leet Code : 1004
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        ans = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                ans +=1
            while ans > k:  
                if nums[left] == 0:
                    ans -=1
                left += 1
            max_len= max(max_len, right-left +1)
        return max_len      

#Leet Code : 930