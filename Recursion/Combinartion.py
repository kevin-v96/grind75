#solution to https://leetcode.com/problems/combinations/description/

#using built-in function

import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations(range(1, n+1), k)
            

#without using built-in functions
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(first = 1, curr = []):
            #if this is a valid combination of k numbers, add it to the output
            if len(curr) == k:
                output.append(curr[:])
                return
            
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack()
        return output