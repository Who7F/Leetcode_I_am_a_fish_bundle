class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        hashMap = defaultdict(list)

        for i, num in enumerate(nums):
            hashMap[num].append(i)

        for h in hashMap.values():
            if len(h) == 1:
                continue

            total = sum(h)
            prf = 0

            for i in range(len(h)):
                sfx = total - prf - h[i]

                left = h[i] * i - prf
                right = sfx - h[i] * (len(h) - i - 1)

                res[h[i]] = left + right

                prf += h[i]

            
        return res

            
