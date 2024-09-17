class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        anc = ""
        min_len = len(word1)
        if min_len > len(word2):
            min_len = len(word2)
        
        for i in range(min_len):
            anc += word1[i] + word2[i] 

        anc += word1[min_len:] + word2[min_len:]

        return anc
