#creating the dictonaries
my_dict = {
    "name": "Nusrat", 
    "age": 20,
    "city": "Kurukshtra"
}
print(my_dict)
print(type(my_dict))
#accessing the values
print(my_dict['name'])
print(my_dict.get('age'))
print("new",my_dict.get('country', 'India')) #default value
#adding the values
my_dict['job'] = 'Engineer'
print(my_dict)
my_dict.update({'country': 'India'})
print("mew:",my_dict)
#removing the values
del my_dict['age']  
print(my_dict)
my_dict.pop('city')
print(my_dict)  
my_dict.popitem() #removes the last item
print(my_dict)
#nested dictionaeries
my_dict = {
    "name": "Nusrat", 
    "age": 20,
    "address": {
        "street": "123 Main St",
        "city": "Kurukshtra",
        "country": "India"
    }
}
print(my_dict)
print(my_dict['address']['city'])
#looping through the dictionaery
for key in my_dict:
    print(key, my_dict[key])
for key, value in my_dict.items():
    print(key, value)
#dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares)

#dictionary methods
print(my_dict.keys())
print(my_dict.values()) 
print(my_dict.items())
print(len(my_dict))
my_dict.clear() #removes all the items
print(my_dict)