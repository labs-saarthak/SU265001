#496. Next Greater Element I
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    d = {}
    for i in range(len(nums2)-1,-1,-1):
        cur = nums2[i]
        while stack and stack[-1] <= cur:
            stack.pop()
        if stack:
            d[cur] = stack[-1]
        else:
            d[cur] = -1
        stack.append(cur)
    res = []
    for ele in nums1:
        res.append(d[ele])
    return res

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1,nums2))