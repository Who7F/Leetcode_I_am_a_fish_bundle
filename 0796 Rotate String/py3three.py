class Solution:
    def build_lps(self, pattern):
        lps = [0] * len(pattern)

        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

        return lps

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        text = s + s
        lps = self.build_lps(goal)

        i = 0
        j = 0

        while i < len(text):
            if text[i] == goal[j]:
                i += 1
                j += 1

                if j == len(goal):
                    return True

            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1

        return False
