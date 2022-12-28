#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2) Solution
        #for i,x in enumerate(nums):
        #    for j, y in enumerate(nums):
        #        if i == j:
        #            continue
        #        else:
        #            sum = nums[i] + nums[j]
        #            if sum == target:
        #                return i,j
        
        # O(n) Solution
        # Applying 'in' to dict object is O(1) because it's implemented in hash table 
        mem = {}
        for i,x in enumerate(nums):
            if x in mem: 
                return mem[x],i
            else:
                mem[target-x] = i
                
        
# @lc code=end

