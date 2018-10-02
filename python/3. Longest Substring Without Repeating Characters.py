class Solution:
    def init(self, s):
        self.string_len = len(s)
        
        if self.string_len < 1:  # Null check
            return True
        
        self.substring_len = 1
        self.max_substring_len = 1
        self.seen_chars = [s[0]]
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        This will be solved by a sliding window. 
        
        Start at the beginning.
        If char has not been encountered: 
            save char in list
            increment counter by 1
        elif char is repeated:
            stop expanding the window
            reset the list of saved char with new char
            
        If counter is larger than previously stored substring length:
            update if yes
        else:
            do not update if no
            
        check next char
        """
        if self.init(s): 
            return 0
        
        position = 1
        while position < self.string_len:
            if s[position] not in self.seen_chars:
                self.seen_chars.append(s[position])
                self.substring_len += 1 
            else:
                self.update_max_substring()  # update if needed
                self.update_lower_window(s[position])
            position += 1  # check next char
            
        # check if need to update upon exiting loop
        self.update_max_substring()  # update if needed
        
        return self.max_substring_len  
    
    def update_max_substring(self):
        self.max_substring_len = self.substring_len if self.substring_len > self.max_substring_len else self.max_substring_len
        
    def update_lower_window(self, repeated_char):
        """
        Find index of repeated char
        Keep list from that index + 1 till the end
        """
        repeated_char_index = self.seen_chars.index(repeated_char) + 1
        
        if repeated_char_index < self.substring_len:
            self.seen_chars = self.seen_chars[repeated_char_index:] + [repeated_char]
            self.substring_len -= repeated_char_index - 1
        else:  # the repeated char is at the end of the seen_chars list
            self.seen_chars = [repeated_char]
            self.substring_len = 1
            
        
