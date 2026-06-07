class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):

            if i == len(nums):
                res.append(subset.copy())
                return

            for n in nums:

                if n in subset:
                    continue

                subset.append(n)

                dfs(i + 1)

                subset.pop()

        dfs(0)
        return res
            