### THIS IS USED TO ADD STRINGS TOGETHER ###

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.


num1 = '364'
num2 = '1836'


# approach 1
def solution(num1,num2):
    # this approach si to evaluate the strings as numbers indivually and return addition of the two wrapped in str()
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))

# approach 2 # bit manipulation

def solution(num1, num2):
    n1, n2 = 0,0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)
    return m1 + m2 


