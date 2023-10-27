#!/bin/bash

# Defina suas credenciais de login do Oracle
username="AERO"
password="aero123"
database="xe"
host="10.1.2.10"
port="1521"

# Script SQL a ser executado
script_sql="/media/brida/OS/BRIDA_SQL/teste_parser_DEV.sql"

# Defina a variável de ambiente LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_4:$LD_LIBRARY_PATH

# Comando para conectar e executar o script SQL
/opt/oracle/instantclient_21_4/sqlplus -s $username/$password@$database @$script_sql
# export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_4:$LD_LIBRARY_PATH
# /opt/oracle/instantclient_21_4/sqlplus AERO/aero123@xe

