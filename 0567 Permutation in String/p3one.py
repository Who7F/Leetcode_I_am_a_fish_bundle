class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        c1, c2= [0]*26, [0]*26

        for i in range(l1):
            c1[ord(s1[i]) - 97] += 1
            c2[ord(s2[i]) - 97] += 1

        if c1 == c2:
            return True
        
        for i in range(l1, l2):
            c2[ord(s2[i]) - 97] += 1
            c2[ord(s2[i - l1]) - 97] -= 1
            if c1 == c2:
                return True

        return False