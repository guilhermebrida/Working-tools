#!/bin/bash

# Defina a pasta de origem e a pasta de destino
# pasta_origem_svn="/media/brida/OS/ScriptsConfigurador/VL10/Configuracao"
pasta_origem_svn="/media/brida/OS/ScriptsConfigurador/VL10/Perfil Conducao"
pasta_origem_git="/media/brida/OS/Git Repo/virloc6/CAN-Sensor"
pasta_destino="/media/brida/OS/@Sandbox/vc5vl10_perfil"

planilha_scripts_comparados="/media/brida/OS/Python_scripts/Working-tools/docs/scripts_comparados_vc5.xls"


# Defina o caminho do arquivo de lista
python -u "/media/brida/OS/Python_scripts/Working-tools/Python_tools/Json_type.py" > "/media/brida/OS/Python_scripts/Working-tools/docs/files.txt"
arquivo_lista="/media/brida/OS/Python_scripts/Working-tools/docs/files.txt"


if [ ! -d $pasta_destino ];then
    mkdir $pasta_destino
fi

# Ler cada linha do arquivo de lista e copiar o arquivo correspondente
while IFS= read -r nome_arquivo; do
    caminho_arquivo_origem="$pasta_origem_svn/$nome_arquivo"
    caminho_arquivo_destino="$pasta_destino/$nome_arquivo"
    
    if [ -e "$caminho_arquivo_destino" ];then
        echo "Arquivo já existe, não será copiado: $caminho_arquivo_destino"
    else
    # Verifique se o arquivo de origem existe antes de copiá-lo
        if [ -f "$caminho_arquivo_origem" ]; then
            cp "$caminho_arquivo_origem" "$caminho_arquivo_destino"
            echo "Copiado: $caminho_arquivo_origem -> $caminho_arquivo_destino"
        else
            echo "Aviso: Arquivo de origem não encontrado: $caminho_arquivo_origem"
        fi
    fi
done < "$arquivo_lista"

rm -f "/media/brida/OS/Python_scripts/Working-tools/docs/files.txt"


# Copia apenas os arquivos da pasta de origem para a pasta de destino
# find "$pasta_origem_git" -type f -name "*.txt" -exec cp {} "$pasta_destino" \;

echo "Concluído clone dos arquivos JSON e txt!"


## rodar script que compara os arquivos json e txt de uma pasta e gera uma planilha com os resultados 
# python -u "/media/brida/OS/Python_scripts/Working-tools/Python_tools/compara_scripts.py" "$pasta_destino" "$planilha_scripts_comparados"


