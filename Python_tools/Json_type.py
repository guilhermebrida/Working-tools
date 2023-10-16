
from tkinter import filedialog as dlg
from bitmap import listar_arquivos
import json
from tkinter import messagebox
import os


# if __name__ == '__main__':
# with open('scripts_vl1012.txt', 'a') as f:
#     f.write('============== VL1012 =============\n')


# pasta = dlg.askdirectory()
pasta = "/media/brida/OS/ScriptsConfigurador/VL10/Perfil Conducao"
# pasta = "C:/ScriptsConfigurador/VL10/Perfil Conducao"
files = listar_arquivos(pasta)
# print(files[0])
for file in files[1]:
    # print(file)
    if file.endswith('.json'):
        try:
            with open(file, 'r') as f:
                content = f.read()
            
            data = json.loads(content)
            # print(data)
            hw = data['hardware']
            print(hw)
            # if ("VIRLOC10" in hw and "VIRLOC11" in hw and "VIRLOC12" in hw) and os.path.basename(file) not in 'hardwares_perfis.txt':
            if ('VIRLOC10' in hw or 'VIRLOC11' in hw or 'VIRLOC12' in hw) and 'VIRLOC6' not in hw and 'VL6' not in hw and 'VIRCOM5' not in hw:
                with open('docs/removido_vl1012.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{os.path.basename(file)}\n')
                print(file,hw)
        except:
            continue