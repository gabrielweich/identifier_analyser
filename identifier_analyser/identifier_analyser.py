"""
    This file contains the methods related to the logic
    of the algorithm execution.
"""

import re
from collections import defaultdict
from .io_manager import format_exit, read_file, input_file

regex = re.compile("[^A-Za-z0-9_]")


# Remove special characters from the line
def clean_special_characters(line):
    return regex.sub(" ", line)


# Split the words in the line
def split_line(line):
    return line.split(" ")


# Clean empty elements from array
def remove_spaces(words):
    return filter(lambda x: x.strip(), words)


# Count identifiers in the line
def ocurrences(lines):
    ocurrences = defaultdict(list)
    for i, line in enumerate(lines):
        words = remove_spaces(split_line(clean_special_characters(line)))
        for word in words:
            ocurrences[word].append(str(i + 1))
    return ocurrences


# Executes main flow
def main():
    try:
        filepath = input_file()
        lines = read_file(filepath)
        result = ocurrences(lines)
        format_exit(result, filepath)
        return 0
    except Exception as e:
        print(f"ERRO: {e}")
        return 1
