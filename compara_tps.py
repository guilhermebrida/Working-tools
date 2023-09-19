import re
from pprint import pprint 
from tkinter import filedialog as dlg
import os
import json
from encrypter import AES_pkcs5
import functions
import bitmap

def get_tps(path):

    for file in path:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        tp = re.search('>STP02.*?<', content)
        comandos = re.findall('>.*<', content)
        velocidade = functions.velocidade_s8(comandos)
        rpm = functions.rpm_s8(comandos)
        limpador = functions.extrair_limpador(comandos)
        odometro = functions.odometro_s8(comandos)
        horimetro = functions.horimetro_s8(comandos)
        freio = functions.freio_s8(comandos)
        farol = functions.farol_s8(comandos)
        cinto = functions.cinto_s8(comandos)
        freioMao = functions.freio_mao_s8(comandos)
        litrometro = functions.litrometro(comandos)
        with open('TPS_CAN_GIT_VL8.xls','a',encoding='utf-8') as f:
            f.write(f'{os.path.splitext(os.path.basename(file))[0]};{tp.group()};{velocidade};{rpm};{limpador};{odometro};{horimetro};\
            {freio};{farol};{cinto};{freioMao};{litrometro}\n')


def get_tps_json(path):
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
        tp = re.search('>STP02.*?<', comandos)
        comandos_vs = re.findall('>.*<', comandos)
        velocidade = functions.velocidade_s8(comandos_vs)
        rpm = functions.rpm_s8(comandos_vs)
        limpador = functions.extrair_limpador(comandos_vs)
        odometro = functions.odometro_s8(comandos_vs)
        horimetro = functions.horimetro_s8(comandos_vs)
        freio = functions.freio_s8(comandos_vs)
        farol = functions.farol_s8(comandos_vs)
        cinto = functions.cinto_s8(comandos_vs)
        freioMao = functions.freio_mao_s8(comandos_vs)
        litrometro = functions.litrometro(comandos_vs)
            # comandos = re.sub('\n',';',comandos)
        with open('TPS_CAN_SVN_VL8.xls','a',encoding='utf-8') as f:
            f.write(f'{os.path.splitext(os.path.basename(file))[0]};{tp.group()};{velocidade};{rpm};{limpador};{odometro};{horimetro};\
            {freio};{farol};{cinto};{freioMao};{litrometro}\n')

if __name__ == "__main__":
    if not os.path.exists('TPS_CAN_GIT_VL8.xls'):
        with open('TPS_CAN_GIT_VL8.xls','w',encoding='utf-8') as f:
            f.write('Arquivo;TP;Velocidade;RPM;Limpador;Odometro;Horimetro;Freio;Farol;Cinto;Freio de mão;Litrometro\n')

    if not os.path.exists('TPS_CAN_SVN_VL8.xls'):
        with open('TPS_CAN_SVN_VL8.xls','w',encoding='utf-8') as f:
            f.write('Arquivo;TP;Velocidade;RPM;Limpador;Odometro;Horimetro;Freio;Farol;Cinto;Freio de mão;Litrometro\n')

    pasta = dlg.askdirectory()
    arquivos_txt, arquivos_json = bitmap.listar_arquivos(pasta)
    get_tps(arquivos_txt)
    get_tps_json(arquivos_json)