#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            freq[c].append(n)
            
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        
        
# @lc code=end

