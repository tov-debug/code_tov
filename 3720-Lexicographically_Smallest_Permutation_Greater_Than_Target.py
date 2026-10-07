"""
Problem Summary:
Find the lexicographically smallest permutation of string 's' that is strictly greater than 'target'.

Approach:
Count character frequencies in 's'. Use backtracking with a 'flag' to build the result:
- If flag is False: pick characters >= target[idx] to stay valid.
- If flag is True: a larger character was already picked, so pick any smallest available character.
"""

# Backtracking with Frequency Array
# Time Complexity: O(N * 26) - recursion depth up to N with at most 26 letter choices per step.
# Space Complexity: O(N) - recursion stack depth up to N.
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        #frequency of each character in 's'
        counts = [0] * 26
        for ch in s:
            counts[ord(ch)-ord('a')] += 1

        #go over targent and change the smallest possible 
        def req(idx, flag):
            if idx == len(target):#reached end of target
                return "" if flag else None
            
            target_idx = ord(target[idx]) - ord('a')
            start_idx = 0 if flag else target_idx

            #looping over the potantional letters
            for ch in range(start_idx,26):
                if counts[ch] > 0:
                    counts[ch] -= 1 #choose character
                    #mark True if we picked a strictly larger character
                    flag = flag or (ch > target_idx) 

                    res = req(idx + 1, flag)
                    if res is not None:
                        return chr(ord('a') + ch) + res #valid permutation

                    counts[ch] += 1 #backtrack choice

            return None #no valid permutation found

        res = req(0, False)
        return res if res else ""