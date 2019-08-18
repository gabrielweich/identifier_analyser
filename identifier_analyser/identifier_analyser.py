import re
from pathlib import Path
from collections import defaultdict

regex = re.compile("[^A-Za-z0-9_]")


def format_exit(ocurrences, filename):
    with open(f"{filename}-xref.txt", "w") as f:
        for k, v in ocurrences.items():
            f.write(k + ";" + ",".join(v) + "\n")


def clean_special_characters(line):
    return regex.sub(" ", line)


def split_line(line):
    return line.split(" ")


def remove_spaces(words):
    return filter(lambda x: x.split(), words)


def file_is_valid(path):
    return path.is_file()


def input_file():
    name = input("Por favor, digite o nome do arquivo-texto de entrada: ")
    path = Path(name + ".txt")
    return name, path


def read_file(path):
    with path.open() as f:
        return f.readlines()


def ocurrences(lines):
    ocurrences = defaultdict(list)
    for i, line in enumerate(lines):
        words = remove_spaces(split_line(clean_special_characters(line)))
        for word in words:
            ocurrences[word].append(str(i + 1))
    return ocurrences


def main():
    name, path = input_file()
    if file_is_valid(path):
        lines = read_file(path)
        result = ocurrences(lines)
        format_exit(result, name)
        return 0
    else:
        print("ERRO: arquivo de entrada inexistente.")
        return 1
