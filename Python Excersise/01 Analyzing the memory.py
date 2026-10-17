import sys

# 1char = 1byte (8 bit)

''' 

Question1: After testing multiple arithmetic operations, if the results are identical, the allocated memory bytes remain the same.

For example 100 takes 28bytes so after the test, 99+1 also takes 28bytes

5 * 12 - 12 + 56 - 16 + 12 = 100 is also taking 28 bytes!!! I am wondering why?

Question2: What are modules?


'''

'''

# Welcome

code1 = "Welcome to Python"
print(code1, "and the Memory size is", len(code1),"bytes")

code2 = "Python is fun"
print(code2, "and the Memory size is", len(code2),"bytes")

code3 = "Problem Driven"
print(code3, "and the Memory size is", len(code3),"bytes")

# ComputeExpression
#By lenght method It's difficult for us to extract the exact memory. bauce lenght only calcualte the string len

print(1+1)
print(len("1+1"), "Incorrect") # Incorrect
print(sys.getsizeof(1+1),"bytes", "Correct")

print((10.5 + 2 * 3) / (45 - 3.5))
print(len("(10.5 + 2 * 3) / (45 - 3.5)"), "Incorrect") # Incorrect
print(sys.getsizeof((10.5 + 2 * 3) / (45 - 3.5)), "bytes", "Correct")

# ShowLogicErrors

# Convert Fahrenheit to Celsius
print("Fahrenheit 35 is Celsius degree ")
print(sys.getsizeof("Fahrenheit 35 is Celsius degree"), "bytes")

code4 = '35 Fahrenheit is equals to', (5 / 9 * (35 - 32)), "degree Celcius"
print(code4, sys.getsizeof(code4), "bytes")

'''

'''
# Arthematic Operations
print(sys.getsizeof(100), "bytes")
print(sys.getsizeof(99+1), "bytes")
print(sys.getsizeof(200-100), "bytes")
print(sys.getsizeof(5 * 12 - 12 + 56 - 16 + 12), "bytes")


print(sys.getsizeof(200/2), "bytes") # Division ops use the least memory here.
print(sys.getsizeof(50*2), "bytes")
'''

# Compare the string length result and the simple number.

name = "taimour"
print(len(name))

print(sys.getsizeof(name), "bytes") #It throws the memory bytes of entire 7 characters of memory
print(sys.getsizeof("taimour"), "bytes")

print(sys.getsizeof(len(name)), "bytes") #It throws the memory bytes result of  int 7
print(sys.getsizeof(7), "bytes")

print(sys.getsizeof(), "bytes")