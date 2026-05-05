class Solution:
    def getDist(self, y, x):
        if x == 26 or y == 26: return 0
        return abs(x//6 - y//6) + abs(x%6 - y%6)

    def minimumDistance(self, word: str) -> int:

        dp = [float('inf')] * 27
        dp[26] = 0
        prev = ord(word[0]) - 65

        for c in word[1:]:
            curr = ord(c) - 65
            new_dp = [float('inf')] * 27

            for j in range(27):
                
                new_dp[j] = min(new_dp[j], dp[j] + self.getDist(prev, curr))
            
                new_dp[prev] = min(new_dp[prev], dp[j] + self.getDist(j, curr))
                     
            dp = new_dp
            prev = curr
   
        return min(dp)
