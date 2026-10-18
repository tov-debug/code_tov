"""
Problem Summary:
Find the lexicographically smallest list of indices in word1 that forms word2
allowing at most one character mismatch/modification.

Approach:
1. Precompute 'last' array via a right-to-left scan: last[j] stores the maximum 
   index in word1 that can form the suffix word2[j:].
2. Greedy left-to-right match:
   - Always take an exact match word1[i] == word2[j].
   - If mismatch occurs and 'change' is available, take index 'i' if the remaining
     suffix word2[j+1:] can still fit in word1.
"""

# Time Complexity: O(N + M) - where N is len of word1 and M is len of word2. Two linear scans.
# Space Complexity: O(M) - for the array.
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        last = [-1] * len(word2)

        # compute rightmost valid match positions for word2 suffixes
        i = len(word1) - 1
        j = len(word2) - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        change = True
        j = 0

        # build the smallest index sequence
        for i in range(len(word1)):
            if j == len(word2):
                break
            
            #exact character match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            
            #One-time character change/mismatch
            elif change and (j == len(word2)-1  or i < last[j+1]):
                change = False
                ans.append(i)
                j += 1
                
        return ans if j == len(word2) else []
