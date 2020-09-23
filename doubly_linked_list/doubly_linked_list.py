"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.head
        new_node = ListNode(value, None, self.head)
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return self.head
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return null
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail == None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.tail
        else:
            new_node = ListNode(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return self.tail
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail == None:
            return None
        if self.tail == self.head:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.tail.get_value()
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head == node:
            return self.head
        elif self.tail == node: 
            self.tail = self.tail.prev
            self.tail.next = None
            node.next = self.head
            node.prev = None
            self.head = node
            return self.head
        else:
            value = self.head
            while(value != node):
                value = value.next
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head
            self.head.prev = node
            self.head = node
            return self.head
            
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head == node:
            node.prev = self.tail
            self.tail.next = node
            self.head = node.next
            self.head.prev = None
            self.tail = node
            return self.tail
        elif self.tail == node: 
            return self.tail
        else:
            value = self.head
            while(value != node):
                value = value.next
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            return self.tail

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head == node and (self.head == self.tail):
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.tail == node: 
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
        elif self.head == node:
            self.head = node.next
            self.head.prev = None
            self.length -=1
        else:
            value = self.head
            while(value != node):
                value = value.next
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = 0
        value = self.head
        while(value != None):
            if value.value > max:
                max = value.value
            value = value.next
        return max