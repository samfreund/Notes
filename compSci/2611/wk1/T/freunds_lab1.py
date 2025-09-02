"""
Lab instructions:
1) Rename this file to contain your MSOE username (e.g., my filename would be wrightgs_Lab1.py)
2) Complete the following six methods given the prompts in the comments
3) Test your code to be sure that it works for different input values!
4) Submit your code to Canvas
"""

"""
Problem 1: Nest Egg
Complete the nest_egg(investment, time) method below. 
This method takes in two numbers ('investment' and 'time') and
calculates (and returns) what the value of the initial investment 
will be after a period of 'time' years, assuming that the investment 
grows at 8% per year. The new balance of the investment after a year
can be calcualted by:
new_balance = 1.08*current_balance

For example, an investment of $1000 will have a value of $1080 after 
1 year, $1166.40 after two years, etc.
"""

from math import sqrt


def nest_egg(investment, time):
    return investment * pow(1.08, time)

"""
Problem 2: Nest Egg 2
Complete the nest_egg_2(investment, goal) method below. 
This method takes in two numbers ('investment' and 'goal') and 
returns the amount of time (in years, as an integer) it will take 
the investment to reach the goal, assuming a per-year growth rate 
of 8%.

For example, an initial investment of $1000 will take 10 years to 
reach $2000.
"""


def nest_egg_2(investment, goal):
    years = 0
    balance = investment
    while balance < goal:
        balance *= 1.08
        years += 1
    return years


"""
Problem 3: Draw Triangle
Complete the draw_triangle(width) method below.
This method takes in an integer representing two sides of an 
isosceles right triangle, and returns a String containing a
"pixel" image of the specified triangle, with the right angle
in the upper right corner of the drawing.

For example, draw_triangle(3) should return the following String:
***
 **
  *

Hint: to make a single string contain multiple lines, add a newline
charater ("\n") where you want the line breaks.
"""


def draw_triangle(width):
    returnString = ""

    for i in range(width, 0, -1):
        returnString += " " * (width - i) + "*" * i + "\n"

    return returnString


"""
Problem 4: Prime number checker
Complete the is_prime(number) method below USING A LOOP.
This method takes in an integer ('number') and returns a boolean 
value representing whether that number is prime or not. A prime 
number is a natural number (positive integer) greater than 1 that 
is not a product of two smaller natural numbers.
"""


def is_prime(number):

    if number < 2: return False

    if number % 2 == 0: return False

    for i in range(3, int(sqrt(number) + 1), 2):
        if number % i == 0:
            return False

    return True

"""
Problem 5: Palindrome Checker
Complete the is_palindrome(word) method below.
This method takes in a String ('word') and returns a boolean
value representing whether or not the word is a palindrome.
A palindrome is a word, phrase, or sequence of characters
that reads the same forward and backward (ignoring spaces, punctuation,
and capitalization). For example, the word 'racecar' would return True, 
the word 'automobile' would return False. 'Sit on a potato pan, Otis.' 
should also return True.

Hint: Be sure to do string preprocessing before checking the ordering!
The punctuation marks you need to worry about removing are periods and 
commas. The .replace() method for Strings will likely be helpful here.
"""


def is_palindrome(word):
    
    word = word.replace(".", "").replace(",", " ").replace(" ", "").lower()

    part1 = "" 
    part2 = ""

    # I can cast to int here because I guarantee the numerator is even
    if (len(word) % 2 == 0):
        subLength = int(len(word) / 2)
        part1 = word[:subLength]
        part2 = word[subLength:]
    else:
        subLength = int((len(word) - 1) / 2)
        part1 = word[:subLength]
        part2 = word[subLength + 1:]

    # Invert part two

    inverted2 = ""

    inverted2 = part2[::-1]

    return part1 == inverted2


"""
Problem 6: Credit Card Number Check.

Complete the method below that takes in a 16 digit credit card number (as an integer)
and returns a boolean value representing whether or not the credit card number is valid.

To determine if the number is valid, double every other digit (i.e. the 1st, 3rd,
5th, 7th, 9th, 11th, 13th, and 15th digits). If any of these numbers is greater
than or equal to ten, replace that number with the sum of its digits (e.g. 11 becomes 2).
Then take the sum of the remaining 16 one-digit numbers. If this sum is divisible by 10,
then it is a valid credit card number. Output to the user whether or not their input
number is valid or not.

Note, this algorithm is called the Luhn algorithm. 

Hint: Convert the input card number to a string to easily access individual digits
"""


def cc_check(card_number):
    card_str = str(card_number)
    digits = [int(d) for d in card_str]
    for i in range(0, 16, 2):
        digits[i] *= 2
        if digits[i] >= 10:
            digits[i] = digits[i] // 10 + digits[i] % 10
    total = sum(digits)
    return total % 10 == 0

