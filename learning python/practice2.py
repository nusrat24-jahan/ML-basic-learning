#create a list 
a=[1,2,3,2,1]
b=a.copy()
b.reverse()
if(a==b):
    print("palindrome")
else:   
    print("not palindrome")
print(a)
print(b)
print(type(a))
print(type(b))