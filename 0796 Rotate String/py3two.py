class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        target = s + s
        if len(s) != len(goal):
            return False

        return True if goal in target else False
