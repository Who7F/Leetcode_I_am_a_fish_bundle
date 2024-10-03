class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        anc = 0
        my_set = set()
        low = 0
        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[low])
                low += 1
            
            my_set.add(s[i])
            anc = max(anc, i - low + 1)
        return anc
