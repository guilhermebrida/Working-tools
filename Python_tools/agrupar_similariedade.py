import os
import difflib
from tkinter import filedialog as dlg
from pprint import pprint
import re


def similaridade_strings(arquivo_a, arquivo_b):
    # Calcula a similaridade entre duas strings    
    if re.search('.*Script.Adicional.*',arquivo_a):
        arquivo_a = re.sub('Script.Adicional.','',arquivo_a)
    return difflib.SequenceMatcher(None, arquivo_a.upper(), arquivo_b.upper()).ratio()



def agrupar_arquivos_parecidos(pasta, limiar_similaridade=0.60):
    arquivos = os.listdir(pasta)
    
    grupos = []
    grupo_nao_similar = []

    for arquivo_txt in arquivos:
        # if re.search('.*Script_Adicional.*',arquivo_txt):
            # arquivo_txt = re.sub('Script_Adicional_','',arquivo_txt)
            # print(arquivo_txt)
        if arquivo_txt.endswith('.txt'):
            
            arquivo_txt_base = os.path.splitext(arquivo_txt)[0]
            similaridade_maxima = 0
            arquivo_json_max_similaridade = None

            for arquivo_json in arquivos:
                if arquivo_json.endswith('.json'):
                    arquivo_json_base = os.path.splitext(arquivo_json)[0]
                    similaridade = similaridade_strings(arquivo_txt_base, arquivo_json_base)
                    # with open('similaridades.txt', 'a') as f:
                        # f.write(f'{arquivo_txt} x {arquivo_json}: {similaridade}\n')
                    

                    if similaridade >= limiar_similaridade and similaridade > similaridade_maxima:
                        similaridade_maxima = similaridade
                        arquivo_json_max_similaridade = arquivo_json

            if arquivo_json_max_similaridade:
                grupo_existente = None

                for i, grupo in enumerate(grupos):
                    if arquivo_txt in grupo or arquivo_json_max_similaridade in grupo:
                        grupo_existente = i
                        break

                if grupo_existente is None:
                    novo_grupo = [os.path.join(pasta, arquivo_txt), os.path.join(pasta, arquivo_json_max_similaridade)]
                    grupos.append(novo_grupo)
            else:
                grupo_nao_similar.append(arquivo_txt)



    for i, grupo in enumerate(grupos):
        print(f'Grupo {i + 1}:')
        for membro in grupo:
            print(f' - {membro}')
            
    

    if grupo_nao_similar:
        print('Arquivos não similares:')
        for arquivo in grupo_nao_similar:
            print(f' - {arquivo}')
    

    #json sem match
    json_in_grupos = set([os.path.basename(elemento) for sublista in grupos for elemento in sublista if elemento.endswith('.json')])
    json_in_pasta = set(arquivos for arquivos in os.listdir(pasta) if arquivos.endswith('.json'))
    json_sem_match = json_in_pasta - json_in_grupos
    # pprint(list(json_sem_match))

    return grupos,grupo_nao_similar,json_sem_match


if __name__ == '__main__':
    print(f'*****{__name__}*****{__name__}*****{__name__}*****{__name__}*****{__name__}')
    pasta = dlg.askdirectory()
    agrupar_arquivos_parecidos(pasta)