"""
Problem Summary:
We have to find two non-overlapping subarrays that each sum up to the given target.
and return the minimum sum of their lengths. If not found, return -1.


Approach:
We can look at it as two sides of the array.
We use two sliding windows:
 prefix- finds the shortest valid subarray ending at or before index i.
 sufix- finds the shortest valid subarray starting at or after index i .
Finally, we check all split points to find the minimum combined length from both sides.
"""

# Sliding Window with Prefix/Suffix Arrays
# Time Complexity: O(N) - We pass through the array a few times.
# The sliding windows only move forward, processing each element at most twice.
# Space Complexity: O(N) - For storing the minP and minS arrays.
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        minP, minS = [n] *n, [n]*n

        #prefix:
        left, sum,mn = 0,0,n
        for right in range(n):
            sum += arr[right]
            while sum > target:
                sum -= arr[left]
                left += 1
            if sum == target:
                mn = min(mn, right - left+1)
            minP[right] = mn
        
        #sufix:
        right, sum, mn = n-1,0,n
        for left in range(n-1, -1,-1):
            sum += arr[left]
            while sum > target:
                sum -= arr[right]
                right -= 1
            if sum == target:
                mn = min(mn, right-left +1)
            minS[left] = mn

        #looking for the minimum length:
        ans = n+1
        for i in range(n-1):
            ans = min(ans, minP[i] + minS[i+1])
        return ans if ans < n+1 else -1 
            


            
        