class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        h = 0
        anc = 0
        for i in prices:
            if i > h:
                h = i
                if h - l > anc:
                    anc = h - l

            if i < l:
                l = i
                h = i

        return anc
