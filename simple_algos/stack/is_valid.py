###
# Solution to is_valid parenthesis easy leetcode problem
###
# This soltution focuses on using a stack that will hold that element or char that corresponds for
# the one that we are searching for. We store them as key: val pairs for easy checking and quick lookup

# Runtime:12ms 98.16%
# Space: 13.5mb 87.56%


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # the stack will track open brackets
        stack = []

        # Dict of the various parenthesis we are looking for
        paren = {')': '(', '}': '{', ']':'['}

        for char in s:
            # if char is a closing bracket
            if char in paren:
                # This returns the top element of the stack if there is one
                top_elem = stack.pop() if stack else '#'

                # Use the closing delim as key and search dict; so if top value is the opening bracket
                if paren[char] != top_elem:
                    return False

            else:
                # opening bracket, so push to the stack
                stack.append(char)

        # if the stack is empty at the end we have a valid statement 
        # if there are any values in stack we want to return false
        return not stack
