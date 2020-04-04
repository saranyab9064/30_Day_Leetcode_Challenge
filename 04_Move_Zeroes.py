"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # count no of zeroes in the list
        count = 0
        for element in range(len(nums) - 1):
            if nums[element] == 0:
                count = count + 1
        print(nums,count)
        # remove zeroes from the list
        for rem in range(0,count):
            nums.remove(0)
        print(nums)
        # add zeroes to the list
        for i in range(0,count):
            nums.append(0)
        return nums



if __name__ == '__main__' :
    n = [0,1,0,3,12]
    Sum = Solution()
    res = Sum.moveZeroes(n)
    print(res)
