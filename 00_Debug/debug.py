from typing import Dict, List
#from collections import defaultdict
import collections
#from typing import list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        

def main():
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    ans = sol.groupAnagrams(strs)
    print(ans)
    
if __name__ == "__main__":
    main()