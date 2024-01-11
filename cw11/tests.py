from singlelist import SingleList, Node
import unittest


class TestSingleList(unittest.TestCase):
    def test_remove_tail(self):
        list1 = SingleList()
        for i in range(10):
            list1.insert_head(Node(i))
            self.assertEqual(list1.length, i + 1)
        self.assertEqual(list1.length, 10)

        for i in range(10):
            list1.remove_tail()
            self.assertEqual(list1.length, 9 - i)
        self.assertRaises(ValueError, list1.remove_tail)

    def test_clear(self):
        list1 = SingleList()
        list1.clear()

        list1.insert_tail(Node(1))
        self.assertEqual(list1.length, 1)
        list1.clear()
        self.assertEqual(list1.length, 0)

        for i in range(10):
            list1.insert_head(Node(i))
        self.assertEqual(list1.length, 10)
        list1.clear()
        self.assertEqual(list1.length, 0)

    def test_join(self):
        list1 = SingleList()
        list2 = SingleList()

        list1.join(list2)
        self.assertEqual(list1.__str__(),"")
        self.assertEqual(list2.__str__(),"")

        list2.insert_head(Node(1))
        list2.insert_head(Node(2))
        list2.insert_head(Node(3))
        list1.join(list2)
        self.assertEqual(list1.__str__(),"3,2,1")
        self.assertEqual(list2.__str__(),"")
        self.assertEqual(list1.length,3)
        self.assertEqual(list2.length,0)

        list2.join(list1)
        self.assertEqual(list1.__str__(),"")
        self.assertEqual(list2.__str__(),"3,2,1")
        self.assertEqual(list1.length,0)
        self.assertEqual(list2.length,3)

        list2.clear()
        list1.insert_head(Node(1))
        list1.insert_head(Node(2))
        list2.insert_head(Node(1))
        list2.insert_head(Node(2))
        list1.join(list2)
        self.assertEqual(list1.__str__(),"2,1,2,1")
        self.assertEqual(list2.__str__(),"")
        self.assertEqual(list1.length,4)
        self.assertEqual(list2.length,0)
unittest.main()
