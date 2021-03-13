
# Delete Head Node BY VAALUE

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node  = None

        # Delete Node other than the Head BY VAALUE
        prev = None
        while cur_node and cur_node.data != key:
            prev     = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node  = None