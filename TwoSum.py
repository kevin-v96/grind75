#solution for https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        n = len(nums)

        for i in range(n):
            remainder = target - nums[i]
            if remainder in hashmap:
                return [hashmap[remainder], i]
            hashmap[nums[i]] = i
        
        return []