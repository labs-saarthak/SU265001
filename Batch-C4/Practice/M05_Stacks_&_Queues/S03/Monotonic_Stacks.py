'''
Monotonic of stacks:It is mainly used to store the data in a specific order
Either in the increasing order or decreasing order

Types: 2
1.Monotonic of Increasing order
2.Monotonic of decreasing order

1.Monotonic of Increasing order:
Algorithm:
1. Create an Empty stack
2. Traverse through each element:
    -->While stack not empty and stack[-1] > num:
        ---> remove the top element from the stack
    --->Append the element into stack
3. return stack
'''
def monotonic_Increasing(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack
arr =[12,21,76,2,5]
print(monotonic_Increasing(arr))

'''
2.Monotonic of decreasing order:
Algorithm:
1. Create an Empty stack
2. Traverse through each element:
    -->While stack not empty and stack[-1] < num:
        ---> remove the top element from the stack
    --->Append the element into stack
3. return stack'''

def monotonic_decreasing(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    return stack
arr =[12,21,76,2,5]
print(monotonic_decreasing(arr))

#What type of problems they can ask in interview:
'''
1. Next greater element
2. Next Smallest Element
3. Previous Greater Element
4. Previous Smallest element'''

#1. Next greater element:
#Brute force Algorithm:
'''1. Calculate the length of arr
2. initialize res with [-1] upto size
3. Traverse all index:
   -->For every index, upto to right to arr:
      -->if arr[j] > arr[i]:
          -->res[i] = arr[j]
4. Return res
'''
def next_greater(arr):
    n = len(arr)
    res = [-1] * n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    return res
arr = [2,1,5,3,4]
print(next_greater(arr))

#Optimaml Solution for next_Greater Elem:
#Algorithm:
'''
1. Calculate the length of arr
2. Initialize res with [-1] upto size 
3. Create an empty stack
4. Traverse from left to right:
   -->while stack not empty and top elem in stack < arr[i]:
      --> store the pop() element
      --> Assign the value to the index 
   --> store index value in the stack
5. return res 
'''
def next_greater2(arr):
    n = len(arr)
    res = [-1] * n
    stack =[]
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            res[index] = arr[i]
        stack.append(i)
    return res
arr = [2,1,5,3,4]
print(next_greater2(arr))

'''
#Important for Interview:
next Greater elem --> Use Decreasing Method
prev Greater elem --> Use Decreasing Method

next Smaller elem --> Use Increasing Method
prev Smaller elem --> Use Increasing Method
'''
#Optimaml Solution for next_Smaller Elem:
def next_smaller(arr):
    n = len(arr)
    res = [-1] * n
    stack =[]
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            index = stack.pop()
            res[index] = arr[i]
        stack.append(i)
    return res
arr = [2,1,5,3,4]
print(next_smaller(arr))

#Optimaml Solution for prev_Greater Elem:
def prev_greater(arr):
    n = len(arr)
    res = [-1] * n
    stack =[]
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = arr[stack[-1]]
        stack.append(i)
    return res
arr = [2,1,5,3,4]
print(prev_greater(arr))