"""
Problem Summary:
Return True if the strings' 's' letters can be replaced to get 't' with a 1-to-1 mapping.

Approach:
Iterate through both strings while maintain a hash map to track character mappings from 's' to 't':
"""
# Using hash solution.
# Time Complexity: O(N * 26) - the lookup in dictionary values .
# Space Complexity: O(26) - space used by the hash map.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        for ch1, ch2 in zip(s,t):
            if ch1 in map:
            #verify it consistently maps to 'ch2'
                if map[ch1] != ch2:
                    return False
            #ensure 'ch2' hasn't already been mapped to another character in 's'
            elif ch2 in map.values():
                return False
            #mapping characters from 's' to 't' 
            map[ch1] = ch2

        return True #went good