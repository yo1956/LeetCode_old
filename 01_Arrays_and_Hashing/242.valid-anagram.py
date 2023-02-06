#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        l = []
        for c in s:
            l.append(c)
        for c in t:
            if c in l:
                i = l.index(c)
                l.pop(i)
        if 0 < len(l):
            return False
        else:
            return True
            
        
# @lc code=end

