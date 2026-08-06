'''
What is Sliding Window:It is very important optimization Technique in DSA
It is also used to reduce the Time Complexity(O(n**2)-->O(n))
Where:
-->Arrays
-->Lists
-->Strings
What Programs:
1) Sub-Array sum
2) Sub-Strings

Real-World Application:
Ex:  H1 H2 H3 H4 H5
Bus-->
1) H1 H2 H3-->Windows
2) H2 H3 H4-->Windows
3) H3 H4 H5-->Windows

Types:
2 Types
1) Fixed Sliding
2) Variable Sliding 

1) Fixed Sliding:
Window Size is Fixed.Not Change


#Maximum Sum of Sub-arrays of k
#Traditional Approach:
def max_sum(arr,k):
    n =len(arr)
    maxsum1 = 0
    for i in range(n-k+1):   #n=5=>i=(5-3+1)=>i=[0,1,2]
        add1 = 0
        for j in range(k):     #k=3-->j=3
            add1 = add1 + arr[i+j]
        maxsum1 = max(maxsum1 , add1)
    return maxsum1
arr= [1,2,3,4,5]
k = 3
print(max_sum(arr,k))

#Optimal Solution:
def max_sum(arr,k):
    add2 = sum(arr[:k])
    maxsum2 = 0
    for i in range(k,len(arr)):
        add2 = add2 - arr[i-k] + arr[i]
        maxsum2 = max(maxsum2, add2)
    return maxsum2
print(max_sum([1,2,3,4,5],3))


#Average of Maximum Sum of Sub-arrays(Leetcode: 643)
def max_sum2(arr,k):
    add2 = sum(arr[:k])
    print(add2 / k)
    for i in range(k,len(arr)):
        add2 = add2 - arr[i-k] + arr[i]
        print(add2 / k)
max_sum2([1,2,3,4,5],3)
#[1,2,3]=>1+2+3=6==> 6/3 =2.0
#[2,3,4]=>2+3+4=9==> 9/3 =3.0
#[3,4,5]=>3+4+5=12==> 12/3 =4.0
'''
#Maximum Sub-array sum Window (Return Window)
#arr=[1,2,3,4,5],k=3
#[1,2,3]=>1+2+3=6
#[2,3,4]=>2+3+4=9
#[3,4,5]=>3+4+5=12

#Output: [3,4,5]

def avg(arr,k):
    add2 = sum(arr[:k])
    maxsum2 = add2
    start =0
    for i in range(k,len(arr)):
        add2 = add2 -arr[i-k] +arr[i]
        if add2 > maxsum2:
            maxsum2 = add2
            start = i - k + 1
    return arr[start : start +1]
print(avg([1,2,3,4,5],3))

   