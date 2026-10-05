#Solution - 1
from typing import List
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res=[]
    for  i in range(0,len(nums)-k+1):
        res.append(max(nums[i:i+k]))
    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))

#Solution - 2

from collections import deque
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = deque()
    res = []

    for i in range(len(nums)):
        # Remove indices outside the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Record the maximum once the first window is complete
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))