# ============================================================================
# Name        : 06_Group_Anagram.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================

"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
import collections




class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        # accepted solution
        groupedWords = collections.defaultdict(list)

        # Put all anagram words together in a dictionary
        # where key is sorted word
        for word in strs:
            groupedWords[''.join(sorted(word))].append(word)

        return groupedWords.values()
        """
        # create a dict
        result = {}
        # iterate the word in strs and sort them
        # it will be like eat -> ['a','e','t'] => join them as aet
        for i in strs:
            x = "".join(sorted(i))
            print(x,i)
            # append sorted word as well as unsorted one
            #'aet':['eat]
            if x in result:

                result[x].append(i)
            else:
                print(result)
                result[x] = [i]
        return list(result.values())






if __name__ == "__main__":
    test = Solution()
    string_in = ["eat", "tea", "tan", "ate", "nat", "bat"]
    out = test.groupAnagrams(string_in)
    print(out)
