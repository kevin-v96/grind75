#solution to https://leetcode.com/problems/valid-anagram/

#if you can use counter
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
#if you can't use counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #dict would throw keyerror, defaultdict makes a value using the function you pass it. int returns 0 by default.
        dictionary = defaultdict(int)

        for letter in s:
            dictionary[letter] += 1

        for letter in t:
            dictionary[letter] -= 1

        #if there's any letters left which didn't have the same frequency in both the strings.
        for letterCount in dictionary.values():
            if letterCount != 0:
                return False
            
        return True    