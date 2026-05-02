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

    def displayNumbers(new_ln):
        while (new_ln):
            print(new_ln.val)
            new_ln = new_ln.next

    


l1 = [2,4,3]
l2 = [5,6,4]

n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(1)

n1.next = n2
n2.next = n3


Solution.displayNumbers(n1)

# Solution.displayNumbers(Solution.addTwoNumbers(l1, l2))