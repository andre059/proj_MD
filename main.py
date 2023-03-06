class Node:
    """ Узел """

    def __init__(self, data, next_node=None):
        self.data = data  # тут данные
        self.next_node = next_node  # тут ссылка на следующий


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """ Добавление элемента """

        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top




n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
print(n2.next_node)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
print(stack.top.next_node.next_node.next_node.data)
