import re

def extrair_limpador(comandos):
    for i in range(len(comandos)):
        limpador = re.search('>SUT02,QCT80.*<', comandos[i])
        if limpador is not None:
            return 'CAN'
        
        limpador = re.search('>SUT02,QIN.*<', comandos[i])
        if limpador is not None:
            return 'SENSOR'
    
    return None

def litrometro(comandos):
    for comando in comandos:
        if re.search('>SED22.*',comando) is not None:
            return 'CAN'
        if re.search('>SED36.*',comando) is not None:
            return 'CAN'
    return None

def velocidade_s8(comandos):
    for comando in comandos:
        match = re.search('>VS29\d\d,.*<', comando)
        if match is not None:
            if len(match.group().split(',')) == 11:
                velocidade = match.group().split(',')[4]
                if re.search('(64|48)', velocidade):
                    return match.group()
            if len(match.group().split(',')) > 11:
                velocidade = match.group().split(',')[11]
            if velocidade is not None and re.search('(64|48)', velocidade):
                return match.group()
    return None

def rpm_s8(comandos):
    for comando in comandos:
        match = re.search('>VS29\d\d,.*<', comando)
        if match is not None:
            try:
                rpm = match.group().split(',')[4]
                if re.search('27', rpm) is not None:
                    return match.group()
                rpm = match.group().split(',')[11]
                if re.search('27', rpm) is not None:
                    return match.group()
            except IndexError:
                continue
    return None

def odometro_s8(comandos):
    for comando in comandos:
        match = re.search('>VS29\d\d,.*<', comando)
        if match is not None:
            odometro = match.group().split(',')[4]
            odometro = re.search('01', odometro)
            if odometro is not None:
                return match.group()
        odometro = re.search('>SUT50,QCT03,07,15,0,1.*<', comando)
        if odometro is not None:
            return 'SENSOR'
    return None

def horimetro_s8(comandos):
    for comando in comandos:
        match = re.search('>VS29\d\d,.*<', comando)
        if match is not None:
            horimetro = match.group().split(',')[4]
            horimetro = re.search('02', horimetro)
            if horimetro is not None:
                return match.group()
        horimetro = re.search('>SED119.*<', comando)
        if horimetro is not None:
            return 'CALCULADO'
    return None

def freio_s8(comandos):
    for comando in comandos:
        match = re.search('>VS29\d\d,.*<', comando)
        if match is not None:
            try:
                freio = match.group().split(',')[4]
                if re.search('81', freio) is not None:
                    return match.group()
                freio = match.group().split(',')[11]
                if re.search('81', freio) is not None:
                    return match.group()
            except IndexError:
                continue
    return None

def farol_s8(comandos):
    for comando in comandos:
        match = re.search('>VS29\d\d,.*<', comando)
        if match is not None:
            farol = match.group().split(',')[4]
            farol = re.search('82', farol)
            if farol is not None:
                return match.group()
    return None

def cinto_s8(comandos):
    for comando in comandos:
        match = re.search('>VS29\d\d,.*<', comando)
        if match is not None:
            cinto = match.group().split(',')[4]
            cinto = re.search('83', cinto)
            if cinto is not None:
                return match.group()
    return None

def freio_mao_s8(comandos):
    for comando in comandos:
        match = re.search('>VS29\d\d,.*<', comando)
        if match is not None:
            freio_mao = match.group().split(',')[4]
            freio_mao = re.search('84', freio_mao)
            if freio_mao is not None:
                return match.group()
    return None