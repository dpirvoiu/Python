#print List IMPORTANT ! ITERATION
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # APPEND We define a new node using our Node Class
    def append(self, data):
        new_node = Node(data)
    # EMPTY LINKED LIST . The head pointer doesn’t point to anything at all, and therefore there is no node in the linked list.
        if self.head is None:
            self.head = new_node
            return
    # NON Empty Linked List
        last_node  = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next= new_node