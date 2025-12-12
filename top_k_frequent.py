# Trishitha Dharmavaram

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        array = []
        for num, cou in count.items():
            array.append([cou,num])
        array.sort()

        result = []
        while len(result)<k:
            result.append(array.pop()[1])
        return result
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.topKFrequent([1,2,2,3,3,3],2))