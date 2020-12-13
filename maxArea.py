"""Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, 
such that the container contains the most water."""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        i,j = 0,len(height)-1
        
        while i < j:
            maxA = max(maxA,min(height[i],height[j]) * (j-i))
            
            if height[i] < height[j]:
                i+=1
            else:
                j-= 1
        return maxA
