#!/bin/bash

# Defina a pasta de origem e a pasta de destino
pasta_origem="/media/brida/OS/ScriptsConfigurador/VL10/Perfil Conducao"
pasta_destino="/media/brida/OS/@Sandbox/VL10eVL12"

# Defina o caminho do arquivo de lista
arquivo_lista="/media/brida/OS/Python_scripts/Working-tools/scripts_vl1012.txt"


# Ler cada linha do arquivo de lista e copiar o arquivo correspondente
while IFS= read -r nome_arquivo; do
    caminho_arquivo_origem="$pasta_origem/$nome_arquivo"
    caminho_arquivo_destino="$pasta_destino/$nome_arquivo"
    
    # Verifique se o arquivo de origem existe antes de copiá-lo
    if [ -f "$caminho_arquivo_origem" ]; then
        cp "$caminho_arquivo_origem" "$caminho_arquivo_destino"
        echo "Copiado: $caminho_arquivo_origem -> $caminho_arquivo_destino"
    else
        echo "Aviso: Arquivo de origem não encontrado: $caminho_arquivo_origem"
    fi
done < "$arquivo_lista"

echo "Concluído!"
