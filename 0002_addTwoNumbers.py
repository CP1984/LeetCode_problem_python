from typing import Optional

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to convert a list to a ListNode.
def list_to_listnode(lst):
    if not lst:
        return None
    
    head = ListNode(lst[0])  # Create the head node.
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)  # Create the next node and link it.
        current = current.next

    return head

# Function to convert a ListNode to a list.
def listnode_to_list(node):
    lst = []
    current = node
    while current:
        lst.append(current.val)  # Append the value of the current node to the list.
        current = current.next   # Move to the next node.

    return lst

# Solution class with the addTwoNumbers method.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to simplify result list creation.
        current = dummy
        carry = 0
        while (l1 != None) or (l2 != None) or (carry != 0):
            # Get the values from l1 and l2 if they are not None.
            val_1 = l1.val if l1 != None else 0
            val_2 = l2.val if l2 != None else 0
            total = val_1 + val_2 + carry  # Sum the values and the carry.
            carry = total // 10  # Calculate the new carry.

            current.next = ListNode(total % 10)  # Create the next node with the remainder.
            current = current.next  # Move to the next node in the result list.

            # Move to the next nodes in l1 and l2 if they are not None.
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        return dummy.next  # Return the next of dummy node which is the head of the result list.

if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5, 6, 9, 9, 9]
    list_2 = [4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9]
    list_node_1 = list_to_listnode(list_1)  # Convert list_1 to ListNode.
    list_node_2 = list_to_listnode(list_2)  # Convert list_2 to ListNode.
    print(listnode_to_list(list_node_1))  # Print the ListNode as a list.
    print(listnode_to_list(list_node_2))  # Print the ListNode as a list.

    ans = Solution()
    # Add the two numbers represented by list_node_1 and list_node_2.
    result = ans.addTwoNumbers(list_node_1, list_node_2)
    print(listnode_to_list(result))  # Print the result ListNode as a list.
