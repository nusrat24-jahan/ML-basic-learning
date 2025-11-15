# while i<=100:
#     print(i)
#     i+=1

# while i>=1:
#     print(i)
#     i-=1

# n=int(input("Enter a number: "))
# #for printing the table of the number
# while i<=10:
#    print(f"{n} x {i} = {n*i}")
#    i+=1
# while i<=10:
#    print(f"{n} x {i} = {n*i}")
#    i+=1
mylist=[]
i=1
while i<=10:
   print((i*i))
   mylist.append(i*i)
   i+=1  
print(mylist)
k=36
for j in mylist:
    print(j)
    if j==k:
        print(f"{k} is present in the list")
        break
else:
    print(f"{k} is not present in the list")
print("loop ended")
