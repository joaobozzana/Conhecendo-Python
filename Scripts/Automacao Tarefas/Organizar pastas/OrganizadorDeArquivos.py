import os

def organize_folder():
    types = ['jpeg', 'zip'] # Escolho o tipo dos formatos que quero trabalhar

    base_path = os.path.expanduser('~') # Pego o caminho da pasta raiz
    path = os.path.join(base_path, 'Downloads') # Downloads é a pasta que quero aplicar o script
    # print(path)

    cwd = os.chdir(path)

    full_list = os.listdir(cwd) # Armazena todos os arquivos da pasta Download
    # print(full_list)

    # Essa estrutura é para criar pastas (caso não tenha) das extensões, para posteriormente alocar os arquivos da mesma extensão dentro
    for type_ in types:
        if type_ not in os.listdir():
            os.mkdir(type_)

    # Estrutura para percorrer a pasta desejada, e separar os arquivos por extensão nas suas devidas pastas
    for file in full_list:
        for type_ in types:
            if '.' + type_ in file:
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, type_, file)
                os.replace(old_path, new_path)

if __name__ == '__main__':
    organize_folder()