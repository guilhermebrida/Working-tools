
$pasta_origem = "C:/ScriptsConfigurador/VL10/Perfil Conducao"
$arquivo_lista = "C:/Python_scripts/Working-tools/docs/removido_vl1012.txt"

foreach ($nome_arquivo in Get-Content $arquivo_lista) {
    $caminho_arquivo_origem = Join-Path $pasta_origem $nome_arquivo
    
    if (Test-Path $caminho_arquivo_origem -PathType Leaf) {
        Remove-Item $caminho_arquivo_origem -Force
        Write-Host "removido: $caminho_arquivo_origem"
    } else {
        Write-Host "Aviso: Arquivo de origem não encontrado: $caminho_arquivo_origem"
    }
}