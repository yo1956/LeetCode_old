#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start

from typing import Dict, List
from collections import defaultdict
#from typing import list

# ----- ポイント ----- #
# 1. dictのキーはhashableである必要が有る
# 2. tupleはhashableである
# 3. lというlistをtuple(l)でtupleに変換できる
# 4. listはmutable、tupleはimmutable
# https://www.lifewithpython.com/2017/12/python-tuple-list-difference.html
# 5. dictのvalues()関数は、dictのすべての値をリスト形式で表示できる
#    →list形式のOutputが求められる場合でも、最後にvalues()を使うことで
#      dictで管理するというテクニックが使える。
# 6. ord()関数は、指定した文字のUnicodeポイントを整数で返す
# 7. defaultdictは、新しいキーでも指定した型のデフォルト値が入っているものとして扱えるdict。
#    通常のdictと特にパフォーマンス面でも変わらない模様→基本defaultdictでも良さそう
# 8. count = [0] * 26 →[0,0,...,0]という記述方法が出来る

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list) # defaultdict: Keyが存在しない場合は型のデフォルト値を返すdict
        #ans = defaultdict() # 型の指定がないとKeyErrorになる

        for s in strs:
            count = [0] * 26 # [0,0,...,0]
            for c in s:
                count[ord(c) - ord("a")] += 1
            #ans[count].append(s) # listのままだとunhashable type: 'list'
            ans[tuple(count)].append(s)
        return ans.values() # ansを表示

        
# @lc code=end

