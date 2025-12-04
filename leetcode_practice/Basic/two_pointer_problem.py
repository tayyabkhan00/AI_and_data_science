def hasCycle(head):
    slow = head                # 1
    fast = head                # 2

    while fast and fast.next:  # 3
        slow = slow.next       # 4
        fast = fast.next.next  # 5

        if slow == fast:       # 6
            return True        # 7
    
    return False               # 8
