class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def isPalindrome(word):
            return word == word[::-1]

        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return

            for j in range(i, len(s)):
                curr = s[i:j + 1]

                if isPalindrome(curr):
                    subset.append(curr)
                    dfs(j + 1)
                    subset.pop()

        dfs(0)
        return res