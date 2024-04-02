pasta_origem="/home/brida/Repos/ScriptsConfigurador/VL10/Configuracao"
arquivo_lista="/media/brida/OS/Python_scripts/Working-tools/docs/vl6_can.txt"

while IFS= read -r nome_arquivo; do
    caminho_arquivo_origem="$pasta_origem/$nome_arquivo"
    
    if [ -f "$caminho_arquivo_origem" ]; then
        # svn delete "$caminho_arquivo_origem" 
        rm -f "$caminho_arquivo_origem"
        echo "removido: $caminho_arquivo_origem"
    else
        echo "Aviso: Arquivo de origem não encontrado: $caminho_arquivo_origem"
    fi
done < "$arquivo_lista"




