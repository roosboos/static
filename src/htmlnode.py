class HTMLNode():
   def __init__(self, tag=None, value=None, children=None, props=None):
       self.tag = tag
       self.value = value
       self.children = children
       self.props = props
    
   def to_html(self):
       raise NotImplementedError
    
   def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        props_strings = []
        for key, value in self.props.items():
            props_strings.append(f' {key}="{value}"')
        
        return "".join(props_strings)
   
   def __repr__(self):
       return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # LeafNode doesn't allow children, so we pass None as children
        super().__init__(tag, value, None, props)
        # Ensure value is required
        if value is None:
            raise ValueError("LeafNode must have a value")

    def to_html(self):
        # If value is empty, raise ValueError
        if not self.value:
            raise ValueError("LeafNode must have a value")
        
        # If no tag, return raw text
        if self.tag is None:
            return self.value
        
        # Return HTML with tag, props and value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"