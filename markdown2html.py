#!/usr/bin/python3
"""
Script markdown2html.py that takes an argument 2 strings
and converts a Markdown file to HTML
"""
import sys
import os
import markdown
import re


def convert_markdown_to_html(markdown_file, output_file):
    with open(markdown_file, 'r') as md_file:
        markdown_text = md_file.read()
        html_text = markdown.markdown(markdown_text)
        with open(output_file, 'w') as html_file:
            html_file.write(html_text)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)
