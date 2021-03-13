# Length of a linked list, ITERATIVE METHOD  IMPORTANT ! ITERATION

    def len_iterative(self):
        count    = 0 
        cur_node = self.head
        while cur_node:
            count   += 1
            cur_node = cur_node.next
        return count
    # Lenght of a list RECURSIVE METHOD

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)