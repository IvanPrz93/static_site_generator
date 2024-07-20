import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        expected_props_html = 'href="https://www.google.com" target="_blank"'
        assert node.props_to_html() == expected_props_html, f"Expected {expected_props_html} but got {node.props_to_html()}"

    def test_repr(self):
        child_node = HTMLNode(tag='span', value='child')
        parent_node = HTMLNode(tag='div', value='parent', children=[child_node])
        expected_repr = "HTMLNode(tag='div', value='parent', children=[HTMLNode(tag='span', value='child', children=None, props=None)], props=None)"
        assert repr(parent_node) == expected_repr, f"Expected {expected_repr} but got {repr(parent_node)}"

    def test_basic_functionality(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")
        
    def test_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")
        
    def test_props_handling(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.example.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">Click me!</a>')
        
    def test_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def testParentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_textnode_to_html(self):
        pass


if __name__ == "__main__":
    unittest.main()
