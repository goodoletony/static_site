import re
from enum import Enum
from htmlnode import HTMLNode
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from textnode import text_node_to_html_node
from md_to_textnode import text_to_textnodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block != ""]


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def text_to_children(text):
    children = text_to_textnodes(text)
    return [text_node_to_html_node(child) for child in children]

def regex_rm_md(pattern, target):
    split_target = [re.sub(pattern, "", split) for split in target.split("\n")]
    return split_target



def block_to_block_type(block):
    block = block.strip()
    if re.match(r'^#{1,6} +', block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        quotes = [quote.strip() for quote in block.split("\n")]
        for quote in quotes:
            if quote.startswith(">"):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("- "):
        ul_li_list = [li.strip() for li in block.split("\n")]
        for li in ul_li_list:
            if li.startswith("- "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif re.match(r'^\d+\. +', block):
        ol_li_list = [li.strip() for li in block.split("\n")]
        for li in ol_li_list:
            if re.match(r'^\d+\. +', li):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


def assign_tags(blocks):
    html_blocks = []
    for block in blocks:
        if block_to_block_type(block) == BlockType.QUOTE:
            clean_block = "\n".join(regex_rm_md(r'^> ?', block))
            print(clean_block)
            html_blocks.append(ParentNode("blockquote", text_to_children(clean_block)))
        elif block_to_block_type(block) == BlockType.UNORDERED_LIST:
            clean_block = regex_rm_md(r'^- +', block)
            split_ul = [ParentNode("li", text_to_children(line)) for line in clean_block]
            html_blocks.append(ParentNode("ul", split_ul))
        elif block_to_block_type(block) == BlockType.ORDERED_LIST:
            clean_block = regex_rm_md(r'^\d+\. +', block)
            split_ol = [ParentNode("li", text_to_children(line)) for line in clean_block]
            html_blocks.append(ParentNode("ol", split_ol))
        elif block_to_block_type(block) == BlockType.CODE:
            clean_block = "\n".join(regex_rm_md(r'```', block))
            html_blocks.append(ParentNode("pre", [LeafNode("code", clean_block)]))
        elif block_to_block_type(block) == BlockType.HEADING:
            ch = re.findall(r'^#{1,6} +', block)
            ch_count = len(ch[0].strip())
            clean_block = "\n".join(regex_rm_md(r'^#{1,6} +', block))
            html_blocks.append(ParentNode(f"h{ch_count}", text_to_children(clean_block)))
        elif block_to_block_type(block) == BlockType.PARAGRAPH:
            html_blocks.append(ParentNode("p", text_to_children(block)))

    return html_blocks


def markdown_to_html_node(markdown):
    parents = assign_tags(markdown_to_blocks(markdown))

    return ParentNode("div", parents)


md =  """
- This is the first list item in a list block
- This is a list item [with a link]("http://link-to-nowhere.swz")
- This is another list item with an inline code block `const orderId = document.getElementById("order-id").value;`


## This is a heading.

1. Doing some ordered lists (1)
2. Ordered list li (2)
3. ol li (3) ![with an image!](fotografia/photo.png)

> Quotes...
> quotes 2
> quotes 3

```
# Here is an example of some code in a code block.
i = 1
while i <= 100:
    if i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)
    i += 1
```

            And _this_ is just a **paragraph**.
"""

# print(markdown_to_html_node(md))
