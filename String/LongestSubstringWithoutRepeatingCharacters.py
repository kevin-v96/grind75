#solution to https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #a dict that uses character as key and the position that it was last encountered at as value
        lastEncounteredIndex = {}
        #left side of the sliding window
        left = 0
        maxLength = 0

        for right in range(len(s)):
            #if the new char was previously never encountered
            if s[right] not in lastEncounteredIndex:
                #check if our maxlength needs to be updated (i.e., if current window is longer than previously longest substring)
                maxLength = max(maxLength, right - left + 1)
            else:
                #if the last position this char was encountered at is outside the window
                if lastEncounteredIndex[s[right]] < left:
                    #nothing needs to be done about the dict, just update the current window size
                    maxLength = max(maxLength, right - left + 1)
                else:
                    #if it's inside the current window, move the start of the window of unique characters to after that last index
                    left = lastEncounteredIndex[s[right]] + 1
            
            #add the new element to the dict
            lastEncounteredIndex[s[right]] = right

        return maxLength