from copy_static import replace_public
from generation import generate_pages_recursive


def main():
    replace_public()
    generate_pages_recursive('content', 'template.html', 'public')


main()
