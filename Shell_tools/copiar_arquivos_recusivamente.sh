#!/bin/bash

pasta_origem="/media/brida/OS/Git Repo/virloc12/CAN-Sensor"
pasta_destino="/media/brida/OS/@Sandbox/can_vl10"

# Copia apenas os arquivos da pasta de origem para a pasta de destino
find "$pasta_origem" -type f -name "*.txt" -exec cp {} "$pasta_destino" \;

