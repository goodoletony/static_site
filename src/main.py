import sys
from copy_static import replace_public
from generation import generate_pages_recursive

default_basepath = "/"

def main():
    replace_public()
    base_path = default_basepath
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    generate_pages_recursive('content', 'template.html', 'docs', base_path)


main()
