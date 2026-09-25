"""
Problem Summary:
Given an array and target we want to count number of diffrence ways to sum up to target with + and - operators.

Approach:
At each step, we recursively branch into two options: adding or subtracting the current number. 
To avoid redundant calculations, we cache the result of each state. 
If we reach the end of the array, we check if the accumulated sum matches the target.
"""

#Top-down dp- using simple dfs+memo.
#Time Complexity: O(N * M) - Where N is the length of array and M is the total sum of the array elements, there are at most N * 2M unique states.
#Space Complexity: O(N * M) - For storing the dictionary and the recursion call stack .
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def re(amount:int,i:int)->int:
            if (amount,i) in memo:#already been calculate
                return memo[(amount,i)]
            if i == len(nums): #finish this branch
                if amount == target :#built
                    return 1
                return 0
            memo[(amount,i)] = re(amount+nums[i], i+1) + re(amount-nums[i], i+1)#keeping in memory
            return memo[(amount,i)]
        return re(0,0)

"""
Alternative Approach (Bottom-Up DP):
We can also solve this iteratively to avoid recursion overhead. By only keeping track of the previous row's sums, we can optimize the space complexity to O(M).
Hope to add that solution later on.
"""