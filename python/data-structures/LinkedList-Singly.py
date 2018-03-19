"""
Singly Linked List
    Each Node has a single link to the next Node in the list.
"""

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.get_data

    def set_next(self, new_node):
        self.next_node = new_node

    def set_data(self, new_data):
        self.data = new_data


class LinkedList():

    def __init__(self):
        self.head = None  # initialized head of the linked list
        self.tail = None  # initialized tail of the linked list
        self.size = 0     # initialized size of the linked list

    def add_node_head(self, data):
        new_node = Node(data, self.head) # new node being added to the list
        if(self.size == 0):
            self.tail = new_node # set tail when first node in list
        self.head = new_node
        self.size += 1 # linked list gets bigger
        return True

    def add_node_tail(self, data):
        new_node = Node(data, None) # new node being added to the list
        if(self.size == 0):
            self.head = new_node  # set head when first node in list
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.size += 1 # linked list gets bigger
        return True

    def print_nodes(self):
        curr = self.head # start from the head node
        while curr:
            print(curr.data)
            curr = curr.get_next() # move down the list of node


linked_list = LinkedList()
linked_list.add_node_tail('first tail value')
linked_list.add_node_head('Hello')
linked_list.add_node_head('World!')
linked_list.add_node_tail(1)
linked_list.add_node_head(2)
linked_list.add_node_tail(3.14)

linked_list.print_nodes()
