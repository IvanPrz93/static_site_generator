class TextNode:
    def __init__(self, text, text_type, url= None, alt=""):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return  self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"Textnode({self.text}, {self.text_type}, {self.url})"

def main():
    textnode = TextNode("This is a text node","bold","https://www.boot.dev")
    print(repr(textnode))

main()

