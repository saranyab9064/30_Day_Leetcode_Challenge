# ============================================================================
# Name        : 14_Perform_String_Shifts.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.



Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
"""


class Solution(object):

    def leftrotate(self, s, n):
        s = s[n:] + s[:n]
        return s

    def rightrotate(self, s, n):
        s = (s[-n:] + s[:-n])
        return s

    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        rotation = [0, 1]
        left = rotation[0]
        right = rotation[1]
        left_shift, right_shift = 0, 0
        for i in range(len(shift)):
            if shift[i][0] == left:
                left_shift = left_shift + shift[i][1]
            elif shift[i][0] == right:
                right_shift = right_shift + shift[i][1]
        print("i,l_shift,r_shift", i, left_shift, right_shift)
        if right_shift > left_shift:
            right_rotate = right_shift - left_shift
            if right_rotate > len(s):
                temp = right_rotate % len(s)
                out = self.rightrotate(s, temp)
            else:
                out = self.rightrotate(s, right_rotate)
            return out
        elif left_shift > right_shift:
            left_rotate = left_shift - right_shift
            if left_rotate > len(s):
                print("am")
                temp = left_rotate % len(s)
                print(temp)
                out = self.leftrotate(s, temp)
            else:
                out = self.leftrotate(s, left_rotate)
            return out
        elif left_shift == right_shift:
            return s


if __name__ == "__main__":
    test = Solution()
    # expected output "qpifxqgwki"
    # got output: "xqgwkiqpif"

    a = "xqgwkiqpif"
    string = [[1, 4], [0, 7], [0, 8], [0, 7], [0, 6], [1, 3], [0, 1], [1, 7], [0, 5], [0, 6]]

    out = test.stringShift(a, string)
    print(out)
