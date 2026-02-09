class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(char.lower() for char in s if char.isalnum())
        
        return word == word[::-1]