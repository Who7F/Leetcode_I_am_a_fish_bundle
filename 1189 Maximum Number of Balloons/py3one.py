class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        magic = Counter(text)
        balloons = Counter("balloon")
        cnt = 0
        while True:
            for k, i in balloons.items():
                magic[k] -= i
                if magic[k] < 0:
                    return cnt
            cnt += 1
