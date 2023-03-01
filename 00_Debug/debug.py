from typing import Dict, List
from collections import defaultdict
#from typing import list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

def main():
    sol = Solution()
    l = ["eat","tea","tan","ate","nat","bat"]
    sol.groupAnagrams(l)
    
if __name__ == "__main__":
    main()