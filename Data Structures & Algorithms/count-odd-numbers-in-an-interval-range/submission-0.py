class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        return length // 2 + (length % 2 and low % 2)
        