from bitmap import json,re,dlg,listar_arquivos


##CRIA PLANILHA COM CUSTOMER CHILD ID DE CADA ARQUIVO JSON DA PASTA

def get_cc_tag(pasta:list):
    sem_tag = [] 
    for file in pasta:
        with open(file, 'r') as f:
            file_json = json.load(f)
        try:
            nome = file_json['idarquivo'] 
            print(nome)
            cc_tag = file_json['customer_child_id']
            print(cc_tag)
        except:
            sem_tag.append(file)
            print('Nao tem cc_tag',nome)
        with open('cc_tag_vl1012.xls', 'a') as f:
            f.write(f'{nome};{cc_tag}\n')
    with open('cc_tag_vl1012.xls', 'a') as f:
        f.write('\nSem cc_tag\n')
        for i in sem_tag:
            f.write(f'{i}\n')



if __name__ == '__main__':
    pasta = dlg.askdirectory()
    jsons = listar_arquivos(pasta)[1]
    get_cc_tag(jsons)
