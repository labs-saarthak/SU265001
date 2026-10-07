''''
Monotonic of stacks:
Arranging of elements in a particular either in increasing or decreasing
2 ways
1. Monotomic of Increase order--> small to large
2. Monotomic of Decrease order--> large to small
'''
# 1. Monotomic of Increase order--> small to large
'''Algorithm:
1. Initialize an empty stack
2. Itererate every element
3. for every element:
    -->stack should not empty and top element shopuld be greater than your curr elem
         --> Remove the element
4. insert the curr element
5. In the output it will be monotonic of increasing order elements
'''
def monotonic_increase(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack
arr = [1,3,2,4,5]
print(monotonic_increase(arr))

# 2. Monotomic of decrease order--> large to small
'''Algorithm:
1. Initialize an empty stack
2. Itererate every element
3. for every element:
    -->stack should not empty and top element should be less than your curr elem
         --> Remove the element
4. insert the curr element
5. In the output it will be monotonic of decreasing order elements
'''
def monotonic_decrease(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    return stack
arr = [10,80,20,30,40,60,10]
print(monotonic_decrease(arr))

#Where We apply Monotonic of stacks:
#1. To Find the next greater Element
#2. To Find the next smaller Element
#3. To Find the previous greater element
#4. To Find the Previous smaller Element

#1. To Find the next greater Element:
#Brute Force Algorithm:
'''1. Find the len of arr
2. create an result array with -1 values
3. iterate through each element throught the next right elements
4. check with the condition (if arr[j] > arr[i])
5. Store the arr[j] value in result
6. after iteration return result array'''
#[10,30,50,2,25]-->O/P : [50,50,-1,25,-1]
def next_greater(arr):
    n = len(arr)
    res = [-1] * n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    return res
arr = [5,3,50,2,25]
print(next_greater(arr))

#Optimal Solution Algorithm:Next Greater Element
'''
1. Find the length of array
2. Create a res of array of size n,with -1
3. create an empty stack
4. Traverse the array from left to right
5. For every index:
       -->While stack is not empty and arr[stack[-1]] < arr[i]:
           -->Pop the top index
           -->Store arr[i] as next greater elem
6. After traversal, all indexes remaining in the stack,returns -1
7. Return Res array
'''
def next_greater2(arr):
    n = len(arr)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            res[index] = arr[i]
        stack.append(i)
    return res
arr = [2,1,2,5,8]
print(next_greater2(arr))

#next smaller Elem:
#Previous Greater Elem:
#Previous Smaller Elem:
