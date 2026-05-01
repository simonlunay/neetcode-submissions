class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        l = 0
        print(sorted(s2[l:r]))
        while r < len(s2)+1:
            
            if(sorted(s1) == sorted(s2[l:r])):
                return True
            else:
                l += 1
                r += 1
        return False
