import os
import psycopg2

# Configurações de conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="fota",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Caminho da pasta principal
base_dir = "/home/brida/Repos/iot-virtec-scripts-generator/api_copiloto/backend/funcoes_copiloto"

try:
    with conn.cursor() as cursor:
        # Iterar pelas pastas (hardware) e arquivos (description)
        for hardware in os.listdir(base_dir):
            hardware_path = os.path.join(base_dir, hardware)
            
            if os.path.isdir(hardware_path):  # Se for uma pasta
                for description_with_ext in os.listdir(hardware_path):
                    file_path = os.path.join(hardware_path, description_with_ext)
                    
                    if os.path.isfile(file_path):  # Se for um arquivo
                        # Remover a extensão .txt do nome do arquivo
                        description = os.path.splitext(description_with_ext)[0]
                        
                        # Ler o conteúdo do arquivo (script)
                        with open(file_path, 'r', encoding='utf-8') as file:
                            script = file.read()
                        
                        # Inserir no banco de dados
                        insert_query = """
                            INSERT INTO copilot_functions (hardware, description, script)
                            VALUES (%s, %s, %s)
                        """
                        cursor.execute(insert_query, (hardware, description, script))
        
        # Confirmar as inserções
        conn.commit()

except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()

finally:
    conn.close()