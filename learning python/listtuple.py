#tuples are immutable lists
mytuple = ("apple", "banana", "cherry")
print(mytuple)  
print(type(mytuple))
print(mytuple[1])
#to convert the tuple to list
mylist = list(mytuple)
print(mylist)
print(type(mylist))
mylist[1] = "kiwi"
print(mylist)
#to convert the list back to tuple
#methods of the tuple
mytuple.index("cherry")
print(mytuple.index("cherry"))
mytuple.count("apple")
print(mytuple.count("apple"))

