"""Number 1"""
# Write a program which will find all such numbers which are divisible
# by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Consider use range(#begin, #end) method.
"""Solution N. 1"""
# print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 == 0), sep=',')

"""Number 2"""
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320
# In case of input data being supplied to the question, it should be assumed to be a console input

"""Solution N. 2"""
# facto = int(input("What factorial do you wish to calculate"))
# i = ii = 1
# for i in range(1, facto+1):
#     ii = ii*i
#     i += 1
# print(ii)

"""Number 3"""
# With a given integral number n, write a program to generate a dictionary
# that contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

"""Solution N. 3"""
# num = int(input("What would you like to calculate?: "))
# print({x: x*x for x in range(1, num+1)})
"""Here the function dict() is used in the comprehension mode
it creates a key-value pair each using the for loop"""


"""Number 4"""
# Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then the output should be like this
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# In case of input data being supplied to the question,
# it should be assumed to be a console input.tuple() method can convert list to tuple
"""Solution N. 4"""

# nums = input("Insert numbers here: ")
# nummers = nums.split(',')
# num_tups = tuple(nummers)
# print(nummers, num_tups)

"""Number 5"""
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use init method to construct some parameters
"""Solution N. 5"""

# class Strings:
#     """A simple class to receive and print strings in upper case"""
#
#     def getString(self):
#         self.string = input("Please enter a string to print in UPPER CASE: ")
#
#     def printString(self):
#         print(self.string.upper())
#
# waddup = Strings()
# waddup.getString()
# waddup.printString()


"""Number 6"""
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated
# sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
# input: 100,150,180
# output: 18,22,24

"""Solution N. 6"""

# import math as m
#
# C = 50
# H = 30
# values = input("Enter the values to calculate: ")
# values = values.split(',')
# D = [float(i) for i in values]
# Q = [str(round(m.sqrt((2*C*d)/H))) for d in D]
# print(','.join(Q))


"""Number 7"""
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be ij
#
# Note: i=0,1.., X-1; j=0,1, Y-1.
# Suppose the following inputs are given to the program:
# input: 3,5
# output: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

"""Solution N. 7"""

# dimensions = input("Select the dimensions: ").split(',')
# xs = list(range(int(dimensions[0])))
# ys = list(range(int(dimensions[1])))
# in_list, out_list = [], []
# for x in xs:
#     for y in ys:
#         in_product = x*y
#         in_list.append(in_product)
#     out_list.append(in_list)
#     in_list = []
# print(out_list)


"""Number 8 """
# write a program that accepts a comma separated sequence of words
# as input and prints the words in a comma separated sequence after
# sorting them alphabetically

"""Solution N. 8"""

# words = input("Enter words to sort out: ").lower()
# print(','.join(sorted(words.split(','))))


"""Number 9"""
# Write a program that accepts sequence of lines as input and prints
# the lines after making all characters in the sentence capitalized.

"""Solution N. 9"""

# text = []
# while True:
#     chars = input("What shall we capitalize today?: ")
#     if chars =='':
#         break
#     text.append(chars.upper())
# for char in text:
#     print(char)


"""Number 10"""
# Write a program that accepts a sequence of whitespace separated words
# as input and prints the words after removing all duplicate words and
# sorting them alphanumerically.

"""Solution N. 10"""

# words = input("Enter words to sort out: ").lower().split(' ')
# words = ' '.join(sorted(set(words)))
# print(words)

