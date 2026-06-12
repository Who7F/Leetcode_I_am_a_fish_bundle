class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        dirtyTrick = defaultdict(list)

        for i, num in enumerate(nums):
            dirtyTrick[num].append(i)

        for dT in dirtyTrick.values():
            if len(dT) == 1:
                continue

            total = sum(dT)
            tempL = 0

            for i in range(len(dT)):
                tempR = total - tempL - dT[i]

                left = dT[i] * i - tempL
                right = tempR - dT[i] * (len(dT) - i - 1)

                res[dT[i]] = left + right

                tempL += dT[i]

            
