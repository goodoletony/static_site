def extract_title(markdown):
    replaced_markdown =markdown.lstrip().replace(markdown[0], "", 1)
    return_title = replaced_markdown.split("\n", 1)
    if replaced_markdown[0].strip() == "#":
        raise Exception("Title not present.")
    else:
        print(return_title[0])
        return return_title[0].strip()
