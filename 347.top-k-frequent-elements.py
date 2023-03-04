#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = defaultdict(int) # default-factoryを指定しないと要素アクセス時にKeyError
        
        for num in nums:
            d[num] += 1
            
        ans = []
        while(k > 0):
            max_key = 0
            max_val = 0
            for key,val in d.items():
                if max_val < val:
                    max_val = val
                    max_key = key 
            ans.append(max_key)
            del d[max_key]
            k -= 1
            
        return ans

            
# @lc code=end

