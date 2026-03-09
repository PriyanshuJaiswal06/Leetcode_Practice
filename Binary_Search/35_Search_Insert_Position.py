#Given a sorted array of distinct integers and a target value, 
#return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        guess = (high + low)//2
        guess_count = len(nums)
        while nums[guess] != target and guess_count > 0:
            guess_count -= 1
            if nums[guess] > target:
                high = guess - 1
            else:
                low = guess + 1
            guess = (high + low)//2
        if guess_count == 0:
            return guess + 1
        return guess