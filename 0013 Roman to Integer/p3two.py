class Solution:
    def romanToInt(self, s: str) -> int:
        s_replaced = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        
        my_dect = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        anc = 0
        my_len = len(s_replaced) 
        for i in range(my_len):
                anc += my_dect[s_replaced[i]]

        return anc
