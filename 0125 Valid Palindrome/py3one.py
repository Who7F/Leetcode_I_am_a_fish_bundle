class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(char.lower() for char in s if char.isalnum())
        
        l, r= 0, len(word) -1
        while r > l:

            if word[l] != word[r]: 
                return False
            
            l += 1
            r -= 1
        return True
