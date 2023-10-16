pasta_origem="/media/brida/OS/ScriptsConfigurador/VL10/Perfil Conducao"
arquivo_lista="/media/brida/OS/Python_scripts/Working-tools/docs/removido_vl1012.txt"

while IFS= read -r nome_arquivo; do
    caminho_arquivo_origem="$pasta_origem/$nome_arquivo"
    
    if [ -f "$caminho_arquivo_origem" ]; then
        rm -f "$caminho_arquivo_origem" 
        echo "removido: $caminho_arquivo_origem"
    else
        echo "Aviso: Arquivo de origem não encontrado: $caminho_arquivo_origem"
    fi
done < "$arquivo_lista"




