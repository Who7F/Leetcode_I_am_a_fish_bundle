class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magic = {}
        for i in magazine:
            if i in magic:
                magic[i] += 1
            else:
                magic[i] = 1

        for j in ransomNote:
            if j in magic and magic[j] > 0:
                magic[j] -= 1
            else:
                return False
        return True
        