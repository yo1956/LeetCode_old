from typing import Dict, List
#from collections import defaultdict
import collections
#from typing import list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            freq[c].append(n)
            
        ans = []
        append_num = 0
        for i in range(len(freq) - 1, 0, -1):
            if 0 < len(freq[i]):
                for n in freq[i]:
                    ans.append(n)
                    append_num += 1
                    if append_num == k:
                        return ans

def main():
    sol = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    ans = sol.topKFrequent(nums, k)
    print(ans)
    
if __name__ == "__main__":
    main()