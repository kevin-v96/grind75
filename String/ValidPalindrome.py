#solution to https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #uses regex to substitute everything in lowercase s that isn't an alphanumeric character (\W matches anything that is not alphanumeric and underscore, and _ matches underscores)
        string = re.sub(r'[\W_]+', '', s.lower())

        #check if the string is the same backwards and forward, since the third argument inside [] is the step size
        return string == string[::-1]