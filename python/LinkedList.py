"""Singly Linked List - each node only has a single linke to the next node"""
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

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def add_node_head(self, data):
        new_node = Node(data, self.head)
        if(self.size == 0):
            self.tail = new_node
        self.head = new_node
        self.size += 1
        return True

    def add_node_tail(self, data):
        new_node = Node(data, None)
        if(self.size == 0):
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.size += 1
        return True

    def print_nodes(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.get_next()


linked_list = LinkedList()
linked_list.add_node_tail('first tail value')
linked_list.add_node_head('Hello')
linked_list.add_node_head('World!')
linked_list.add_node_tail(1)
linked_list.add_node_head(2)
linked_list.add_node_tail(3.14)

linked_list.print_nodes()
