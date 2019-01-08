# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# This is a sliding window problem.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_set = set()
        start = 0
        maximum = 0
        
        for end, value in enumerate(s):
            if s[end] in my_set:
                while s[start] != s[end]:
                    my_set.remove(s[start])
                    start += 1
                my_set.remove(s[start])
                start += 1
            my_set.add(s[end])
            maximum = max(maximum, len(my_set))
            
        return maximum
