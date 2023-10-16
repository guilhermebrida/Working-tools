import re
from pprint import pprint 
from tkinter import filedialog as dlg
import os
import json
from encrypter import AES_pkcs5
import base64


padroes = {
    'Tracking': '>SED00.*V0.*',
    'Faixas RPM': 'SUT13,QCT27',
    'Discretas': '>SED10.*SCT78 HFFFFFFFF.*',
    'Excesso RPM': '>SED32.*V0.*',
    'Parada motor ligado': '>SED37.*V2.*',
    'Cercas': '>SED81 RR.*',
    'Limpador de parabrisa': '>SSH121<',
    'Excesso de Velocidade': '>SED30.*V0.*',
    'Desaceleração brusca': '>SED207.*V2.*',
    'Aceleração brusca': '>SED208.*V2.*',
    'Mifare externo': '.*RU00\+\+',
    'Mifare interno': '>SED19 IO03\+\+.',
    # 'Condução ininterrupta': '>SED115 CC45.*',
    'Condução ininterrupta': '>SSH151<',
    'Modo Sleep': '>SED15 LP01\+\+.*',
    'Rotas SP': '>SED81 VM01\+\+.*',
    'Tablet': '>SED169.*TRM.*',
    # 'Lora': '>SED126 RF32\+\+.*',
    'Lora': '>VSMG0000.*',
    'Bloqueio': '>SED59.*V2.*',
    'Banco de motorista': '>SED105.*AX.*',
    'Comboio': '>SED125 CC26\-\-.*',
    'Banguela': '>SED35.*V2.*'
}
resultados = {}

def bitmap_funcionaliades(index):
    bitmap = 0
    for i in index:
        bitmap = bitmap + 2**(int(i))
    return bitmap


def change_files(path):
    for file in path:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        resultados = {chave: True if (busca := re.search(padrao, content)) is not None 
                        else False for chave, padrao in padroes.items()}

        indices = [i for i, x in enumerate(resultados.values()) if x == True]
        bitmap = bitmap_funcionaliades(indices)
        content = re.sub('>SSO<',f'//Bitmap funcionalidades\n>SCT95 {bitmap}<\n>SSO<',content)
        content = re.sub('>SED181.*','>SED181 CL58++ +- GF0 AX {QUV00,9,3 QUV10,9,130 QCT14,7,10 QCT15,7,10 QCT17,7,10 QCT95,7,10}<',content)
        with open('fucionalidades_github_vl8.xls','a',encoding='utf-8') as f:
            f.write(f'{os.path.basename(file)};{bitmap}\n')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)


def change_files_json(path):
    for file in path:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            data = json.loads(content)
            comandos = data['comandos']
            hash = data['hash']
            aes_object = AES_pkcs5(comandos)
            if data['hash'] != "":
                comandos = aes_object.decrypt(hash, comandos)
                data.update({'comandos': comandos, 'hash': ""})
            comandos = re.sub(';','\n',comandos)
            resultados = {chave: True if (busca := re.search(padrao, comandos)) is not None 
                            else False for chave, padrao in padroes.items()}

            indices = [i for i, x in enumerate(resultados.values()) if x == True]
            bitmap = bitmap_funcionaliades(indices)
            
            comandos = re.sub('>SSO<',f'>SCT95 {bitmap}<;>SSO<',comandos)
            comandos = re.sub('>SED181.*?<','>SED181 CL58++ +- GF0 AX {QUV00,9,3 QUV10,9,130 QCT14,7,10 QCT15,7,10 QCT17,7,10 QCT95,7,10}<',comandos)
            comandos = re.sub('\n',';',comandos)
            with open ('fucionalidades_vl8.xls','a',encoding='utf-8') as f:
                f.write(f'{os.path.basename(file)};{bitmap}\n')
            data.update({'comandos': aes_object.encrypt(comandos)})
            data.update(hash=base64.b64encode(aes_object.key).decode('utf-8'))
                
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False)



def listar_arquivos(pasta):
    arquivos_txt = []
    arquivos_json = []

    for diretorio_raiz, _, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                caminho_completo = os.path.join(diretorio_raiz, arquivo)
                arquivos_txt.append(caminho_completo)
            if arquivo.endswith(".json"):
                caminho_completo = os.path.join(diretorio_raiz, arquivo)
                arquivos_json.append(caminho_completo)

    return arquivos_txt, arquivos_json


if __name__ == "__main__":
    pasta = dlg.askdirectory()
    path_txt, path_json = listar_arquivos(pasta)
    change_files(path_txt)
    change_files_json(path_json)
