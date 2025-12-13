class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        anc = []
        anc.append(intervals.pop(0))
        n = 0

        for i in intervals:
            if anc[n][1] >= i[0]:
                if anc[n][1] < i[1]:
                    anc[n][1] = i[1]
            else:
                anc.append(i)
                n += 1

        return anc
