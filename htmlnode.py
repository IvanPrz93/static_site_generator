from src.textnode import TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return " ".join([key + '="' + value + '"' for key, value in self.props.items()])

    def __repr__(self):
        return f"HTMLNode(tag={repr(self.tag)}, value={repr(self.value)}, children={repr(self.children)}, props={repr(self.props)})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("LeafNode must have a value")
                            
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        if self.tag == None:
            return self.value
        # Start with opening tag
        tag_string = f"<{self.tag}"

        # Add props if they exist
        if self.props:
            for key, value in self.props.items():
                
                tag_string += f' {key}="{value}"'
        
        # Close the opening tag, add value, and close the tag
        tag_string += f">{self.value}</{self.tag}>"
        
        return tag_string
             
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children == None:
            raise ValueError("ParentNode must have children")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        
        # Start with opening tag
        tag_string = f"<{self.tag}>"

        # Add children recursive
        for child in self.children:
            tag_string += child.to_html()
        
        # Close the tag
        tag_string += f"</{self.tag}>"
        
        return tag_string


def text_node_to_html_node(textnode):
    if textnode.text_type == "Text":
        return LeafNode(None, textnode.text)
    if textnode.text_type == "bold":
        return LeafNode("b", textnode.text)
    if textnode.text_type == "italic":
        return LeafNode("i", textnode.text)
    if textnode.text_type == "code":
        return LeafNode("code", textnode.text)
    if textnode.text_type == "link":
        return LeafNode("a", textnode.text, {"href": textnode.url})
    if textnode.text_type == "image":
        return LeafNode("img", "", {"src": textnode.url, "alt": textnode.alt_text})
    else:
        raise Exception("Unknown text node type")


def main():
    htmlnode = HTMLNode("b","This is an html node")
    print(repr(htmlnode))

main()