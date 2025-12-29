import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    """
    def test_default_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_all_params_eq(self):
        node = HTMLNode(
            "test-tag", "test-value", "test-child",
            {"href": "http://google.com", "target": "_blank"})
        node2 = HTMLNode(
            "test-tag", "test-value", "test-child",
            {"href": "http://google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def _test_unequal(self):
        node = HTMLNode(
            "test-tag", "test-value")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_props_to_html(self):
        node = LeafNode("a", "Click Me!", {"href": "http://somesite.biz"})
        self.assertEqual(node.to_html(), '<a href="http://somesite.biz">Click Me!</a>')

    def test_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    """

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("placeholder text", TextType.LINK, "http://notasite.xyz")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "placeholder text")
        self.assertEqual(html_node.props, {"href": "http://notasite.xyz"})

    def test_img(self):
        node = TextNode("img description", TextType.IMAGE, "http://dummyimage.tuv")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "http://dummyimage.tuv", "alt": "img description"})



