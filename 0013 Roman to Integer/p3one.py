class Solution:
    def romanToInt(self, s: str) -> int:
        my_dect = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        anc = 0
        my_len = len(s) -1
        for i in range(my_len):
            if my_dect[s[i]] < my_dect[s[i+1]]:
                anc -= my_dect[s[i]]
            else:
                anc += my_dect[s[i]]

        anc += my_dect[s[my_len]]
        
        return anc
