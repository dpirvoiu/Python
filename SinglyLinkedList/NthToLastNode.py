    ## Nth- to -last Node

    ## Solution A)
    #1) Calculate the length of the linked List
    #2) Count down from the total length until n is reached
    """
    def print_nth_from_last(self, n):
        total_len = self.len_iterative()
  
        cur = self.head 
        while cur:
            if total_len == n: ## PRIMARY METHOD
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
             return  
    """
    ## Solution B)
    ## P will point to the head node
    ## Q will point n  nodes beyond head node.
    ## When q will reach None, we’ll check where p is pointing, as that is the node we want
    def print_nth_from_last(self, n):
        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while q:
                count += 1
                if(count>=n):
                    break
                q = q.next
            
            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None
