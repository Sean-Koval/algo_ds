### This solution is for taking in an int and reversing it

## Runtime: 16ms faster than 88.96%
## Memory: 13.4 MB less than 66.54%


###
# The idea behind this solution is to first turn the int into a string after checking bounds.
# Then the cases regarding -1 are handled
# We slice the string removing the first/last value and concat with the value '-' that we want at the beginning
###

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mina = -2**31
        maxa = 2**31 -1

        if x <= mina or x >= maxa:
            return 0
        else:
            m = str(x)
            if x >= 0:
                fin = m[::-1]
            else:
                temp = m[1:]
                temp2 = temp[::-1]
                fin = '-' + temp2

            if int(fin) >= 2 ** 31 -1 or int(fin) <= -2 ** 31:
                return 0
            else:
                return int(fin)