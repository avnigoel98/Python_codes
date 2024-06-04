# a = 5

# print(a)

# print(type(a))


# print(6>3)


# and, or, not

# if(4>20 and 3>0):
#     print("hello")


# input - user wants to enter something
# typecasting - changing the type of data type
# by default - user input is always in string format

# num1 = float(input("Enter your number1: ")) 
# num2 = float(input("Enter your number2: "))

# sum = num1 + num2

# print(sum)

# "2" + "4" = "24"
# 2 + 4 = 6
# 2.0 + 4.0 = 6.0

# write a python program to find remainder when a number is divided by 3.
# the number is given by the user


# strings


# str1 = 'apple'
# str2 = "apple"
# str3 = '''apple'''

# print(str1, str2, str3)

# str = '''Rahul"s birthday' is on 25th'''
# print(str)



# print("2" + "5")  # concatinate, or join 
# print("Good monrning " + "Harry")


# string slicing - take some part of the string

#indexing
#        012345678910...........
# fruit = "avni@gmail.com"

# # [start index : end index - 1 : skip ]
# print(fruit[0:10])  

# task
# take a user input for a user email address and fetch out the name of the person from the email
# length of the user name should be 5 letters only.


# string functions
#       0123456
# name = "harry is learning is python"
# print(name.endswith("abcds"))
# print(name.count('python'))
# print(name.capitalize())
# print(name.find("is")) # gives the first occurance of the word or character, if not present then -1
# print(name.replace("python" , "Java"))

# print(len(name))


# # Write a program to fill in a letter template gievn below with name and date

# letter =  '''
#         Dear <|NAME|>,
#         you are selected!
#         <|DATE|>
#     '''

# # to detect the double spaces in a string
# st = "This is a string with  double    spaces"
# # replace the double spaces with single spaces

# doubleSpace = st.find("  ")
# print(doubleSpace)

# space = st.replace("  " , " ")
# print(space)


# Escape characters  -  \n , \t

letter =  "Dear harry, \n\tyou are selected! \nRegards"

print(letter)

