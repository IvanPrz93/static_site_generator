from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        html_node = block_to_html_node(block)
        block_nodes.append(html_node)
    return ParentNode("div",block_nodes)
    


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return ulist_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return olist_to_html_node(block)




def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def paragraph_to_html_node(block):
    paragraph = " ".join(block.split("\n"))
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    if block.startswith("# "):
        i = 2
        heading_tag = "h1"
    elif block.startswith("## "):
        i = 3
        heading_tag = "h2"
    elif block.startswith("### "):
        i = 4
        heading_tag = "h3"
    elif block.startswith("#### "):
        i = 5
        heading_tag = "h4"
    elif block.startswith("##### "):
        i = 6
        heading_tag = "h5"
    elif block.startswith("###### "):
        i = 7
        heading_tag = "h6"
    text = block[i:]
    children = text_to_children(text)
    return ParentNode(heading_tag, children)


def code_to_html_node(block):
    code = block[4 : -3]
    code_TextNode = TextNode(code, TextType.CODE)
    code_htmlnode = text_node_to_html_node(code_TextNode)
    return ParentNode("pre", [code_htmlnode])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line[2:])
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    lines = block.split("\n")
    html_nodes = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_nodes.append(ParentNode("li", children))
    return ParentNode("ul", html_nodes)

def olist_to_html_node(block):
    lines = block.split("\n")
    html_nodes = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_nodes.append(ParentNode("li", children))
    return ParentNode("ol", html_nodes)