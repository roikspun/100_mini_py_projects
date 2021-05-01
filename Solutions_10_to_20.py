"""Number 10"""
# Write a program that accepts a sequence of whitespace separated words
# as input and prints the words after removing all duplicate words and
# sorting them alphanumerically.

"""Solution N. 10"""

# words = input("Enter words to sort out: ").lower().split(' ')
# words = ' '.join(sorted(set(words)))
# print(words)


"""Number 11"""
# Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Input: 0100,0011,1010,1001
# Output:  1010
# hint: 5 in binary 101

"""Solution N. 11"""

# numbers = input("Enter numbers to calculate: ").lower().split(',')
# multi5 = []
# for numb in numbers:
#     dec = int(numb, 2)
#     print(dec)
#     if dec%5 == 0:
#         multi5.append(numb)
# print(','.join(multi5))


"""Number 12"""
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

"""Solution N. 12"""

# numbers = []
# for number in range(1000,3001):
#     digit = str(number)
#     if int(digit[0])%2 ==0 and int(digit[1])%2 ==0 and int(digit[2])%2 ==0 and int(digit[3])%2 ==0:
#         numbers.append(digit)
# print(','.join(numbers))


"""Number 13"""
# Write a program that accepts a sentence and calculate the number
# of letters and digits.
# input: hello world! 123
# output: Letters 10
#         Digits 3

"""Solution N. 13"""

# nums, lets = 0, 0
# text = input("Calculate this text:")
# for char in range(len(text)):
#     if text[char] != ' ':
#         try:
#             if type(int(text[char])) == int:
#                 nums += 1
#         except ValueError:
#             lets += 1
# print(f"Letters: {lets}\nDigits: {nums} ")


"""Number 14"""
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# input: Hello
# output: Upper: 1 lower: 4

"""Solution N. 14"""

# ups, lows = 0, 0
# text = input("Coun this: ")
# for char in range(len(text)):
#     if text[char].islower() == True and text[char] != ' ':
#         lows += 1
#     elif text[char].isupper() == True:
#         ups += 1
# print(f"Upper: {ups}\nLower: {lows}")



"""Number 15"""
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# input: 9
# output: 11106

"""Solution N. 15"""

# total, digit = 0, input("Enter digit to calculate: ")
# sum = [int(i*digit) for i in range(1,5)]
# for i in sum:
#     total += i
# print(total)


"""Number 16"""
# Use a list comprehension to square each odd number in a list. The list is input by a sequence
# of comma-separated numbers. >Suppose the following input is supplied to the program:
# Input: 1,2,3,4,5,6,7,8,9
# Output: 1,9,25,49,81

"""Solution N. 16"""

# nums = input("What shall we square today: ").split(',')
# squares = [str(int(num)**2) for num in nums if int(num)%2 != 0]
# print(','.join(squares))


"""Number 17"""
# Write a program that computes the net amount of a bank account based a transaction log
# from console input. The transaction log format is shown as following:
# D 100  D means deposit
# W 200  W means withdrawal
# Suppose the following input:
# D 300
# D 300
# W 200
# D 100
# the output should be:
# 500

"""Solution N. 17"""

# balance = 0
# while True:
#     actions = input("Enter amount and description: ").strip('')
#     if not actions:
#         break
#     net = actions.replace(' ','')
#     try:
#         for char in range(len(net)):
#             if net[char].lower() == 'd':
#                 balance += float(net.lower().strip('d'))
#             elif net[char].lower() == 'w':
#                 if balance < float(net.lower().strip('w')):
#                     print("Not enough funds, try another amount")
#                 else:
#                     balance -= float(net.lower().strip('w'))
#     except ValueError:
#         print("Enter a valid amount for your transaction")
#
# print(f"Balance: {balance}")

"""Number 18"""
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
#   At least 1 letter between [a-z]
#   At least 1 number between [0-9]
#   At least 1 letter between [A-Z]
#   At least 1 character from [$#@]
#   Minimum length of transaction password: 6
#   Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will
# check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.

"""Solution 18"""


## check sum, check[0] changes to 1 if it has a lower case letter
## check[1] changes to 1 if it has an upper case letter
## and so on... if the sum of elements in check is equal to 5
## it is a valid password.

# #words = input("Enter the passwords to check: ").split(',')
# valid = []
# for word in words:
#     check_pswd = [0, 0, 0, 0, 0]
#     for char in range(len(word)):
#         if len(word) > 6 and len(word) < 12:
#             check_pswd[4] = 1 # min and max len checked
#             if 'a'>= word[char] and word[char] <= 'z' and check_pswd[0] == 0:
#                 check_pswd[0] = 1
#             elif word[char] >= '0' and word[char] <= '9' and check_pswd[1] == 0:
#                 check_pswd[1] = 1
#             elif 'A'>= word[char] and word[char] <= 'Z' and check_pswd[2] == 0:
#                 check_pswd[2] = 1
#             elif check_pswd[3] == 0 and word[char] == '$' or word[char] == '#' or word[char] == '@':
#                 check_pswd[3] = 1
#             sum = 0
#             for i in range(len(check_pswd)):
#                 sum += check_pswd[i]
#             if sum == 5:
#                 valid.append(word)
#                 check_pswd = [0, 0, 0, 0, 0]
#         else:
#             print(f"your password '{word}' is not valid, try again")
#             break
# print("Valid passwords:",','.join(valid))

""" Number 19"""
# You are required to write a program to sort the (name, age, score) tuples by ascending order
# where name is string, age and score are numbers.
# The tuples are input by console. The sort criteria is:
#    1: Sort based on name
#    2: Then sort based on age
#    3: Then sort by score
# The priority is that name > age > score.
#
# If the following tuples are given as input to the program:
#
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
#
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""Solution N. 19"""

# from operator import itemgetter, attrgetter
# rank = []
# while True:
#     player = tuple(input("Enter players, age and score: ").split(','))
#     if not player[0]:
#         break
#     rank.append(player)
#
# print(sorted(rank, key=itemgetter(0,1,2)))


"""Number 20"""

# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.
# input: 7
# output:
# 0
# 7
# 14

"""Solution N. 20"""

# class Gen():
#     """A simple generator for multiples of 7 in a range 0 to n"""
#     def multiples_of_7(self,n):
#         for i in range(0,n+1):
#             if i%7 == 0:
#                 yield i
# 
# for i in Gen().multiples_of_7(int(input("Enter range to calculate: "))):
#     print(i)
