# https://leetcode.com/problems/longest-palindromic-substring/

def add_hash(s):
  ns = ''
  for c in s:
    ns += f'#{c}'
  ns += '#'
  return ns

def get_palindrome_length(arr, i, length):
  start = i - length - 1
  end = i + length + 1

  try:
    while arr[start] and arr[end]:
      if arr[start] == arr[end]:
        length += 1
        start -= 1
        end += 1
      else:
        break
  except IndexError:
    pass

  return length
    
class Solution:

    def longestPalindrome(self, s):
        
        s = add_hash(s)
        lengths = [0] * len(s)
        max_index = 0
        center = 0
        right_boundary = 0

        for i, c in enumerate(s):
          mirror = lengths[(center * 2) - i]

          if i < right_boundary:
            lengths[i] = min(mirror, right_boundary - i)

          lengths[i] = get_palindrome_length(s, i, lengths[i])

          if i + lengths[i] > right_boundary:
            center = i
            right_boundary = i + lengths[i]

          if lengths[max_index] < lengths[i]:
            max_index = i

        start = max_index - lengths[max_index]
        end = max_index + lengths[max_index] + 1

        return s[start:end].replace('#', '')
        
