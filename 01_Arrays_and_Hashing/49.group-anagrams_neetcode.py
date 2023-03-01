#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start

from typing import Dict, List
from collections import defaultdict
#from typing import list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list) # defaultdict: Keyが存在しない場合は型のデフォルト値を返すdict
        #ans = defaultdict() # KeyErrorになる

        for s in strs:
            count = [0] * 26 # [0,0,...,0]
            for c in s:
                count[ord(c) - ord("a")] += 1
            #ans[count].append(s) # listのままだとunhashable type: 'list'
            ans[tuple(count)].append(s)
        return ans.values() # ansを表示

        
# @lc code=end

