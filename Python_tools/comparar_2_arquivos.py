from tkinter import filedialog as dlg
import re
from encrypter import AES_pkcs5
import json
import os
import time
from pprint import pprint
from agrupar_similariedade import *
import compara_scripts as cs



if __name__ == '__main__':
    nome_xls = 'docs/diff_comandos_VL10.xls'
    arquivo1 = cs.open_txt(dlg.askopenfilename())   
    arquivo2 = cs.open_json(dlg.askopenfilename())
    if not os.path.exists(nome_xls):
        with open(nome_xls, 'a') as f:
            f.write(f'Arquivo1;Arquivo2;Comandos não encontrados\n')

    comandos_nao_encontrados = cs.compara_comandos(arquivo1[1],arquivo2[1])
    cs.cria_planilha(arquivo1[0],arquivo2[0],comandos_nao_encontrados,nome_xls)