#fruits = {"apple", "banana", "lemon"} #Set of Strings
#print(fruits) #Printing the set of fruits
#fruits = {"apple", "banana", "lemon", "apple"} #Set of Strings
#print(fruits) #Printing the set of fruits, apple will only appear once since sets do not allow duplicate values
#print(type(fruits)) #Printing the type of the variable, which is a set
#print(len(fruits)) #Printing the length of the set, which is 3 since there are 3 unique elements in the set

#fruits = set(("apple", "banana", "lemon")) #Creating a set using the set() constructor
#print(fruits) #Printing the set of fruits

#fruits = set(()) #Creating an empty set using the set() constructor
#print(fruits) #Printing the empty set
#print(type(fruits)) #Printing the type of the variable, which is a set

#fruits = set {} #Creating an empty set using the set() constructor
#print(fruits) #Printing the empty set
#print(type(fruits)) #Printing the type of the variable, which is a set

#You cannot create an empty set using the {} syntax, as it will create an empty dictionary instead. To create an empty set, you must use the set() constructor.

#You cannot access items in sets using indexing or slicing, as sets are unordered collections of unique elements.
#fruits = {"apple", "banana", "lemon"} #Set of Strings
#print(fruits[0]) #This will raise a TypeError, as sets do not support indexing or slicing

#for i in fruits: #Iterating through the set using a for loop
#    print(i) #Printing each element in the set

#print("banana" in fruits) #Checking if "banana" is in the set, which will return True

#fruits.remove("banana") #Removing "banana" from the set
#print(fruits) #Printing the set of fruits after removing "banana"

#fruits.discard("banana") #Discarding "banana" from the set, which will not raise an error if "banana" is not in the set
#print(fruits) #Printing the set of fruits after discarding "banana"

#x = fruits.pop() #Removing and returning an arbitrary element from the set
#print(x) #Printing the element that was removed from the set

#fruits.clear() #Removing all elements from the set
#print(fruits) #Printing the empty set after clearing all elements

#del fruits #Deleting the set variable, which will remove the set from memory
#print(fruits) #Error because sets have been deleted and no longer exist