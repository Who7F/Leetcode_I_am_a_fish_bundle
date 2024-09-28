class Solution:
    def eats_bananas(self, bite, h, piles):
        n = 0
        for p in piles:
            n += ceil(p / bite)
        return n <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        big = max(piles)
        lit = 1
        while lit < big:
            bite = lit + (big - lit) // 2
            
            if self.eats_bananas(bite, h, piles):
                big = bite
            else:
                lit = bite + 1
            

        return lit
