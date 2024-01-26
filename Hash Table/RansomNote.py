#solution to https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = defaultdict(int)
        lettersToFind = len(ransomNote)

        for letter in magazine:
            dictionary[letter] += 1

        for letter in ransomNote:
            if dictionary[letter] > 0:
                dictionary[letter] -= 1
                lettersToFind -= 1
            
        return not lettersToFind