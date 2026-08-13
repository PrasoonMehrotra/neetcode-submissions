class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_dict = {}

        for num in nums:
            unique_dict[num] = unique_dict.get(num, 0) + 1
     
        sorted_dict=sorted(unique_dict.items(),key = lambda item: item[1], reverse=True)
        result=[]
        for i in range(k):
            result.append(sorted_dict[i][0])
        return result