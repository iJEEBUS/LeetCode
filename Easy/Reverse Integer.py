"""
For this I will deconstruct the integer into a list.
I will then reverse the list, reconstruct a string of
the reversed number, then turn it back into an int.

:author: Ronald Rounsifer
:version: 07.05.2018
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        __UPPER_BOUND = 2**31 - 1
        __LOWER_BOUND = -2**31
        og_num = x
        og_num_list = []
        reverse_num_list = []
        reverse_num = 0
        reverse_num_string = ""
        leading_zero = False

        # Places negative symbol in front
        # of number if True
        negative = False

        # Create character list for original number
        for char in str(og_num):
        	og_num_list.append(char)

        # New copy of the og number list
        temp = og_num_list[:]

        # Reverse the original number list
        while len(og_num_list) > 0:
        	reverse_num_list.append(og_num_list.pop())

        # Remake the og number list from copy
        og_num_list = temp[:]

        # Checks for negatives
        if og_num < 0:
        	negative = True
        # Check for leading zeros
        if og_num % 10 == 0 and len(og_num_list) > 1:
        	leading_zero = True
        #if og_num_list[-1] == '0' and len(og_num_list) > 1:
        #	leading_zero = True

        # Place negative number into reversed string
        if negative:
        	reverse_num_string += '-'
        	reverse_num_list = reverse_num_list[:len(reverse_num_list)-1]
        
        # If a leading zero is expected then remove it
        # from the reversed list before constructing
        # final string
        if leading_zero:
        	reverse_num_list = reverse_num_list[1:]
        	for char in reverse_num_list:
        		reverse_num_string += char
        else:

        	# Construct string without leading zero
        	for char in reverse_num_list:
        		reverse_num_string += char

        # Check there is something to turn into an integer
        if len(reverse_num_string) > 0:
        	reverse_num = int(reverse_num_string)

        	# Bounds checking and output returns
        	if reverse_num > __UPPER_BOUND or reverse_num < __LOWER_BOUND:
        		return 0
        	else:
        		return reverse_num

testing = Solution()
print(testing.reverse(123))