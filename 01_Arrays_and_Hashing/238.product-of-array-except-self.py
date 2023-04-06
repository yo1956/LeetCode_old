#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        
        # Calculate the product of the elements preceding nums[i]
        # nums[i]の左側の要素の積を計算する
        prefix = 1
        for i, num in enumerate(nums):
            ret[i] *= prefix
            prefix *= num
        # Calculate the product of the elements following nums[i]
        # nums[i]の右側の要素の積を計算する
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= suffix
            suffix *= nums[i]
        
        return ret
        
# @lc code=end

