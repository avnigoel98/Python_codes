# # tuples

# t1 = (2, 4, 5, 6, 8) # tuple with multiple values
# print(t1)
# # print(type(t1))

# # t2 = () # empty tuple
# # print(type(t2))

# # t3 = (2,) # tuple with single element
# # print(type(t3))


# t1[0] = 100 # throws error as cant update tuples once created
# print(t1)

# indexing,
# tuple slicing
# tuple methods / functions

      # 0  1  2  3....
# t1 = (2, 4, 5, 6, 8, 2, 2, 2)
# print(t1.count(2))
# print(t1.index(4))


# Dictionary - (key-value pair)


# dictionary are mutable 
# dictionary are unordered (so no indexing)
# does not have duplicate keys
# list = []
# tuple = ()

myDictionary = {
#     key        value
    "Fast" : "In a quick manner",
    "Harry" : "a friend",
     4 : 100,
    "num" : 78,
    "Marks" : [1, 6, 9, 0],
    "anotherDictioanry" : {"apple" : "fruit", "harry" : "a coder"},
    #"num" : 10
}


#print(myDictionary)

# print(myDictionary["Fast"])
# print(myDictionary["Slow"])

print(myDictionary.get("Fast"))
print(myDictionary.get("Slow"))

# myDictionary["num"] = 1000
# print(myDictionary)

#print(myDictionary["anotherDictioanry"]["apple"])

# dictionary functions / methods

# print(myDictionary.keys())
# print(myDictionary.values())
# print(myDictionary.items())

# update_dict = {"harshita" : "friend", "Shubham" : "friend"}

# myDictionary.update(update_dict)
# print(myDictionary)



# write a program to create a dictionary of Hindi words with values as their english translation.
# Provide user with an option to look it up.

# translater = {
#     "Pankha" :"Fan"
# }

# print("Options are: ", translater.keys())
# print("The translation is :", translater.get(user))

# Create an empty dictionary
# Allow 4 friends to enter favourite language as values and use keys as their names
# Assume that the names are uniques

dict = {}
