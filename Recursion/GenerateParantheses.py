#solution to https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recursion(left, right, currentCombination):
            if left == right == n:
                result.append(currentCombination)
                return

            #if there's capacity for left paranthesis left, add one and recurse
            if left < n:
                recursion(left + 1, right, currentCombination + '(')

            #if there's capacity for right paranthesis left (be it 1, 2...upto n parantheses that we've opened, add a right one and recurse)
            if left > right:
                recursion(left, right + 1, currentCombination + ')')

        recursion(0,0,'')
        return result