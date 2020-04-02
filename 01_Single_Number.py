"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h ={}
        n = len(nums)
        for i in range(n):
            if nums[i] in h:
                h[nums[i]] += 1
            else:
                h[nums[i]] = 1
        flag =  False
        for key in h:
            if h[key] == 1:
                flag = True
                return key
                break
        if flag == False:
            return -1

if __name__ == '__main__':
    nums = [3,2,3,2]
    test = Solution()
    ans = test.singleNumber(nums)
    print(ans)
