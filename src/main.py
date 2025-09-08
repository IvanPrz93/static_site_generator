from textnode import TextNode, TextType

def main():
    
    anchor_text = TextNode("This is a text node", TextType.LINK_TEXT, "https://www.boot.dev")

    print(anchor_text)

main()
