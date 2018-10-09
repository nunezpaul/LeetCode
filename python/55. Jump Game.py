class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        """
        # Edge case check
        len_nums = len(nums)
        if len_nums < 2:
            return True

        curr_idx, max_idx = [0] * 2

        while curr_idx < len_nums:
            # Early stop if we can hop to last idx
            if max_idx >= len_nums-1:
                return True

            curr_val = nums[curr_idx]
            if curr_val > 0:
                # Move to the next number since doesn't matter
                max_idx = max(nums[curr_idx] + curr_idx, max_idx)
                curr_idx += 1
            elif max_idx > curr_idx:
                # Encountered a 0 but can hop over it
                max_idx = max(nums[curr_idx] + curr_idx, max_idx)
                curr_idx += 1
            else:
                # Encountered a 0 but can't hop over it
                return False

        return False
