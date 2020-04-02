"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""



class Solution:
    def isHappy(self, n: int) -> bool:

        list1 = []
        while True:
            result = self.to_find_squares(n)
            if result == 1:
                return True
            else:
                if result in list1:
                    return False
                list1.append(self.to_find_squares(n))
                n = result

    def to_find_squares(self, n):
        out = 0
        string1 = str(n)
        for ele in string1:
            out += int(ele) ** 2
        return out



if __name__ == '__main__':
    nums = 2
    test = Solution()
    ans = test.isHappy(nums)
    print(ans)
