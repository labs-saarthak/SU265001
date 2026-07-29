'''
Sliding Window:
2 tpyes
1. Fixed --> Size of the window in always Fixed
2. Variable

2.Variable Sliding Window:
--> Size of the window is not fixed
--> either may be increase or decrease based upon the condition
Ex: [2,1,5,8,39]
[2]                        Fixed:k=3
[2,1]                      [2,1,5]-->[1,5,8]-->[5,8,39]
[2,1,5]
[2,1,5,8]
[1,5]
[1,5,8]
-------
-------
-------
Real-World Appli:
Meesho Product Purchase app 

Algorithm for Variable Sliding Window:
Step-1: Two-Pointer Approach
Step-2: for loop
Step-3: Expand Window
Step-4: check with condition
Step-5: if condition is false
Step-6: Shrink the window
step-7: Update the result/Answer

How to identify, which type of sliding window will be used in problem-solving
Sliding window concepts are mainly used in Sub-arrays or Sub-Strings

Fixed:                                Variable:
1. Size of K                        1. Atmost of K  
2. Length of K                      2. Almost of k
                                    3. Minimum or Maximum of K
                                    4. Less than or equal & greater than or equal to K

#Find the longest Sub-array with sum is less than or equal to k?
# arr=[2,3,1,4,2]
#k=6

def longest(arr,k):
    left =0
    right =0 
    add =0 
    max_len = float('-inf')
    for right in range(len(arr)):
        add += arr[right]
        while add > k:
            add -= arr[left]
            left +=1
        max_len = max(max_len, right - left +1)
    return max_len
print(longest([2,3,1,4,2],6))

'''

#Find the smallest Sub-array with sum is greater than or equal to k?
def smallest(arr,k):
    left =0
    right =0 
    add =0 
    min_len = float('inf')  #min_len=len(arr)+1
    for right in range(len(arr)):
        add += arr[right]
        while add >= k:
            min_len = min(min_len,right-left+1)
            add -= arr[left]
            left += 1
    return 0 if min_len == float('inf') else min_len       
print(smallest([2,3,1,4,2],6))

#leetcode : 209, 713
























