class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        hashTable = {}
        res = 0
        for s in hashSet:
            if s not in hashTable:
                hashTable[s] = 1

        

        for s in hashSet:
            if s-1 not in hashTable:
                n = 1
                while s + n in hashTable:
                    n += 1
                if n > res:
                    res = n
   
        return res