def mergeTwoLists(list1, list2):
    dummy = ListNode()      # 1
    tail = dummy            # 2
    
    while list1 and list2:  # 3
        if list1.val < list2.val:   # 4
            tail.next = list1       # 5
            list1 = list1.next      # 6
        else:
            tail.next = list2       # 7
            list2 = list2.next      # 8
        
        tail = tail.next            # 9
    
    # Attach the remaining part
    tail.next = list1 if list1 else list2   # 10
    
    return dummy.next              # 11
