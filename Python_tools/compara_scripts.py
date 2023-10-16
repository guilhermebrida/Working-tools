from tkinter import filedialog as dlg
import re
from encrypter import AES_pkcs5
import json
import os
import time
from pprint import pprint
from agrupar_similariedade import *
import sys
import logging

def open_txt(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        content = re.sub('//.*','',content)
        comandos_vs = re.findall('>.*<|#.*', content)
        return os.path.basename(path) , comandos_vs
    except Exception as e:
        logging.error(f'Erro ao abrir o arquivo {path} {e}')

def open_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        data = json.loads(content)
        comandos = data['comandos']
        hash = data['hash']
        aes_object = AES_pkcs5(comandos)
        if data['hash'] != "":
            comandos = aes_object.decrypt(hash, comandos)
            data.update({'comandos': comandos, 'hash': ""})
        comandos = re.sub(';','\n',comandos)
        comandos_vs = re.findall('>.*<|#.*', comandos)
        return os.path.basename(path),comandos_vs
    except Exception as e:
        logging.error(f'Erro ao abrir o arquivo {path} {e}')



def compara_comandos(comandos1,comandos2):
    comandos_nao_encontrados = []
    for comando in comandos1:
        if comando not in comandos2:
                comandos_nao_encontrados.append(comando)
    
    comandos_nao_encontrados.append('<<<<>>>>')
    
    for comando2 in comandos2:
        if comando2 not in comandos1:
            comandos_nao_encontrados.append(comando2)
    
    return comandos_nao_encontrados


def cria_planilha(arquivo1,arquivo2,comandos_nao_encontrados,nome_xls):
    with open(nome_xls, 'a') as f:
        f.write(f'{arquivo1};{arquivo2};{comandos_nao_encontrados}\n')


def open_files(lista:list[list],nome_xls:str):
    for i in range(len(lista)):
        for file in lista[i]:
            if file.endswith('.txt'):
                # print(file)
                arquivo1=open_txt(file)

            if file.endswith('.json'):
                # print(file)
                arquivo2=open_json(file)
        comandos_nao_encontrados = compara_comandos(arquivo1[1],arquivo2[1])
        cria_planilha(arquivo1[0],arquivo2[0],comandos_nao_encontrados, nome_xls)
            



if __name__ == '__main__':
    # pasta = dlg.askdirectory()
    print(sys.argv)
    pasta = sys.argv[1]
    # nome_xls = 'perfis_vl1012.xls'
    nome_xls = sys.argv[2]
    list_files,nao_agrupados,json_sem_match = agrupar_arquivos_parecidos(pasta)
    open_files(list_files,nome_xls)
    with open(nome_xls, 'a') as f:
        f.write(f'\n')
        f.write(f'Nao agrupados\n')
        for i in nao_agrupados:
            f.write(f'{i}\n')
        f.write(f'\n')
        f.write(f'Json sem match\n')
        for i in json_sem_match:
            f.write(f'{i}\n')


    

    