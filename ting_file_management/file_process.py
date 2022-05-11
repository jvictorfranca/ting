import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    isInQueue = False
    for index in range(len(instance)):
        print(instance.search(index))
        if instance.search(index) == path_file:
            isInQueue = True
    if not isInQueue:
        textLines = txt_importer(path_file)
        dictToReturn = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(textLines),
            "linhas_do_arquivo": textLines
        }
        instance.enqueue(path_file)
        print(dictToReturn, file=sys.stdout)
        return dictToReturn


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
