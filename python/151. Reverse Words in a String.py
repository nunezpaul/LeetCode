'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = s.split()
        s = s[::-1]
        
        i = 0
        while i < len(s):
            if s[i] == ' ':
                s.pop(i)
            else:
                i+=1
        
        return ' '.join(s)
        
