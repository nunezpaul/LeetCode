'''

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

O(n) time
O(unique chars) space

'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        length = len(s)
        
        if length != len(t):
            return False
        
        s = list(s)
        t = list(t)
        
        letter_dict = {}
        
        for i in range(length):
            
            if s[i] not in letter_dict:
                letter_dict[s[i]] = 1
            
            else:
                letter_dict[s[i]] += 1
                
            if t[i] not in letter_dict:
                letter_dict[t[i]] = -1
                
            else:
                letter_dict[t[i]] -=1
                
        for i in letter_dict.values():
            if i != 0:
                return False
            
        return True
