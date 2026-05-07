class Solution:
    def expectCenter(sllf, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        
        return s[left + 1:right]


    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        res = ""

        for i, _ in enumerate(s[1:], start=1):
            odd = self.expectCenter(s, i, i-1)
            even = self.expectCenter(s, i, i)

            if len(odd) > len(res):
                res = odd 
            if len(even) > len(res):
                res = even 

        return res
