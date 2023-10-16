from bitmap import dlg, listar_arquivos

def add_space_before_first_newline(file_path):
    for file in file_path:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            first_newline_index = content.find('\n')
            if first_newline_index != -1:
                content = content[:first_newline_index] + ' ' + content[first_newline_index:]

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)


# file_path = 'C:/Python_scripts/Working-tools/docs/txt_vl10.txt'
pasta = dlg.askdirectory()
file_path = listar_arquivos(pasta)[0]
add_space_before_first_newline(file_path)