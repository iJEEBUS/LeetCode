"""
For this I will determine the perimeter of an island
that is represented by an inputted matrix.

:author: Ronald Rounsifer
:version: 07.05.2018
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tot_perimeter = 0
        for row in grid:
        	print row
        		


input = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

testing = Solution()
print(testing.islandPerimeter(input))