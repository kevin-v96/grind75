#solution to https://leetcode.com/problems/subsets/

#the only difference this has from combinations is that for combinations, you only returned/added the current answer if it was the whole length
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(output, start, subset, nums):
            #append the current subset
            output.append(subset[:])

            #for all the remaining elements
            for i in range(start, len(nums)):
                #add the element
                subset.append(nums[i])
                #explore again
                backtrack(output, i + 1, subset, nums)
                #remove the element so that the next iteration of the for loop can explore solutions with dfs of other elements
                subset.pop()

        backtrack(output, 0, [], nums)
        return output