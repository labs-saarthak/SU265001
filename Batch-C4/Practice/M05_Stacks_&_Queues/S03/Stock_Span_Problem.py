'''
Stock Span :(Previous Greater Elem)
for every day price, 
we need to calculate the no.of consecutive previous days lessthan or equal to current price


#Brute Force:
1. find length prices
2. initialize span with [1] upto size
3. Traverse from left to right:
   ---> take previous val
   while j >= 0 and prices[j] <= prices[i]:
      --> increment span by 1
      --> decrement j 
4. Return span
'''
def Stock_Span1(prices1):
    n = len(prices1)
    span = [1] * n
    for i in range(n):
        j = i-1
        while j>=0 and prices1[j] <= prices1[i]:
            span[i] +=1
            j -= 1
    return span
prices1 = [100,80,60,70,75,85]
print(Stock_Span1(prices1))

#Optimal Solution of Stock Span Problem:  Previous Greater element
'''
1. Create a Empty stack
2. Create a Empty span

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
prices2 = [100,80,60,70,75,85]
print(Stock_Span2(prices2))