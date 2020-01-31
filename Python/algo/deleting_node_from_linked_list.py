
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def deleteList(self):
        current = self.head

        while current:
            prev = current.next
            del current.data
            current = prev

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def show(self):
        current = self.head

        while current:
            print  (current.data)
            prev = current.next
            current = prev

if __name__ == '__main__':

    links = LinkedList()

    links.push(1)
    links.push(2)
    links.push(3)
    links.push(10)
    links.push(12)
    links.push(15)

    print("before")
    links.show()

    links.deleteList()
    print("after")
    links.show()