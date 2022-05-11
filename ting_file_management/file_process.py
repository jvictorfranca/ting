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
    if len(instance) == 0:
        message = "Não há elementos"
        print(message, file=sys.stdout)
        return None
    removed = instance.search(0)
    instance.dequeue()
    message = f"Arquivo {removed} removido com sucesso"
    print(message, file=sys.stdout)
    return message


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if position >= len(instance):
        message = "Posição inválida"
        print(message, file=sys.stderr)
        return None
    path_file = instance.search(position)
    textLines = txt_importer(path_file)
    dictToReturn = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(textLines),
        "linhas_do_arquivo": textLines
    }
    print(dictToReturn, file=sys.stdout)
    return dictToReturn
