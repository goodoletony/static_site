class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == "":
            return ""
        else:
            f_props = ""
            for key, value in self.props.items():
                f_props += f'{key}="{value}" '

            return f_props.rstrip()

    def __repr__(self):
        return (
            f"| tag: {self.tag} | value: {self.value} | children: "
            f"{self.children} | props: {self.props_to_html()} |\n"
            )


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)
        self.props = props

    def to_html(self):
        if self.props is not None:
            return (
                f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>")
        if self.value is None or self.value == "":
            print("Bad LeafNode: ", repr(self), "Type(value): ", type(self.value))
            raise ValueError
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props=None)
        self.children = children
        self.props = props

    def to_html(self):
        """
        if self.value is None or self.value == "":
            raise ValueError
        if self.tag is None or self.tag == "":
            raise ValueError("html is required for this function")
        """

        tag_family = ""
        # print(type(self.children))
        for i in range(len(self.children)):
            tag_family += self.children[i].to_html()

        return f"<{self.tag}>{tag_family}</{self.tag}>"

