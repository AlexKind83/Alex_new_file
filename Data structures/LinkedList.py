# Node - узел
# head - головной
# data - данные
# next - следующий (далее)
# current - текущий (настоящий)
# search - поиск

# create - создать


# get - получить
# set - набор
# coord - координировать
# add - добавлять
# to - к
# change - менять

class Node:
    def __init__(self, data):
        self.data = data
        self.new = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.new:
            current = current.new
        current.new = Node(data)

    def get_information(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.new

    def search(self, target):
        current = self.head
        while current.new:
            if current.data == target:
                return True
            else:
                current = current.new
        return False


a_list = LinkedList()
a_list.append('first_list')
a_list.append('two_list')
a_list.append('three_list')
a_list.get_information()
print()

print(a_list.search('first_list'))
print(a_list.search('two_list'))
print(a_list.search('three'))


#

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node
#
#     def pop(self):
#         if self.head is None:
#             raise IndexError("Выскакивает из пустой стопки")
#         poppednode = self.head
#         self.head = self.head.next
#         return poppednode.data
#
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# for i in range(3):
#     print(stack.pop())
