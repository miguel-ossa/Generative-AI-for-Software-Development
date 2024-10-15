import unittest
from doublyLinkedList import Node, DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_add_node(self):
        self.dll.add_node(1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 1)
        self.dll.add_node(2)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.tail.data, 2)

    def test_add_duplicate_node(self):
        self.dll.add_node(1)
        with self.assertRaises(ValueError):
            self.dll.add_node(1)

    def test_traverse(self):
        self.dll.add_node(1)
        self.dll.add_node(2)
        self.dll.add_node(3)
        self.assertEqual(self.dll.traverse(), [1, 2, 3])

    def test_link_nodes(self):
        node1 = self.dll.add_node(1)
        node2 = self.dll.add_node(2)
        self.dll.link_nodes(node1, node2)
        self.assertEqual(node1.next, node2)
        self.assertEqual(node2.prev, node1)

    def test_link_nodes_with_none(self):
        node1 = self.dll.add_node(1)
        with self.assertRaises(ValueError):
            self.dll.link_nodes(node1, None)

    def test_find_node(self):
        self.dll.add_node(1)
        self.dll.add_node(2)
        self.dll.add_node(3)
        found_node = self.dll.find(2)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 2)

    def test_find_non_existent_node(self):
        self.dll.add_node(1)
        self.dll.add_node(2)
        found_node = self.dll.find(3)
        self.assertIsNone(found_node)

    def test_empty_list(self):
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(self.dll.traverse(), [])


if __name__ == '__main__':
    unittest.main()
