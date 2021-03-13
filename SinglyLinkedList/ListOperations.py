class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    #prepend 
    def prepend(self ,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head     = new_node
        
    # Insert After a Specific Node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)

        new_node.next  = prev_node.next
        prev_node.next = new_node

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

    ## REMOVE DUPLICATES HASH TABLE
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next # counter to traverse


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

    ## COUNT OCCURANCE iterative and recursive method

    def count_occurance_iterative(self, data):
        count = 0
        cur   = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count



"""
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(llist.print_nth_from_last(4))
 
llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)

print("Original Linked List")
llist.print_list()
print("Linked List After Removing Duplicates")
llist.remove_duplicates()
llist.print_list()

    
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()

llist.print_list()

print("\n Reversing the list")
llist.reverse_iterative()
print("\n Reversing the list RECURSIVE")
llist.reverse_recursive()
llist.print_list()
"""
#llist.prepend("D")  #Prepend Value in the list 
#llist.insert_after_node(llist.head.next, "D") #insert value after a node

#llist.delete_node("B")
#llist.delete_node("E")
#list.delete_node_at_pos(0)


  
#print("Original List")
#llist.print_list()


#llist.swap_nodes("B", "C")
#print("Swapping nodes B and C that are not head nodes")
#llist.print_list()

#llist.swap_nodes("A", "B")
#print("Swapping nodes A and B where key_1 is head node")
#llist.print_list()

#llist.swap_nodes("D", "B")
#print("Swapping nodes D and B where key_2 is head node")
#llist.print_list()

#llist.swap_nodes("C", "C")
#print("Swapping nodes C and C where both keys are same")
#llist.print_list()
