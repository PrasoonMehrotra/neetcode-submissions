class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap=defaultdict(int)

        for n in nums:
            hmap[n] = 1 + hmap.get(n,0)

        sorted_items=sorted(hmap.items(), key=lambda item:item[1], reverse=True)
        res =[]
        for i in range(k):
            res.append(sorted_items[i][0])

        return res

