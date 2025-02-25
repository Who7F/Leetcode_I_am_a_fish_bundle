class Solution:
    def getCobinations(self, digits, letter_map, res, sol, index):
        if index == len(digits):
            res.append("".join(sol))
        else:
            for i in letter_map[digits[index]]:
                sol.append(i)
                self.getCobinations(digits, letter_map, res, sol, index + 1)
                sol.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        letter_map = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
            }
        self.getCobinations(digits, letter_map, res, [], 0)
        return res
