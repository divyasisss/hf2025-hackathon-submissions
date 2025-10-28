class Solution:
    def rotate(self, nums, k):
        """
        Rotates the array nums to the right by k steps.
        Do not return anything, modify nums in-place.
        """
        n = len(nums)
        k = k % n  # handle cases where k > n
        
        # Reverse the entire array
        nums.reverse()
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])
