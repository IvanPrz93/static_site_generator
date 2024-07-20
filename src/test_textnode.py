import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "www.boot.dev")
        self.assertEqual(node, node2)

    def test_different_urls(self):
        node1 = TextNode("This is a text node", "bold", "www.boots.com")
        node2 = TextNode("This is a text node", "bold", "www.bears.com")
        self.assertNotEqual(node1, node2)

    def test_different_text_types(self):
        node1 = TextNode("This is a text node", "bold", "www.boots.com")
        node2 = TextNode("This is a text node", "italic", "www.boots.com")
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        node1 = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
