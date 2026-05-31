class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=len(nums)
        a=set(nums)
        y=len(a)

        if x==y:
            return False
        else:
            return True

        