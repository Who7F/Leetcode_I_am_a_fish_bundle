class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {} 
        res = 0 

        for num in nums: 
            if num - 1 in hashMap: 
                hashMap[num] = hashMap[num - 1] + 1
            else: 
                hashMap[num] = 1 

            tempMax = hashMap[num]
            n = 1 
            
            while num + n in hashMap: 
                hashMap[num + n] = hashMap[num] + n
                tempMax = hashMap[num + n]
                n += 1

            res = max(res, tempMax) 
            
        return res