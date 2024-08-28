 # variable and data types


# string(str) -> string is anything between single or double quote
# name  = "jamiu"
# # print(name)
# # print(type(name))
# first_name = "Ola"
# last_name = "Wale"
# full_name = first_name + " " + last_name
# print("Hello " + full_name)
# print(type(full_name))
# j = 3
# p = "jamiu"
# print(j , p)

# Multiline strings -> Three doudle quotes or three single quotes
# a = """ asdrfghjkl
# wertyghjkl
# ertyuijk'"""
# print(a)

# String length  ->{len} to get a length of  a String 
# a = " bola ola "
# print(len(a))

# Check String ->{in} to check if a certain phrase or character is present in a string. 
# text = "I love working with strings"
# print("love" in text)

# c4t = "best place to learn programming"
# if "best place" in c4t:
#     print("best place" in c4t)

# Check if Not -> {not in} to check if a certain phrase or character is not present ina string. 
# x = "python is very easy to learn"
# if "much" not in x:
#     print ("Yes, 'much' is not present in a string")


# Modify Strings
# Upper case -> 
# a = "Python is popular"
# print(a.upper())


# Lower case
# b = "Python Is GOOd Enough to build something fun"
# print(b.lower())

# Remove WhiteSpace -> Remove spaces from beginning and end
# a = " Hello, world! "
# print(a.strip())


# Replace String
# a = "Hello Tolani "
# print(a.replace("ll","kk" ))
# print(a.replace("Hello", "Hi"))


# String count method -> return number the number of times the value appears in a string
# t = "I love python because we use python to build software"
# x = t.count("python")
# print(x)






# integer (int) it can't store decimal numbers
# age = 18
# age = age + 1
# age -= 1
# age *= 3
# age  += 1
# print(type(age))
# print(type(age))
# print("Your age is :" + age) # TypeError: can only concatenate str (not "int") to str
# print("Your age is :" + str(age))



# float -> float can store decimal numbers
# money = 450.5
# print(type(money))
# print("Your money is :" + money) TypeError: can only concatenate str (not "float") to str
# print("Your money is:" + str(money))




# Boolean (True or false) -> it is very useful in if statement
# friend =True
# print (friend)
# print(type(friend))
# print (4 > 3)
# print (6 > 10)

# enemy = False
# print(enemy)




# MULTIPLE ASSIGNMENT
#Many Values to Multiple Variables
# Name, location , age = "Paul", "Lagos", 17
# print(Name)
# print(location)
# print(age)

# One Value to Multiple Variables
# a = b = c = "Unilag"
# print(a, b, c)
# print(a)
# print(b)
# print(c)

# Unpack a Collection
# foods = ["rice", "beans", "bread"]
# x, y, z = foods
# print(x)
# print(y)
# print(z)



# fruits = ["rice", "beans", "bread"]
# print("bread" in fruits)


# x = 5
# del x
# print(x)

# food = ["yyy", "zzz" , "ttt", "udhs", 9]
# del food[4]
# del food
# print(food)

# Casting

# x = str(2)
# # x = 4
# print(type(x))

# y = float(9)
# y = 9
# print(y)
# print(type(y))

# z = int(90.8)
# print(z)
# print(type(z))



# Python Operators
# Arithmetic Operators -> it is use with numeric value to perform common mathematical operation.
# x = 10 
# g = 3
# print (x // g)


# Assignment  Operators
# age = 5
# age /=2
# print(age)

# Comparison Operators
# friend =  "Desire"
# dept = "backend"
# if (friend != "Tayo"):
#     print("Wow nice to meet you ", friend )

# age = 18
# if (age <= 17): print("You are  eligible to vote")


#  Logical Operators
# x = 10
# print(x > 4 and  x < 10)	
# # print(x < 4 or x <= 10)
# print(not(x > 4 and  x >= 10) )



# DATA SEQUENCE
# LIST
fruits_list =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(len(fruits_list))
# print(fruits_list[6])
# print(fruits_list[-1])
# print(fruits_list[2:6])
# fruits_list.append("orange")
# fruits_list.insert(0, "pineapple")
# fruits_list.remove("banana")
# fruits_list.pop(0)
# del fruits_list[5]
# del fruits_list
# fruits_list.clear()
# print(type(fruits_list))
print(fruits_list)
