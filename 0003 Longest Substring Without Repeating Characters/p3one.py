class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        anc = 0
        my_dict = {}
        low = 0
        for i in range(len(s)):
            if s[i] in my_dict:
                my_dict[s[i]] += 1
            else:
                my_dict[s[i]] = 1

            while my_dict[s[i]] > 1:
                my_dict[s[low]] -= 1
                low += 1
            anc = max(anc, i - low + 1)
        return anc
