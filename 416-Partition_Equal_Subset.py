"""
Problem Summary:
For the given array we return True if can be split to two subset uch that the sum of the elements in both subsets is equal, otherwise false.

Approach:
Consider it as a task to find a sunset with sum equal to target, when target is half sum of the original array/
"""

#0/1 Knapsack Top Down DP
#Time Complexity: O(N∗target) - Where N is the length of array and targent as described, there are at most N * target unique states.
#Space Complexity: O(N∗target) - For storing the dictionary and the recursion call stack .

class Solution1:
    def canPartition(self, nums: list[int]) -> bool:
        sm = sum(nums)
        if sm % 2 != 0: #for odd sum there is no chance for equal subsets
            return False
            
        target = sm // 2
        n = len(nums)

        memo = {}
        def req(i, curr):
            if curr == target:#find possibility 
                return True
            
            if (i, curr) in memo:#already been calculated
                return memo[(i, curr)]

            if i == n or curr > target: #there is no equa subsets
                return False
            
            memo[(i, curr)] = req(i+1, curr+nums[i]) or req(i+1, curr)

            return memo[(i, curr)]

        return req(0,0)

# # # # # # # # # # # # # # # # # # # # 


# Bottom-Up DP with a hash set:
# Time Complexity: O(N * Target) - iterate through N numbers and update up to Target sums.
# Space Complexity: O(Target) - memory used by the 'dp' hash set.
class Solution2:
    def canPartition(self, nums: list[int]) -> bool:
        sm = sum(nums)
        if sm % 2 != 0: #same
            return False
        
        target = sm // 2
        dp = {0}
        for num in nums:
            #new sums- by adding current number to the previously sums
            next = set(dp)
            for part in dp:
                if num+part == target:#found
                    return True
                if num+part < target:#to next round
                    next.add(num+part)
            
            dp = next

        return target in dp

        


            



            
