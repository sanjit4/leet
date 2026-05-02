# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        new_val = l1.val+l2.val
        if new_val > 9:
            new_val_2 = l1.next.val+l2.next.val+1
        else:
            new_val_2 = l1.next.val+l2.next.val

            ListNode()
            
            
            # ln()
            # ln = ListNode(new_val)'

        # return new_ln

    def displayNumbers(list_node):
        while (list_node):
            print(list_node.val)
            list_node = list_node.next

    def makeLinkedList(nums):
        list_node = None
        for i in nums[-1::-1]:
            new_list_node = ListNode(i)
            new_list_node.next = list_node
            list_node = new_list_node
        return list_node


l1 = [2,4,3]
l2 = [5,6,7,8,9]

ll1 = Solution.makeLinkedList(l1)
ll2 = Solution.makeLinkedList(l2)

Solution.displayNumbers(ll2)

# Solution.displayNumbers(Solution.addTwoNumbers(ll1, ll2))