import unittest

from main import Node, Stack


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node_1 = Node(5)

    def test_node_1(self):
        self.assertEqual(self.node_1.data, 5)
        self.assertEqual(self.node_1.next_node, None)

    def test_node_2(self):
        self.node_2 = Node('a', self.node_1)
        self.assertEqual(self.node_2.next_node, self.node_1)


class TestStack(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.top = None

    def setUp(self):
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')

    def test_push(self, data):
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

        self.assertEqual(self.top.next_node.next_node.data, (None, 'data1', 'data2', 'data3'))


if __name__ == '__main__':
    unittest.main()
