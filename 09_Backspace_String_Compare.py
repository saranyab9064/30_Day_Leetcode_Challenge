# ============================================================================
# Name        : 09_Backspace_String_Compare.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""
class Solution(object):

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        str1 = []
        str2 = []

        for i in range(0,len(S)):
            if S[i] != "#":
              str1.append(S[i])
            elif len(str1)!= 0:
               str1.pop()
        print(str1)

        for i in range(0, len(T)):
            if T[i] != "#":
                str2.append(T[i])
            elif len(str2) != 0:
                str2.pop()
        print(str2)

        if str1 == str2:
            return True
        else:
            return False



if __name__ == "__main__":
    test = Solution()
    S = "a#c"
    T = "b"
    out = test.backspaceCompare(S,T)
    print(out)
