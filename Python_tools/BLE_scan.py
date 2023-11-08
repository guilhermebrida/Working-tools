from bleak import discover
import re
import asyncio
from colorama import init, Fore, Back, Style

async def scan_devices():
    devices = await discover()
    for device in devices:
        # print(type(device))
        if re.search('VIRTEC.*',str(device.name)):
            if re.search('VIRTEC_VL8_2727',str(device.name)):
                print(Fore.RED + str(device))
            else:
                print(Style.RESET_ALL +str(device))
    print(Style.RESET_ALL +"=========================================")


if __name__ == "__main__":
    init()
    while True:
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(scan_devices())
        except KeyboardInterrupt:
            print("Programa finalizado pelo usuário")
            break
        except:
            print("Erro desconhecido")
            break