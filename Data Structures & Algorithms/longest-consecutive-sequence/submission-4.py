class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new = set(nums)
        longest = 0

        for n in new:
            if (n -1) not in new:
                length = 1
                while (n + length) in new:
                    length +=1
                longest = max(length, longest)

        return longest
                

