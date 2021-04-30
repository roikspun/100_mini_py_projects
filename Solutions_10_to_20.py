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
