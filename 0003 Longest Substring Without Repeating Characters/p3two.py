class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        anc = 0
        my_dict = {}
        low = 0
        # +1 cancel each other out. Needed because of gotcha
        for i in range(len(s)):
            if s[i] in my_dict and my_dict[s[i]] >= low:
                low = my_dict[s[i]] + 1
            
            my_dict[s[i]] = i
            anc = max(anc, i - low + 1)
        return anc
