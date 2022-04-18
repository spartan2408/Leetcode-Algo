class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        l = []
        max_val = sorted(dic.values())[len(dic)-k:]
        for i, j in dic.items():
            if j in max_val:
                l.append(i)

        return l
