from typing import Dict, List
#from typing import list

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict_char: list[(Dict, str)] = []
        for s in strs:
            d: Dict[str, int] = {}
            for c in s:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
            dict_char.append((d, s))
        
        ret: list[list[str]] = []
        while 0 < len(dict_char):
            d1 = dict_char.pop(0)
            ret.append([d1[1]])
            #for i, d2 in enumerate(dict_char[:]):
                #if d1[0] == d2[0]:
                #    d2_s = dict_char.pop(i)
                #    ret[-1].append(d2_s[1])
            for d2 in [d2 for d2 in dict_char if d1[0] == d2[0]]:
                dict_char.remove(d2)
                ret[-1].append(d2[1])
        
        return ret

def main():
    sol = Solution()
    l = ["","",""]
    sol.groupAnagrams(l)
    
if __name__ == "__main__":
    main()