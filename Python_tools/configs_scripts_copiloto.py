import re
from pprint import pprint 
from tkinter import filedialog as dlg
import os
from copilot_functions import Copiloto 
import bitmap as bp


def get_configs(files):
    print(files)
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        vel = Copiloto(content,hw).limite_velocidade()
        print(vel)
        vel_chuva = Copiloto(content,hw).limite_vel_chuva()
        # print(vel_chuva)
        vel_carreg = Copiloto(content,hw).limite_vel_carregado()
        print(vel_carreg)
        tol_vel = Copiloto(content,hw).tolerancia_infra_vel()
        print(tol_vel)
        freada = Copiloto(content,hw).freada_brusca()
        print(freada)
        aceleracao = Copiloto(content,hw).aceleracao_brusca()
        print(aceleracao)
        march = Copiloto(content,hw).marcha_lenta()
        print(march)
        verde = Copiloto(content,hw).faixa_verde()
        print(verde)
        excesso = Copiloto(content,hw).limite_rotacao()
        print(excesso)
        freio_motor = Copiloto(content,hw).freio_motor()
        print(freio_motor)
        troca = Copiloto(content,hw).troca_marcha()
        print(troca)
        parada = Copiloto(content,hw).parada_motor_ligado()
        print(parada)
        conducao = Copiloto(content,hw).tempo_max_conducao()
        print(conducao)
        descanso = Copiloto(content,hw).tempo_descanso()
        print(descanso)
        tol_descanso = Copiloto(content,hw).tolerancia_descanso()
        print(tol_descanso)
        id_arquivo = Copiloto(content,hw).id_arquivo()
        print(id_arquivo)
        id_arquivo2 = Copiloto(content,hw).id_arquivo2()
        print(id_arquivo2)
        bitmap = Copiloto(content,hw).get_bitmap()
        print(bitmap)
        ccid = Copiloto(content,hw).get_ccid()
        print(ccid)
        sleep = Copiloto(content,hw).sleep()
        print(sleep)
        limpador = Copiloto(content,hw).limpador()
        print(limpador)
        bitmap = Copiloto(content,hw).get_bitmap()
        print(bitmap)
        if bitmap is None:
            bitmap = bp.gera_bitmap(file)
            print(f'get_bit {bitmap}')
              
        with open(f'Configs_scripts_suzano_{hw}.xls','a',encoding='utf-8') as f:
            f.write(f'{os.path.basename(file)};{id_arquivo};{id_arquivo2};{vel};{vel_carreg};{vel_chuva};{tol_vel};{parada};{march};{verde};{excesso};{freio_motor};{aceleracao};{freada};{conducao};{descanso};{tol_descanso};{limpador};{bitmap}\n')





if __name__ == "__main__":
    hw = 'VL12'
    
    if not os.path.exists(f'Configs_scripts_suzano_{hw}.xls'):
        with open(f'Configs_scripts_suzano_{hw}.xls','w',encoding='utf-8') as f:
            f.write('Arquivo;Tag1;Tag2;limite Vel;Limite Vel carregado;Limite Vel Chuva;Tolerancia Vel(s);Parada Motor Ligado;Marcha Lenta;Marcha Verde;Excesso RPM;RPM Freio Motor;Aceleração Brusca;Freada Brusca;Tempo max condução(s);tempo descanso(s);tempo tolerancia(s);Limpador;Bitmap Funcionalidades\n')
        

    pasta = dlg.askdirectory()
    arquivos_txt, arquivos_json = bp.listar_arquivos(pasta)
    get_configs(arquivos_txt)
    