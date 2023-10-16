import json
import os

##CRIA O ARQUIVO txt A PARTIR DE UM JSON NO SVN

with open('scripts_vl1012_08.txt','r', encoding='utf-8')as f:
    files = f.read().split('\n')
    print(files)


for file in files:
    try:
        with open(f'C:/@Sandbox/vl10_12_08/{file}','r', encoding='utf-8') as f:
            data = f.read()
    except:
        print(f'Arquivo {file} não encontrado')
        continue
    json_data = json.loads(data)
    comandos = json_data['comandos']
    nome = os.path.basename(file).split('.')[0]
    with open(f'C:/@Sandbox/vl10_12_08/{nome}.txt','w') as f:
        comandos = comandos.split(';')
        for comando in comandos:
            f.write(comando)
            f.write('\n')
        

