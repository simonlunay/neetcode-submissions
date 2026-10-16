class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []



        def backtracking(path):
            if len(path) == len(nums):
                res.append(path[:])
                return


            
            for n in nums:
                if n in path:
                    continue


                path.append(n)
                backtracking(path)

                path.pop()
                


        backtracking([])
        return res