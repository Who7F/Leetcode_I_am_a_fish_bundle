class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        start, end = 0, len(colors) - 1
        if colors[start] != colors[end]:
            return end

        base = colors[start]

        for i in range((end + 2)//2):
            if colors[start + i] != base or colors[end - i] != base:
                return end - i

        return -1
