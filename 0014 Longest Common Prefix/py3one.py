class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = sorted(strs)
        anc = ""
        f = k[0]
        l = k[-1]
        
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                return anc
            anc += f[i]
        return anc