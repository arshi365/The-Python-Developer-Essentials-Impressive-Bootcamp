#fruits = ("apple", "banana", "cherry", "date", "elderberry") #Tuple of Strings
#number = (1, 2, 3, 4, 5) #Tuple of Integers
#print(fruits)
#print(number)

#Note: Tuples are immutable, meaning their elements cannot be changed after creation.

#Concatenating tuples
#You can create a new tuple by concatenating existing tuples or by using the tuple() constructor.
#fruits = fruits + ("fig",) #Concatenating a new element to the tuple
#print("The modified tuple of fruits is:", fruits) #Printing the modified tuple

#Access items from a tuple
#fruits = ("apple", "banana", "cherry") #Tuple of Strings
#print("The first fruit in the tuple is:", fruits[0]) #Accessing the first element of the tuple
#print("The last fruit in the tuple is:", fruits[-1]) #Accessing the last element of the tuple
#print(fruits[1:3]) #Accessing a range of elements from the tuple

#Deleting a tuple
#You can delete an entire tuple using the del statement, but you cannot delete individual elements from a tuple.
#fruits = ("apple", "banana", "cherry") #Tuple of Strings
#del fruits #Deleting the entire tuple
#print("The deleted tuple is:", fruits) #This will raise a NameError since the tuple has been deleted