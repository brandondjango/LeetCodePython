#Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.
#
#Return the two integers in any order.
#
#
#
#Example 1:
#
#Input: num = 8
#Output: [3,3]
#Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
#Example 2:
#
#Input: num = 123
#Output: [5,25]
#Example 3:
#
#Input: num = 999
#Output: [40,25]
#
#
#Constraints:
#
#1 <= num <= 10^9
import math
from math import floor


def return_closest_divisors_for_plus_1_and_2(n):
    divisors1 = return_divisors(n+1)
    divisors2 = return_divisors(n+2)
    return min(abs(divisors1[0]-divisors1[1]), abs(divisors2[0]-divisors2[1]))


def return_divisors(n):
    num1 = floor(math.sqrt(n))
    num2 = math.ceil(math.sqrt(n))
    while n % num1 != 0:
        num1 = num1 - 1
    while n % num2 != 0:
        num2 = num2 + 1
    print(num1, num2)
    return [num1,num2]

print(return_closest_divisors_for_plus_1_and_2(999))