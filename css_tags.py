#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser(description='CSStags.')
parser.add_argument('css_file', type=argparse.FileType('r'))


def create_tag(tag_name, filename, line):
    """
    Create a ctag line for the CSS class
    """
    print('%s\t%s\t/^%s$/;"\tc' % (tag_name, filename, line))


def main():
    args = parser.parse_args()

    class_regex = re.compile('^\.([\w-]+)\s*{')

    for line in args.css_file:
        class_match = class_regex.match(line)
        if class_match:
            create_tag(class_match.group(1), args.css_file.name, class_match.group(0))


if __name__ == '__main__':
    main()
