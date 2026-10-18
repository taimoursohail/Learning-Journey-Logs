import sys

# 1 byte (8 bit)

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

'''
# Compare the string length result and the simple number.

name = "taimour"
print(len(name))

print(sys.getsizeof(name), "bytes") #It throws the memory bytes of entire 7 characters of memory
print(sys.getsizeof("taimour"), "bytes")

print(sys.getsizeof(len(name)), "bytes") #It throws the memory bytes result of  int 7
print(sys.getsizeof(7), "bytes")

print(sys.getsizeof(), "bytes")
'''

# optional to understand regarding Int Data type:

# 1. Base Overhead (Python 3.12+): Integer ka basic structure 28 bytes ka hota hai
# 2. Binary Chunks: Digits binary (30-bit) chunks mein store hote hain, har extra chunk +4 bytes add karta hai
# 3. Standard Allocation: Value 0 se lekar ~1.07 Billion (2^30 - 1) tak sab integers 28 bytes lete hain
# 4. Memory Expansion: Jab number 1.07 Billion ko cross karta hai, toh auto +4 bytes (total 32 bytes) add ho jate hain
# 5. CPU vs RAM: Arithmetic calculation ka stress CPU par hota hai; sys.getsizeof() sirf final result ki memory measure karta hai

print(sys.getsizeof(0))          # Output: 28 bytes (Base header in modern Python)
print(sys.getsizeof(100))        # Output: 28 bytes (Fits in initial capacity)
print(sys.getsizeof(123456789))  # Output: 28 bytes (9 digits < 1.07 Billion)
print(sys.getsizeof(2**30))      # Output: 32 bytes (Crosses 1.07 Billion threshold)
