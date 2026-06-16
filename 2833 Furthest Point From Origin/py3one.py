class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = 0
        ls = 0

        for m in moves:
            if m == 'L':
                ls += 1
            elif m == 'R':
                ls -= 1
            else:
                n += 1

        return abs(ls) + n
        
