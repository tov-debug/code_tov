"""
Problem Summary:
Find the length of the longest subsequence in 'nums' such that the bitwise XOR sum of its elements is non-zero.

Approach:
Simple computing the total XOR sum of all elements,if it != 0, the entire array is the longest valid subsequence.
Otherwise: case all elements in the array are 0, it's impossible to form a non-zero XOR sum. other case removing a single element breaks the zero XOR sum.
"""

# Time Complexity: O(N) - single linear pass.
# Space Complexity: O(1) - constant space.
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xorall = 0

        for num in nums:
            xorall ^= num
        
        # check if array consists entirely of zeros
        if xorall == 0:
            if sum(nums) == 0 and nums[0] == 0 and nums[n-1] == 0:
                return 0
            #else
            return n-1
        #else
        return n
