import unittest

from dulwich.porcelain import push

from main import Node, Stack


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node_1 = Node(5, None)

    def test_node_1(self):
        self.assertEqual(self.node_1.data, 5)
        self.assertEqual(self.node_1.next_node, None)

    def test_node_2(self):
        self.node_2 = Node('a', self.node_1)
        self.assertEqual(self.node_2.data, 'a')
        self.assertEqual(self.node_2.next_node, self.node_1)


class TestStack(unittest.TestCase):
    def test_push(self):
        s1 = Stack()
        s1.push('data1')

        self.assertEqual(s1.top.data, 'data1')


if __name__ == '__main__':
    unittest.main()
