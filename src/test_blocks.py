from blocks import markdown_to_blocks, block_to_block_type

def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )


def test__uneven_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )


# This is a ul.
md = """
- This is the first list item in a list block
- This is a list item
- This is another list item


## This is a heading.

1. Doing some ordered lists (1)
2. Ordered list li (2)
3. ol li (3)

> Quotes...
> quotes 2
> quotes 3

```
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

            And this is just a paragraph.
"""
#print(block_to_block_type(md))
#print(md)

# This is NOT a heading.
md = "######### This is a heading."
#print(block_to_block_type(md))
#print(md)
