"""
Problem Summary:
For a given sorted array we have to return an array with thr squares of the numbers sorted.

Approach:
Insead of simple brute force by using 2 pointers its more eficient.

"""

# Mainting the negitive area and positive and taking the squares in order.
# Time Complexity: O(n) - at most 2 pass over the given array.
# Space Complexity: O(1) - just constant.
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        i = 0

        #looping to the most right negetive
        while i < len(nums) and  nums[i] < 0 :
            i += 1
        l,r = i-1, i

        #with point at each part chossing the lower square each time
        while l >= 0 and r < len(nums):
            num1, num2 = nums[l]**2, nums[r]**2
            if num1 < num2:
                res.append(num1)
                l -= 1
            else:
                res.append(num2)
                r +=1
        
        #adding the rest
        while l >= 0:
            res.append(nums[l]**2)
            l -= 1
        while r < len(nums):
            res.append(nums[r]**2)
            r += 1
            
        return res