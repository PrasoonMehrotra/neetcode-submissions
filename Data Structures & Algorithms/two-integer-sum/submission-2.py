class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i, num in enumerate(nums):
            d[num]=i

        for i, n in enumerate(nums):
            diff=target - n
            if diff in d.keys() and d[diff]!= i:
                return [i, d[diff]]
        return []

        