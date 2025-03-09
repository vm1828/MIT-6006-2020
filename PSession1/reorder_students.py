from Linked_List_Seq import *


def reorder_students(L: Linked_List_Seq) -> None:
    '''
    Input:  L    | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
        - any additional linked list nodes
        - any other non-constant-sized data structures
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    if len(L) <= 2:
        return

    mid = L.head.later_node(len(L) // 2 - 1)  # Middle node

    prev = None
    curr = mid.next
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    mid.next = prev  # Reattach reversed half to the first half
