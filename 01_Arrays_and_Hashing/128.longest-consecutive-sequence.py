#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        
        longest = 0
        for x in nums:
            length = 1

            # Without this if statement, 
            # the program times out in some test cases.
            # It is important to think about reducing the number of search iterations.
            if x - 1 not in s:                 
                while x + length in s:
                    length += 1
                if length > longest:
                    longest = length
                
        return longest
        
# @lc code=end

