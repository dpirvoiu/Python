# SWAPING TWO NODES

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        
        # Iterate checking for the first element and keeping track of its previous node
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        # Iterate checking for the second element and keeping track of its previous node
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # check if one or both elements are missing from the list 
        if not curr_1 or not curr_2:
            return
        
        #check if either of our nodes are the head of the linked list and make the previous nodes point to the element we wish to swap
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head   = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head   = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next