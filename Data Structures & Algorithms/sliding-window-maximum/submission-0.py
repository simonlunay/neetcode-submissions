class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        l, r = 0, k - 1
        maxN = -10001

        while r < len(nums):
            for i in range(l, r+1):
                if nums[i] > maxN:
                    maxN = nums[i]

            res.append(maxN)
            l += 1
            r += 1

        return res
        