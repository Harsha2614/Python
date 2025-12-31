
#collection single "variable" used to store multiple values
#List[] ordered and changeable. Duplicates OK
#fruits=["apple", "orange", "banana" "coconut","apple"]
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)
#fruits[0]= "pineapple"
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count('apple'))


#Set= {} unordered and immutable, but Add/Remove OK. NO duplicates

#fruits={"apple", "orange 'banana", "coconut"}

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)
#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop()
# fruits.clear()
# print(fruits)

#Tuple() ordered and unchangeable. Duplicates OK. FASTER

# fruits=("apple", "orange", "banana", "coconut", "coconut")
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)
#print(fruits.index("apple"))
# print(fruits.count("coconut"))
# #print(fruits)
# for fruit in fruits:
#  print(fruit)


# Dictionary a collection of (key: value) pairs ordered and changeable. No duplicates

d={'Japan':'Tokyo','India':'Delhi'}
# d.update({'China':'Bejing'})
# if d.get('Japan'):
#     print("Capital Exists")
# else:
#     print("False")
# print(d)

# d.pop('China')
# print(d)

# d.popitem() #pops last element
# print(d)

# d.clear()
# print(d)

# keys=d.keys()
# for k in keys:
#  print(k)

# values=d.values()
# for v in values:
#     print(v)

items=d.items()

for k in items:
    print(k)