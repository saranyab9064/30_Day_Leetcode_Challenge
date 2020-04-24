# ============================================================================
# Name        : 23_Bitwise_AND_of_Numbers_Range.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given a range [m, n] where 0 <= m <= n <= 2147483647,
return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = m
        for j in range(m,n+1):
            result = result & j
        return result


if __name__ == "__main__":
    Input1 = 0
    Input2 = 1
    test = Solution()
    out = test.rangeBitwiseAnd(Input1, Input2)
    print(out)
