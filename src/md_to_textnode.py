import re
from regex import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        delimiter_count = 0
        for ch in node.text:
            if ch == delimiter:
                delimiter_count += 1
        if delimiter_count % 2 != 0:
            raise Exception("Invalid markdown syntax: Mismatched delimiters")
        splits = node.text.split(delimiter)
        for i, part in enumerate(splits):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text is None or node.text == "":
            continue
        current_text = node.text
        extracted = extract_markdown_images(current_text)

        for alt, url in extracted:
            snippet = f"![{alt}]({url})"
            sections = current_text.split(snippet, 1)
            before = sections[0]
            after = sections[1]

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            current_text = after

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text is None or node.text == "":
            continue
        current_text = node.text
        extracted = extract_markdown_links(current_text)

        for tag, url in extracted:
            snippet = f"[{tag}]({url})"
            sections = current_text.split(snippet, 1)
            before = sections[0]
            after = sections[1]

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(tag, TextType.LINK, url))
            current_text = after

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    base_node = TextNode(text, TextType.TEXT)
    proc_images = split_nodes_image([base_node])
    proc_img_link = split_nodes_link(proc_images)
    bold_nodes = split_nodes_delimiter(proc_img_link, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)

    return code_nodes
