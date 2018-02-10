'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100"
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if a == "":
            a = "0"
        elif b== "":
            b = "0"
        
        a=int(a,2)
        b=int(b,2)
        
        return bin(a+b)[2:]
