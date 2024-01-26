#solution to https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #keep track of a current sum and a maximum sum
        currentSum, maximumSum = nums[0], nums[0]

        #make sure to start from the second element
        for i in range(1, len(nums)):
            #check if at current entry, it'd be better to add the current element or just reset the sum to the current element
            currentSum = max(currentSum + nums[i], nums[i])
            #check if the new sum is bigger than the previous maxSum
            maximumSum = max(maximumSum, currentSum)

        return maximumSum