from typing import Dict, List
from collections import defaultdict
#from typing import list

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = defaultdict(int)
        
        for num in nums:
            d[num] += 1
            
        ans = []
        while(k > 0):
            max_key = 0
            max_val = 0
            for k,v in d.items():
                if max_val < v:
                    max_val = v
                    max_key = k 
            ans.append(max_key)
            del d[max_key]
            k -= 1
            
        return ans

def main():
    sol = Solution()
    l = [1,1,1,2,2,3]
    k = 2
    sol.topKFrequent(l, k)
    
if __name__ == "__main__":
    main()