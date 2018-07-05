"""
For this I will deconstruct the inputs into a list
of acceptable jewels and a list of your current stones.
Then, I visit each stone and see if it is in the current
jewels list.

:author: Ronald Rounsifer
:version: 07.05.2018
"""
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = []
        stones = []
        tot_num_jewels = 0

        # Populate lists with characters
        for char in J:
        	jewels.append(char)
        for char in S:
        	stones.append(char)

        for stone in stones:
        	if stone in jewels:
        		tot_num_jewels += 1

        return tot_num_jewels
