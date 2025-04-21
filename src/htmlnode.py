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