class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for x in nums:
            s.add(x)
        if len(s) == len(nums):
            return False
        else:
            return True