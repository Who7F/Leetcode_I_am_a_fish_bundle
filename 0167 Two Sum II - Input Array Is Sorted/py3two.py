class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers) - 1):
            
            for j in range(i + 1, len(numbers)):
                print(i, j)
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                elif numbers[i] + numbers[j] > target:
                    break

        return[-1, -1]