"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # consider the first element in array as largest element
        # consider the initial ending element index is 0
        max_element = nums[0]
        ending_element = 0
        # iterate each element from index 0 to length(nums)
        for element in range(len(nums)):
            # add the ending element with iterated element
            ending_element = ending_element + nums[element]
            # check if its greater than the iterated element and assign the values
            if ending_element < nums[element]:
                ending_element = nums[element]
            # check if the max_element value is greater than sum up value and assign the values    
            if max_element < ending_element:
                max_element = ending_element
        # return the max_element_so far in the subarray        
        return max_element



if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    test = Solution()
    ans = test.maxSubArray(nums)
    print(ans)
