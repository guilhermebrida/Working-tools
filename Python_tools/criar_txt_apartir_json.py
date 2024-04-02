import json
import os
import platform
##CRIA O ARQUIVO txt A PARTIR DE UM JSON NO SVN

linuxPath = '/media/brida/OS/@Sandbox/vc5vl10_perfil'
windowsPath = 'C:/@Sandbox/can_vl10vc5'

with open('docs/scripts_vc5_vl10.txt','r', encoding='utf-8')as f:
    files = f.read().split('\n')
    print(files)


for file in files:
    try:
        if platform.system() == 'Linux':
            with open(f'{linuxPath}/{file}','r', encoding='utf-8') as f:
                data = f.read()
        if platform.system() == 'Windows':
            with open(f'{windowsPath}/{file}','r', encoding='utf-8') as f:
                data = f.read()
    except:
        print(f'Arquivo {file} não encontrado')
        continue

    json_data = json.loads(data)
    comandos = json_data['comandos']
    nome = os.path.basename(file).split('.')[0]
    if platform.system() == 'Windows':
        with open(f'{windowsPath}/{nome}.txt','w') as f:
            comandos = comandos.split(';')
            for comando in comandos:
                f.write(comando)
                f.write('\n')
    if platform.system() == 'Linux':
        with open(f'{linuxPath}/{nome}.txt','w') as f:
            comandos = comandos.split(';')
            for comando in comandos:
                f.write(comando)
                f.write('\n')
        

