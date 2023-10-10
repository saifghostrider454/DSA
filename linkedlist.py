class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):

        # Empty Linked List
        self.head = None
        # no of nodes in the LL
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):

        # new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        # reassign head
        self.head = new_node

        # increment n
        self.n = self.n + 1

    def __str__(self):

        curr = self.head

        result = ''

        while curr is not None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    def append(self, value):

        new_node = Node(value)

        if self.head is None:
            # empty
            self.head = new_node
            self.n = self.n + 1
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        # you are at the last node
        curr.next = new_node
        self.n = self.n + 1

    def insert_after(self, after, value):

        new_node = Node(value)

        curr = self.head

        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next

        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return 'Item not found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):

        if self.head is None:
            # empty
            return 'Empty LL'

        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):

        if self.head is None:
            # empty
            return 'Empty LL'

        curr = self.head

        # kya linked list me 1 item hai?
        if curr.next is None:
            # head hi hog(delete from head)
            return self.delete_head()

        while curr.next.next is not None:
            curr = curr.next

        # curr -> 2nd last node
        curr.next = None
        self.n = self.n - 1

    def remove(self, value):

        if self.head is None:
            return 'Empty LL'

        if self.head.data == value:
            # you want to remove the head node
            return self.delete_head()

        curr = self.head

        while curr.next is not None:
            if curr.next.data == value:
                break
            curr = curr.next

        # 2 cases item mil gay
        # item nai mila
        if curr.next is None:
            # item nai mila
            return 'Not Found'
        else:
            curr.next = curr.next.next
            self.n = self.n - 1

    def search(self, item):

        curr = self.head
        pos = 0

        while curr is not None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1

        return 'Not Found'

    def __getitem__(self, index):

        curr = self.head
        pos = 0

        while curr is not None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return 'IndexError'
