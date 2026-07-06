

#s1 = "Hello Karan12"
#print(s1.find("K"))
#print(s1.index("K"))
#s2 = s1.replace("Karan","Mayank")
#original will not change
#print("Main Copy: ",s1)
#print("After using replace: ",s2)
#print(s1.lstrip())
#print(s1.count("K"))


#List
#lst = [1, 2, 3, 74, 66,4, 5, 8, 74]
#print(lst)
#lst.pop(0) #remove by index
#lst.remove(8) # remove by value
#lst.reverse()
#lst.insert(0,77) #Insert at index
#lst.clear()		#Remove all
#print(lst.index(74))#Find index
#print(lst.count(74))#Count value
#lst.sort() #Sort list
#lst.reverse()
#print(lst)

#TUPLES
"""
t = (1,2,3, 4,3, 3)
print(type(t))
#Method		Purpose

print(t.count(3))	#Count value
print(t.index(2))	#Find index
"""

"""
#SETS(MUTABLE, NO DUPLICATES AND UNORDERED)
s = {1,2,3,4,5}
s2 = {5,6,7,8,4}
#Method		Purpose
#s.add("Lassi")
#print(s)
#print(s)    #Add element
#s.remove("a")	#Remove (error if missing)
#s.discard("apple")	#Remove safely
#s.pop()		#Remove random
#s.clear()		#Remove all
#ns = s.union(s2) #Combine sets / |
#print(s|s2)
#print(s.intersection(s2))	#Common elements/ &
#print(s&s2)
#print(s.difference())	#Set difference / - (only in s not in s2)
#print(s-s2)
#print(s.symmetric_difference(s2))
#only uniques values from both sets, no COMMON
#print(s^s2)
#print(s.isdisjoint(s2)) #TRUE IF NOTHING IS COMMON ELSE FALSE
#print(s.issubset(s2))# TRUE if every element of set1 is present  in set2
#print(s.issuperset(s2)) #TRUE If set 1 contains every element of set 2
#-set.clear() will remove the items in set and it will make set empty

#DEL(setname) will delete elements and set itself
"""
#DICTIONARY (KEYS ARE IMMUTABLE, VALUES CAN BE ANYTHING
#d = dict( x=10, y=20,z=74 )
#print(d)


#print(d.get("x")) #safe access
#print(d.keys()) #all keys
#print(d.values()) #all values
#print(d.items()) #KEY VALUE PAIRS
#d.update({"y":77}) # UPDATE THE VALUE IN KEY
#print("AFTER UPDATE: ",d)

#print(d.pop("y"))  # REMOVE KEY by its NAME
#print(d)
#print(d.popitem())  #REMOVES AND RETURNS LAST KEY
#print(d)
#d.clear() empty dict
#del(d) #DELETE WHOLE DICT
#print(d)
#for key in d:
#    print(key," : ", d[key])

#MAP (WORKS ON EACH ELEMENT)
def cube(x):
    return x*x*x

lst = [1,2,3,4,5,6]

#with lambda
#nlst = list(map(lambda x: x*x*x,lst))
#print(nlst)

#without lambda
#newlst = list(map(cube,lst))
#print(newlst)


#FILTER (KEEP ONLY TRUE VALUE)

#newl = list(filter(lambda x: x > 2, lst))
#print(newl)

#REDUCE ( from functools import reduce)
#reduce give only single value as result

#from functools import reduce

#num = [1,2,3,4,5]
#sum = reduce(lambda x,y: x+y ,num)
#print(sum)



#palindrome using filter

words = ["madam","hello","level","world", "racecar"]

pal = list(filter(lambda x: x==x[::-1],words))

print(pal)

#factorial using lambda
# Define the lambda function
"""
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Test it
print(factorial(5))  # Output: 120
"""

from functools import reduce

n = int(input("Enter the number to find factorial: "))

factorial = reduce(lambda x, y: x * y, range(1, n+1))

print(factorial)