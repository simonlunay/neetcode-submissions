class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        detect = {}

        for i, n in enumerate(nums):
            if n in detect:
                return n
            else:
                detect[i] = n

        return n

