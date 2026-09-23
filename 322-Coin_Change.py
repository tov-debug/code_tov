"""
Problem Summary:
Find the minimun number of coins from the array(you can use each coin more than once)
that sum up to the given amount, if that amount can't be made up return -1.

Approach: 
Think of this as finding the shortest path to a target amount.
For Bottom-Up: We can visualize an array (or a 1D grid) where the columns represent the target amounts (from 0 to amount). 
Each cell stores the minimum coins needed for that amount. 
For every amount, we check all coins and take the minimum between its current value and 1 + the value at (amount - coin).
"""

# Top-Down Recursion with Memoization.
# Start from the target amount and recursively subtract coins,
#  using a cache to avoid recalculating the same amounts.
# Time Complexity: O(M * N)- where M is the amount and N is the number of coins.
# Space Complexity: O(M) - for the memoization cache and recursion stack depth
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def req(sum:int)-> int:
            if (sum) in cache:# allready been calculate
                return cache[sum]
            if sum < 0:#no reason to substract more
                return amount + 1
            if sum == 0:# found total that sum up to amount
                return 0
            mn = amount + 1# cant be option with more than amount coins, when each>=0

            #loop over coins option to find the minimum
            for num in coins:
                res = req(sum-num) + 1
                mn = min(mn,res)

            cache[sum] = mn
            return mn

        res = req(amount)
        return -1 if res > amount else res #check if it a real rsult

# # # # # # # # # # # # # # # # # # # #  


# Bottom-up solution (1D DP Array)
# Build the solution iteratively from amount 0 up to the target amount.
# Time Complexity: O(M * N) -where M is the amount and N is the number of coins.
# Space Complexity: O(M) - for the DP array.
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount +1]* (amount +1)
        dp[0] = 0 # 0 coins needed for amount 0

        for num in range(1,amount +1):
            if num in coins:
                dp[num] = 1 # exact coin match

            else:
                # try each coin option to find the minimum
                for coin in coins:
                    if num - coin >= 0:
                        dp[num] = min(dp[num],dp[num - coin]+1)

        # try each coin option to find the minimum               
        return dp[amount] if dp[amount] <= amount else -1
                

            


        
        