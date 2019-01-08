# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

import itertools

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not len(digits):
            return []
        
        digits = list(digits)
        letters_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        digits = [letters_map.get(digit) for digit in digits]
        return ["".join(result) for result in list(itertools.product(*digits))]
        
        
