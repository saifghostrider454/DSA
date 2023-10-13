class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):
        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node

        self.n = self.n + 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node

            self.n = self.n + 1
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

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

    def insert_before(self, before, value):
        new_node = Node(value)

        curr = self.head
        prev = None

        while curr is not None:
            if curr.data == before:
                new_node.next = curr
                if prev is not None:
                    prev.next = new_node
                else:
                    self.head = new_node
                self.n += 1
                return
            prev = curr
            curr = curr.next

        return 'Item not found'

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):

        curr = self.head

        if curr is None:
            return "LinkedList is empty"

        self.head = curr.next
        self.n = self.n - 1

    def pop(self):

        curr = self.head

        if curr is None:
            return "LinkedList is empty"

        if curr.next is None:
            self.delete_head()

        while curr.next.next is not None:
            curr = curr.next

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

        return "Item Not Found"

    def __getitem__(self, index):

        curr = self.head
        pos = 0

        while curr is not None:
            if pos == index:
                return curr.data

            curr = curr.next
            pos = pos + 1

        return "IndexError"

    def replace_max(self, value):

        temp = self.head
        max = temp

        while temp is not None:
            if temp.data > max.data:
                max = temp
            temp = temp.next

        max.data = value

    def sum_odds(self):

        curr = self.head
        total = 0

        if curr is None:
            return "Empty LinkedList"

        while curr is not None:
            if curr.data % 2 != 0:
                total += curr.data
            curr = curr.next

        return total

    def reverse(self):

        prev_node = None
        curr_node = self.head

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node

    def change_sent(self):

        curr = self.head

        while curr is not None:
            if curr.data == '*' or curr.data == '/':
                curr.data = ' '
                if curr.next.data == '*' or curr.next.data == '/':
                    curr.next.next.data = curr.next.next.data.upper()
                    curr.next = curr.next.next
            curr = curr.next

    def __str__(self):
        curr = self.head

        result = ""

        while curr is not None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]


if __name__ == '__main__':
    L = LinkedList()
    LL = LinkedList()
    LLL = LinkedList()
    # L.insert_head(5)
    # L.insert_head(4)
    # L.append(7)
    # L.append(5)
    # L.insert_after(5, 6)
    # L.insert_before(5, 6)
    # L.pop()
    # L.clear()
    # L.remove(5)
    # L.remove(7)
    # L.remove(10)
    # print(len(L))
    # print(L)
    # L.delete_head()
    # L.delete_head()
    # print(len(L))
    # print(L)

    # print(L.search(7))
    # print(L[3])
    # L.replace_max(8)
    # print(L)
    # print(L.sum_odds())
    # L.reverse()
    # print(L)
    #
    # L.append("T")
    # L.append("h")
    # L.append("e")
    # L.append("/")
    # L.append("*")
    # L.append("s")
    # L.append("k")
    # L.append("y")
    # L.append("*")
    # L.append("i")
    # L.append("s")
    # L.append("/")
    # L.append("/")
    # L.append("b")
    # L.append("l")
    # L.append("u")
    # L.append("e")
    # print(L)
    # L.change_sent()
    # print(L)
    LL.insert_values([2, 4, 6, 8])
    LLL.insert_values([1, 3, 5, 7])
    print(LL)
