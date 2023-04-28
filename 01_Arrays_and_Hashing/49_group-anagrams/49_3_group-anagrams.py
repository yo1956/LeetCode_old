#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            a = [0] * 26
            for c in s:
                a[ord(c) - ord('a')] += 1
            ans[tuple(a)].append(s)

        return ans.values()
        
# @lc code=end

