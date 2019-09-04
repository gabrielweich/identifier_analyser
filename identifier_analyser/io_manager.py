"""
    This file contains the methods related to input
    and output of data.
"""

import os
import sys
from pathlib import Path


# Receives the filename by args or by input
def input_file():
    args = sys.argv
    name = ''
    if (len(args) > 1):
        name = args[1]
    else:
        name = input("Por favor, digite o nome do arquivo-texto de entrada: ")
    return Path(name)


# Reads the content in file
def read_file(path):
    try:
        with path.open() as f:
            return f.readlines()
    except Exception:
        raise Exception('arquivo de entrada inexistente.')


# Writes the result to file
def format_exit(ocurrences, filepath):
    filename, extension = os.path.splitext(filepath)
    try:
        with open(f"{filename}-xref{extension}", "w") as f:
            for k, v in ocurrences.items():
                f.write(k + ";" + ",".join(v) + "\n")
    except Exception:
        raise Exception("erro ao salvar arquivo de saída.")
