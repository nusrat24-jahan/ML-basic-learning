#to make the function of the sum
def sum(a,b):
    return a+b
print(sum(3,5))

#to wap of a function to find the sum of the list
def sum_list(lst):
    sum=0
    for i in lst:
        sum =sum+i
    return sum
print(sum_list([1,2,3,4,5]))
#to wap of a function to find the factorial of a number
def factorial(n):
    if n==0:
        return 1
    else:
        i=1
        while i<=n:
            fact=fact*i
            i=i+1
        return fact
#learning the recursion 
def factorial_rec(n):
    if n==0:
        return 1
    else:
        return n*factorial_rec(n-1)