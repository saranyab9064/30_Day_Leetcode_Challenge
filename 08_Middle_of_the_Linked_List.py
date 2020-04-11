
# ============================================================================
# Name        : 08_Middle_of_the_Linked_List.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================

"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


Note:

The number of nodes in the given list will be between 1 and 100.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = self.head
        # find the length of the linked list
        count = 0
        while(temp):
            count = count + 1
            temp = temp.next
        # find the middle element of the linked list

        # initialise two pointer p and q
        p = head
        q = head
        while(q and q.next):
            p = p.next
            q = q.next.next
        return p



if __name__ == "__main__":
    llist = Solution()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print(llist.middleNode(ListNode(1)))
