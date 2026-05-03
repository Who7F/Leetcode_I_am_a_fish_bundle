class Solution:
    def minimumDistance(self, nums):
        seen = {}
        min_dista = float('inf')

        for idx, num in enumerate(nums):
            if num in seen:
                if seen[num][0] != None:
                    min_dista = min(min_dista,  (idx - seen[num][0]) * 2)

                seen[num][0] = seen[num][1]
                seen[num][1] = idx

            else:
                seen[num] = [None, idx]


        return min_dista if min_dista != float('inf') else -1
