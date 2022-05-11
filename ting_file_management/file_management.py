from __future__ import print_function
from os.path import exists
import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not exists(path_file):
        message = f"Arquivo {path_file} não encontrado"
        print(message, file=sys.stderr)
        return None
    if path_file.split(".")[1] != "txt":
        message = "Formato inválido"
        print(message, file=sys.stderr)

    with open(path_file, mode="r") as f:
        answer = f.readlines()
        i = 1
        cuttedAnswer = []
        for line in answer:
            if i < len(answer):
                cuttedAnswer.append(line[0:-1])
            else:
                cuttedAnswer.append(line)
            i += 1
    return cuttedAnswer
