"""
emoji_sequences.py

This script is used to automatically generate an emoji regex
using the latest version of the Unicode spec.
"""

import requests
from collections import defaultdict
import re
from unicode_regexes import regex_char_patterns

EMOJI_SEQUENCES_DATA_URL = "https://unicode.org/Public/emoji/latest/emoji-sequences.txt"

emoji_char_class_pattern = re.compile('^([^\s;]+)[\s]*;')
emoji_multi_char_pattern = re.compile('^((?:[^\s;]+ )+[^\s;]+)[\s]*;')


def main():
    """Insert these lines into scanner.re"""
    response = requests.get(EMOJI_SEQUENCES_DATA_URL)

    if response.ok:
        emoji_char_classes = regex_char_patterns(response.text, emoji_char_class_pattern)
        emoji_multi_chars = regex_char_patterns(response.text, emoji_multi_char_pattern)

        print(f"emoji = (?:[{''.join(emoji_char_classes)}])|{'|'.join(emoji_multi_chars)};")

if __name__ == "__main__":
    main()
