class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)


        for i in range(1, len(nums) - 1):
            for j in range(i + 2):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j], dp[i] + 1)
        print(dp)
        return max(dp)