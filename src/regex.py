import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)]\((.*?)\)", text)
    return matches

# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(f"images: {extract_markdown_images(text)}")

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)]\((.*?)\)", text)
    return matches

# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(f"links: {extract_markdown_links(links)}")

