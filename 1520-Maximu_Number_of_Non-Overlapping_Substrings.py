"""
Problem Summary:
We have to return an array with the maximum amout of non-overlapping substrings from the given string,
which has the shortest total length.
The main rule is that if a substring contains a specific letter,
it must contain every instance of that letter found in the entire original string.

Approach:
This problem simplifies substring search into choosing non-overlapping intervals.
The "all-or-nothing" rule limits our options from millions of possibilities to at most 26 main intervals (one per letter).
We stretch each interval to fully cover all letters inside it, drop any invalid ranges, 
and greedily select the maximum number of non-overlapping substrings.

"""

# Greedy: First we find the starting and ending index for each letter to set base boundaries. 
#   Then we expand each boundary to fully include any letters inside it,
#   but discard the boundary if it forces us to expand backward past the original start. 
#   Finally we sort the valid boundaries by their end positions and greedily select non overlapping substrings.

# Time Complexity: O(N) - Finding initial character boundaries takes O(N).
#   Expanding, sorting, and selecting at most 26 intervals takes O(1) time for at most 26 letters.
# Space Complexity: O(N) - The ans array stored at most the whole given string(all the rest are having const space)
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        index = [[-1,-1] for _ in range(26)]

        # extending the length in order to match the condition
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if index[idx][0] == -1:
                index[idx][0] = i
            index[idx][1] = i
        
        valid = []
        #extanding the lenght in order to match the condition
        for i in range(26):
            if index[i][0] == -1:
                continue

            left,right = index[i]
            j = left
            is_valid = True

            while j <= right :
                idx = ord(s[j]) - ord('a')
                if index[idx][0] < left: # extending left means the earlier character will cover this entire valid range anyway
                    is_valid = False
                    break
                if index[idx][1] > right:
                    right = index[idx][1]
                j += 1
            
            if is_valid:# we can add it
                valid.append([left,right])

        
        end = -1
        ans = []
        valid.sort(key = lambda x: x[1])
        # by sorting the end points we guarantee to take the maximum subset with minimum length        for left,right in valid:
            if left > end:
                ans.append(s[left:right +1])
                end = right
        
        return ans 

        