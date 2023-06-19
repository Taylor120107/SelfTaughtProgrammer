#functions-this creates a function and sets variables to call upon multiple times throughout code where useful 

# def function(a,b,c):
#     return a + b + c
# result=function(1,2,3)
# print (result)

# #built in functions-this enables you to change data types i.e int to string
# print (int("200"))
# float(99)
# str(23)

#inputs- This will enable you to place inputs in the terminal 

# age = input("Enter your age: ")
# int_age = int(age)
# name = input("Enter your name: ")
# if int_age <21:
#     print("Wow you are young")
# else:
#     print("You are getting older")

#this function below enables you to enter a number 3 times to see if its even or odd. Within the statement we set a 
#parameter of n which starts as a string, we then convert this string to an integer on the next line
#an if else statement is then used to understand whether the number entered is even or odd
def even_odd():
    n = input("Enter a number: ")
    n = int(n)
    if n % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

even_odd()
even_odd()
even_odd()








