
from tkinter import filedialog as dlg
from bitmap import listar_arquivos
import json
from tkinter import messagebox
import os
import logging
from datetime import datetime


## AGRUPO OS SCRIPTS POR HARDWARE

# pasta = dlg.askdirectory()
pasta = "/media/brida/OS/ScriptsConfigurador/VL10/Perfil Conducao"
# pasta = "/media/brida/OS/ScriptsConfigurador/VL10/Configuracao"
# pasta = "C:/ScriptsConfigurador/VL10/Configuracao"
# pasta = "C:/ScriptsConfigurador/VL10/Perfil Conducao"
files = listar_arquivos(pasta)

# with open('docs/vc5vc7_can.txt', 'a', encoding='utf-8') as f:
    # f.write(f'//================================================\n')
    # f.write(f'//========={datetime.now()}==============\n')
    # f.write(f'//================================================\n')

for file in files[1]:
    if file.endswith('.json'):
        try:
            with open(file, 'r') as f:
                content = f.read()
            data = json.loads(content)
            hw = data['hardware']
            # if ("VIRLOC10" in hw and "VIRLOC11" in hw and "VIRLOC12" in hw) and os.path.basename(file) not in 'hardwares_perfis.txt':
            # if ('VIRLOC10' in hw or 'VIRLOC11' in hw or 'VIRLOC12' in hw) and 'VIRLOC6' not in hw and 'VL6' not in hw and 'VIRCOM5' not in hw:
            if ('VIRLOC10' in hw and 'VIRLOC11' in hw and 'VIRCOM5' in hw):
                with open('docs/vc5vl10_perfil.txt', 'a', encoding='utf-8') as f:
                    print(f'{os.path.basename(file)}\n')
                    f.write(f'{os.path.basename(file)}\n')
        except:
            continue

# with open('docs/vc5vc7_can.txt', 'a', encoding='utf-8') as f:
#     f.write(f'//================================================\n')
#     f.write(f'//================================================\n')