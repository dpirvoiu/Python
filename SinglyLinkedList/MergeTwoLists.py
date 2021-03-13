 # Merge Two Sorted Linked Lists
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s      = p
                p      = s.next

            else:
                s.next = q
                s      = q
                q      = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head  = new_head
        return self.head