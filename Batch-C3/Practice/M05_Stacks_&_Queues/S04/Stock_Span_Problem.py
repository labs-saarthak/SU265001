'''
Stock Span Problem:
for every day prices--no.of consecutive previous days which is lessthan or equal to curr day price
''' 
#Brute Force Algorithm:
'''
1. Find the length of your days
2. initialize span with [1] upto size
3. traverse from left to right:
     --->check the previous
     --->while j >= 0 and price[j] <= price[i]:
           --->Increase span[i] +=1
           ----> decrease j 
4. Store the every day span 
5. Return span

'''
def Stock_Span1(prices):
    n = len(prices)
    span = [1] * n
    for i in range(n):
        j = i -1
        while j >= 0 and prices[j] <= prices[i]:
            span[i] += 1
            j -= 1
    return span
prices = [100,80,60,70,60,75,85]
print(Stock_Span1(prices))

#Optimal Solution Algorithm:
'''
1. Initialize empty stack
2. Initialize empty span
3. Traverse from left to right:
     --->While stack should not empty and price[stack[-1]] <= prices[i]:
        a) Remove the top element
        b) if stack is empty:
             -->Span.append(i+1)
        c) span.append(i -stack[-1])
    d) stack,append(i)
4. return span
'''
def Stock_Span2(prices2):
    stack = []
    span = []
    for i in range(len(prices2)):
        while stack and prices2[stack[-1]] <= prices2[i]:
            stack.pop()
        if not stack:
            span.append(i+1)
        else:
            span.append(i - stack[-1])
        stack.append(i)
    return span
prices2 = [100,80,60,70,60,75,85]
print(Stock_Span2(prices2))
#Leet Code - 901: