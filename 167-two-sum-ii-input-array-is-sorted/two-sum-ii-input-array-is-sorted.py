class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in num_dict:
                return [num_dict[complement]+1, i+1]
            num_dict[numbers[i]] = i