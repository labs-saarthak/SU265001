'''
Sub-String:Sequence of characters
Ex: 'Kalyani'
'k'
'ka'
'kal'
'kaly'
------
------
------
'kln'-->Not a sub-string(sub-sequence-->Skipping of chara)

'''
#Leet Code : 03
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        a = set()
        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[left])
                left += 1
            a.add(s[right])
            max_len = max(max_len, right - left +1)
        return max_len
                
#Leet Code : 424 
'''
Algorithm : 
1) Initialize with 0
2) Take an Empty Dict, max_len, max_freq and assign with 0
3) Move right pointer towards right (Single char at a time)
4) Find the freq of each char
5) Find the max_freq charac
6) calculate the :
     --> replacement = TotalSizeof_string - max_freq 
     --> Condition : replacement <= k -->Shrink 
     --> increment left +=1
7) Find the max_len
8) Return max_len
'''
#Leet Code : 1208









