# REVERSE A LINKED LIST, ITERATIVE AND RECURSIVE

    # ITERATIVE Suing the PREVIOUS AND CURRENT NODE STRATEGY
    def reverse_iterative(self):
        prev = None
        cur  = self.head
        while cur:
            nxt      = cur.next
            cur.next = prev     # THIS IS THE LINE THAT DOES THE WORK
            prev     = cur
            cur      = nxt
        self.head    = prev     # WE SET THE HEAD to PREV because prev is now the last node in the linked list.

    # RECURSIVE METHOD for REVERSE LIST

    """
    We implement the base case.
    We agree to solve the simplest problem, which in this case is to reverse just one pair of nodes.
    We defer the remaining problem to a recursive call, which is the reversal of the rest of the linked list.
    """
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt      = cur.next
            cur.next = prev
            prev     = cur
            cur      = nxt
            return _reverse_recursive(cur, prev)
        
        self.head = _reverse_recursive(cur=self.head, prev=None)