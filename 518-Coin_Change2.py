"""
note: it easier after Coin Change.

Problem Summary:
Find the number of ways to made up amount from coins array(you can repeat coins).

Approach: 
Think of this as a 2D grid where rows represent the available coins and columns the amounts.
Each cell stores the number of ways to reach that column's amount.
Since we can only choose to skip the current coin or use it, the number of ways for any current cell is simply 
the sum of the ways from the cell directly below it (skipping the coin) and the cell to its left by the coin's value (using the coin).

Start with top-down memoization, move to a 2D grid, and finally optimize space down to 1D.
"""


#Top-down dp, using dfs+memo
# Start from the target amount and the first coin,
#  recursively choosing to either use the coin or skip to the next.
#Time complexity: O(M * N) where M is number of coins and N is amout- Going over each combination.
#Space Complexity: O(M * N) - Memoization table + recursion stack depth of O(M + N)
class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def req(sum, start)-> int:
            if (sum, start) in cache:# allready been calculate
                return cache[(sum, start)]
            if sum < 0:#no reason to substract more
                return 0
            if start == len(coins):#edge case
                return 0
            if sum == 0:# found 1 total that sum up to amount
                return 1

            cache[(sum, start)] = req(sum- coins[start], start) + req(sum, start + 1)
            return cache[(sum, start)]

        return req(amount,0)

# # # # # # # # # # # # # # # # # # # 


#Button-up dp, looping over the grid.
# Iteratively filling a 2D matrix based on the options (coins) and amounts.
#Time complexity: O(M * N) where M is number of coins and N is amout- Going over each combination.
#Space Complexity: O(M * N) - 2D DP table.
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]* (n +1) for _ in range(amount +1)]
        dp[0] = [1] * (n+1) #one possibility to not take any coin for amount 0

        #looping from options for zero amount till the actual amount
        for sum in range(amount +1):
            #starting with no coins then 1 2 and so on..
            for start in range(n-1,-1,-1):
                dp[sum][start] = dp[sum][start + 1] #taking the options from less coins that we calculated
                
                previous = sum - coins[start] #relaing on previous amount with the same number of coins
                if previous >= 0:#possible
                    dp[sum][start] += dp[previous][start]#adding the options

        return dp[amount][0]#the final result

# # # # # # # # # # # # # # # # # # # 


#Button-up dp, memory optimize.
# Same logic as the 2D grid, but only keeping track of the current and previous rows to save space.
#Time complexity: O(M * N) where M is number of coins and N is amout- Going over each combination.
#Space Complexity: O(N) - havig just 2 row in amount length.
class Solution3:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        row = [0 for _ in range(amount +1)]
        row[0] = 1 #one possibility to not take any coin for amount 0

        #starting with no coins then 1 2 and so on..
        for start in range(n-1,-1,-1):
            newRow = [0] * (amount +1)
            newRow[0] = 1

            #looping from options for zero amount till the actual amount
            for sum in range(amount +1): 
                newRow[sum] = row[sum]
                
                previous = sum - coins[start] #relaing on previous amount with the same number of coins
                if previous >= 0:#possible
                    newRow[sum] += newRow[previous]#adding the options
            row = newRow

        return row[amount]#the final result



