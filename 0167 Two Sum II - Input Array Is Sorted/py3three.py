class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = defaultdict(list)
        for i, num in enumerate(numbers):
            if target - num not in n:
                n[num] = (i + 1)
            else:
                return [(n[target - num]), i +1]

        return[-1, -1]