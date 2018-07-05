"""
For this I will deconstruct the integer into a list.
I will then reverse the list and compare the two.
If they are the same, then the input is a palindromic
number.

:author: Ronald Rounsifer
:version: 07.05.2018
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Initial cases since 0-9 are palindromes
        if x >= 0 and x < 10:
            return True

        # Only proceed if the input is a number
        elif type(x) == int:
            og_num = x
            og_num_list = []
            reverse_num_list = []
            
            # Create character list for original number
            for char in str(og_num):
                og_num_list.append(char)

            # Copy og number list
            temp = og_num_list[:]

            # Create reverse list of number
            while len(og_num_list) > 0:
                reverse_num_list.append(og_num_list.pop())

            # Get the og number list back
            og_num_list = temp[:]
            
            # Check if they're the same
            if og_num_list == reverse_num_list:
                return True
            return False

        # Just in case    
        return False    
         
testing = Solution()

print(testing.isPalindrome(-1))