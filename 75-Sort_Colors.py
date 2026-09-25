"""
Problem Summary:
For a given array with only 0,1,2 values we have to sort it in place.

Approach:
Mainting 3 ares where: -the left, in indexes 0...l for zeros.
                       -the middele, in indexes l...r for ones.
                       -the right, in indexes r...len(nums) for twos.
looping over the array with index i, and puting each value in iown area.

"""

# Partition with 3 ares.
# Time Complexity: O(N) - just 1 pass over nums.
# Space Complexity: O(1) - contant space.
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        r,l = len(nums)-1, 0

        i = 0
        while i <= r: #no reason to keep going over the right area

            if nums[i] == 0:# zero case
                nums[l], nums[i] = nums[i], nums[l] #swap
                l += 1
                i += 1 #we already take care of the left of us

            elif nums[i] == 2:# two case
                nums[r], nums[i] = nums[i], nums[r]# swap
                r -= 1

            else:# 1 case
                i += 1
        


        
        