# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if both lists are None, return None
        if l1 is not None or l2 is not None:
            total_val = 0

            # add value of both nodes if they exist
            if l1 is not None:
                total_val += l1.val
            if l2 is not None:
                total_val += l2.val

            if total_val > 9:
                # get the remainder for the current node
                total_val %= 10

                # add the carry over to the next node if current node exist and has next node
                if l1 and l1.next:
                    l1.next.val += 1
                elif l2 and l2.next:
                    l2.next.val += 1
                # if there is no next node to add the carry over, make the current node and the next node with value 1(carry over)
                else:
                    return ListNode(total_val, ListNode(1))   
                
            # make the current node and call the recursive function with the next nodes of either lists if they exist, otherwise pass None
            return ListNode(total_val, self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None))    

    def displayNumbers(self, list_node):
        while (list_node):
            print(list_node.val)
            list_node = list_node.next

    def makeLinkedList(self, nums):
        list_node = None
        for i in nums[-1::-1]:
            new_list_node = ListNode(i)
            new_list_node.next = list_node
            list_node = new_list_node
        return list_node


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

ll1 = Solution().makeLinkedList(l1)
ll2 = Solution().makeLinkedList(l2)


Solution().displayNumbers(Solution().addTwoNumbers(ll1, ll2))