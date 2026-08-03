'''
Variable sliding window Problems:
Array based:
209. Minimum Size Subarray Sum
713. Subarray product less than K
904. Fruit Into Baskets

Longest substring based:
3. Longest Substring Without Repeating Characters
424. Longest Repeating Character Replacement
'''
from typing import List
def totalFruit(f: List[int]) -> int:
    left,ans = 0,0
    freq = {}
    for right in range(len(f)):
        freq[f[right]] = freq.get(f[right],0) + 1
        while len(freq) > 2:
            freq[f[left]] -= 1
            if freq[f[left]] == 0:
                del freq[f[left]]
            left += 1
        ans = max(ans,right-left+1)
    return ans
fruits = [1,2,1]
print(totalFruit(fruits))

def lengthOfLongestSubstring(s: str) -> int:
    left,ans = 0,0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        ans = max(ans,right-left+1)
    return ans
s = "abcabcbb"
print(lengthOfLongestSubstring(s))