# Node Structure

class Node:
    def __init__(self, data=None):
        self.data = data  # Store the data value of the node
        self.next = None  # Pointer to the next node in the linked list

# Singly linked list structure

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list
    
    def append(self, data):
        new_node = Node(data)  # Create a new node with the provided data
        if not self.head:  # If the list is empty, set the head to the new node
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Append the new node at the end
    
    def get(self, index):
        current = self.head
        count = 0
        while current:  # Traverse the list to find the node at the specified index
            if count == index:
                return current.data  # Return the data of the node
            count += 1
            current = current.next
        raise IndexError("Index out of range")  # Raise an error if the index is out of range
    
    def set(self, index, data):
        current = self.head
        count = 0
        while current:  # Traverse the list to find the node at the specified index
            if count == index:
                current.data = data  # Update the data of the node
                return
            count += 1
            current = current.next
        raise IndexError("Index out of range")  # Raise an error if the index is out of range

    def display(self):
        elements = []
        current = self.head
        while current:  # Traverse the list and collect data of all nodes
            elements.append(current.data)
            current = current.next
        print(elements)  # Print the collected data as a list


# Node Structure for doubly linked list

class DoublyNode:
    def __init__(self, data=None):
        self.data = data  # Store the data value of the node
        self.next = None  # Pointer to the next node in the linked list
        self.prev = None  # Pointer to the previous node in the linked list


# Doubly linked list structure

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list
    
    def append(self, data):
        new_node = DoublyNode(data)  # Create a new node with the provided data
        if not self.head:  # If the list is empty, set the head to the new node
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Append the new node at the end
            new_node.prev = current  # Set the previous pointer of the new node to the current node
    
    def get(self, index):
        current = self.head
        count = 0
        while current:  # Traverse the list to find the node at the specified index
            if count == index:
                return current.data  # Return the data of the node
            count += 1
            current = current.next
        raise IndexError("Index out of range")  # Raise an error if the index is out of range
    
    def set(self, index, data):
        current = self.head
        count = 0
        while current:  # Traverse the list to find the node at the specified index
            if count == index:
                current.data = data  # Update the data of the node
                return
            count += 1
            current = current.next
        raise IndexError("Index out of range")  # Raise an error if the index is out of range

    def display(self):
        elements = []
        current = self.head
        while current:  # Traverse the list and collect data of all nodes
            elements.append(current.data)
            current = current.next
        print(elements)  # Print the collected data as a list
