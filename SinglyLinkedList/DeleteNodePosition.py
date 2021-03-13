 #DELETE A NODE BY POSITION
    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
     # Check if we are looking for the first item
            if pos == 0:
                self.head = cur_node.next
                cur_node  = None
                return
    # check if we are looking for a different position
            prev = None
            count = 0
            while cur_node and count != pos:
                prev      = cur_node 
                cur_node  = cur_node.next
                count     += 1

            if cur_node is None:
                return
            prev.next =  cur_node.next
            cur_node  = None