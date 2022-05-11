from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    list_to_return = []
    for fileIndex in range(len(instance)):
        text_lines = txt_importer(instance.search(fileIndex))
        file_dict = {
            "palavra": word,
            "arquivo": instance.search(fileIndex),
            "ocorrencias": []
        }
        i = 0
        for line in text_lines:
            if word.lower() in line.lower():
                to_append = {"linha": i + 1}
                file_dict["ocorrencias"].append(to_append)
            i += 1
        list_to_return.append(file_dict)
    return(list_to_return)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


alou = Queue()
alou.enqueue("statics/arquivo_teste.txt")
exists_word("levantamento", alou)
