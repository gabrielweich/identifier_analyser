
import re
import sys
from pathlib import Path
from collections import defaultdict

regex = re.compile('[^A-Za-z0-9_]')

def formatExit(ocurrences, filename):
    with open(f"{filename}-xref.txt", 'w') as f:
        for k, v in ocurrences.items():
            f.write(k + ';' + ','.join(v) + '\n')


def clean_word(word):
    return regex.sub('\t', word).strip()

def split_word(word):
    return word.split('\t')

def flatmap(words):
    return [word for l in words for word in l]

def remove_spaces(words):
    return filter(lambda x: x, words)


def read_file(name):
    path = Path(name + '.txt')

    if path.is_file():
        with path.open() as f:
            return f.readlines()
    else:
        print("ERRO: arquivo de entrada inexistente.")
        exit(1)

def ocurrences(lines):
    ocurrences = defaultdict(list)
    for i, l in enumerate(lines):
        words =  map(split_word, map(clean_word, l.split(' ')))
        flat_words = remove_spaces(flatmap(words)) 
        
        for w in flat_words:
            ocurrences[w].append(str(i + 1))
    
    return ocurrences

def main():
    name = input('Por favor, digite o nome do arquivo-texto de entrada: ')
    lines = read_file(name)

    result = ocurrences(lines)
    formatExit(result, name)
    return 0