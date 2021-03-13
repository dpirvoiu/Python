 # Insert After a Specific Node VALUE
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)

        new_node.next  = prev_node.next
        prev_node.next = new_node