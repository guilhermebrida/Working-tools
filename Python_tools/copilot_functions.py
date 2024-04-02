import re
from datetime import date
import logging

class Copiloto:
    def __init__(self, tudo=None, hardware=None):
        self.tudo = tudo
        self.hardware = hardware

    def limite_velocidade(self):
        try:
            match = re.search('(?<=>SCT11\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar limite de velocidade: {e}')

    def limite_vel_chuva(self):
        try:
            match = re.search('(?<=>SCT12\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar limite de velocidade em chuva: {e}')

    def limite_vel_carregado(self):
        try:
            match = re.search('(?<=>SCT13\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar limite de velocidade carregado: {e}')

    def tolerancia_infra_vel(self):
        try:
            match = re.search('(?<=>SCT06\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
    
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar tolerância infração de velocidade: {e}')

    def freada_brusca(self):
        try:
            match = re.search('(?<=>SCT08\s0-)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar freada brusca: {e}')

    def aceleracao_brusca(self):
        try:
            match = re.search('(?<=>SCT09\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar aceleração brusca: {e}')

    def marcha_lenta(self):
        try:

            if self.hardware == 'VL10' or self.hardware == 'VL12':
                match = re.search('(?<=>SUT04,QCT27,7,15,)\d+(?:,\d+)+(?=<)', self.tudo)
                if match is not None:
                    return match.group()

            else:
                match = re.search('(?<=>SUT11,QCT27,7,15,)\d+(?:,\d+)+(?=<)', self.tudo)
                if match is not None:
                    return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar marcha lenta: {e}')
                

    def faixa_verde(self):
        try:
            if self.hardware == 'VL10' or self.hardware == 'VL12':
                match = re.search('(?<=>SUT09,QCT27,7,15,)\d+(?:,\d+)+(?=<)', self.tudo)
                if match is not None:
                    return match.group()
            
            else:
                match = re.search('(?<=>SUT12,QCT27,7,15,)\d+(?:,\d+)+(?=<)', self.tudo)
                if match is not None:
                    return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar min faixa verde: {e}')


    def limite_rotacao(self):
        try:
            match = re.search('(?<=>SUT13,QCT27,7,15,)\d+(?:,\d+)+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar limite de rotação: {e}')

    def freio_motor(self):
        try:
            if self.hardware == 'VL10' or self.hardware == 'VL12':
                match = re.search('(?<=>SUT17,QCT27,7,15,)\d+(?=(?:,\d+)*<)', self.tudo)
                if match is not None:
                    return match.group()
            else:
                match = re.search('(?<=>SUT15,QCT27,7,15,)\d+(?=(?:,\d+)*<)', self.tudo)
                if match is not None:
                    return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar freio motor: {e}')

    def troca_marcha(self):
        try:
            if self.hardware == 'VL10' or self.hardware == 'VL12':
                match = re.search('(?<=>SUT56,QCT27,7,15,)\d+(?:,\d+)+(?=<)', self.tudo)
                if match is not None:
                    return match.group()
            else:
                match = re.search('(?<=>SUT16,QCT27,7,15,)\d+(?:,\d+)+(?=<)', self.tudo)
                if match is not None:
                    return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar troca de marcha: {e}')

    def parada_motor_ligado(self):
        try:
            match = re.search('(?<=>SCT04\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar tempo de parada motor com ligado: {e}')

    def tempo_max_conducao(self):
        try:
            match = re.search('(?<=>SCT14\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar tempo maximo de condução: {e}')

    def tempo_descanso(self):
        try:
            match = re.search('(?<=>SCT17\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar tempo de descanso: {e}')

    def tolerancia_descanso(self):
        try:
            match = re.search('(?<=>SCT15\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar tolerancia de descanso: {e}')

    def get_bitmap(self):
        try:
            match = re.search('(?<=>SCT95\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar tolerancia de descanso: {e}')

    def get_ccid(self):
        try:
            match = re.search('(?<=\[cc\.id\])\d+(?=\[cc\.id\])', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar tolerancia de descanso: {e}')


    def lora(self, value):
        try:
            rede_lora = ''.join(str(ord(char)) for char in value)
            return re.sub('000102030405060708090A0B0C0D0E0F', rede_lora, self.tudo)
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar rede lora: {e}')

    def id_arquivo(self):
        try:
            match = re.search('>STP01.*<', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar id do arquivo: {e}')

    def id_arquivo2(self):
        try:
            match = re.search('>STP03.*<', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar id do arquivo: {e}')

    def nome_arquivo(self, value):
        try:
            path = value
            path = re.sub(" ", "_", path)
            return path
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar nome do arquivo: {e}')

    def sleep(self):
        try:
            match = re.search('(?<=VSKO)\d{4}', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao alterar tmepo de sleep: {e}')
            
    def limpador(self):
        try:
            match = re.search('>SSH12.*<', self.tudo)
            if match is not None:
                if match.group() == '>SSH121<':
                    return True
                if match.group() == '>SSH120<':
                    return False
            return False
        except Exception as e:
            logging.error(f'Erro ao extrair limpador: {e}')


    def get_bitmap(self):
        try:
            match = re.search('(?<=>SCT95\s)\d+(?=<)', self.tudo)
            if match is not None:
                return match.group()
        except Exception as e:
            logging.error(f'[{self.hardware}]Erro ao extrair bitmap: {e}')