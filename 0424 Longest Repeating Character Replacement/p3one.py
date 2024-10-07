class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_map = {}
        low, high = 0, len(s) 
        anc, max_cnt = 0, 0
        for i in range(high):
            my_map[s[i]] = my_map.get(s[i], 0) + 1
            max_cnt = max(max_cnt, my_map[s[i]])

            if i - low + 1 - max_cnt > k:
                my_map[s[low]] -= 1
                low += 1

            anc = max(anc, i - low + 1)

        return anc