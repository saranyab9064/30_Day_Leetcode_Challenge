# ============================================================================
# Name        : 16_Valid_Parenthesis_String.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        n = len(s)
        print(n)
        if n== 1:
            return False
        print(n)
        l_paren = ['(']
        r_paren = [')']
        l_count = 0
        r_count = 0
        a_count = 0

        for i in range(0, n):
            if s[i] in l_paren:
                l_count = l_count + 1
            elif s[i] in r_paren:
                r_count = r_count + 1
                if l_count < 1 and r_count == 1:
                    return False
                else:
                 continue

            elif s[i] == '*':
                a_count = a_count + 1

        print("left_count,right_count,a_count : ",l_count,r_count,a_count)
        if l_count == r_count:
            return True
        elif l_count < r_count and  a_count > r_count or a_count == r_count or a_count == l_count or a_count+l_count == r_count:
            return True
        elif r_count < l_count and a_count > l_count or a_count == r_count or a_count == r_count or a_count + r_count == l_count:

            return True
        else:
            return False
            """
        # create two stacks for open and star
        # we cannot use single stack is because whenever * comes we need to tarck of it
        # in single stack we can track opening brackets so that if closing brackets comes
        # we can simply pop it
        # position of star is extremely important
        # suppose if *( in this case we cannot convert * but in another case
        # (* , star can be converted to ) or empty string
        # we will be pushing position instead of char into stack
        open_t = []
        star = []
        open_paren = '('
        close_paren = ')'
        star_str = '*'
        # passing the entire string and processing the closed brackets
        for i in range(len(s)):
            if s[i] == open_paren:
                print(i)
                open_t.append(i)
            elif s[i] == star_str:
                star.append(i)
            else:
                if len(open_t) > 0:
                    open_t.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
        # have to balance the open brackets
        while len(open_t) > 0:
            if len(star) == 0:
                return False
            # look into index of start is greater than open
            #  then star is lying towards right hand side of opening brackets
            # (*
            elif open_t[len(open_t)-1]< star[len(star)-1]:
                open_t.pop()
                star.pop()
            else:  # *(-> will not be balanced
                return False
        return True


if __name__ == "__main__":
    test = Solution()
    arr = "*"
    out = test.checkValidString(arr)
    print(out)
