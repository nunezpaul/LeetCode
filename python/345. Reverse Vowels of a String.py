'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = 'aeiouAEIOU'
       
        s = list(s)
        vowel_stack = []
        const_stack = []
        lettr_stack = []
        reconstruct = []
        #1 for vowels and 0 for not
        for i in s:
            if i in vowels:
                vowel_stack.append(i)
                lettr_stack.append(1)
                
            else:
                const_stack.append(i)
                lettr_stack.append(0)
        
        #reversing stack
        const_stack = const_stack[::-1]
        
        #reconstructing the word
        for i in lettr_stack:
            if i == 1:
                reconstruct.append(vowel_stack.pop())
            
            else:
                reconstruct.append(const_stack.pop())
        
        return ''.join(reconstruct)
                
