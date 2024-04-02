import re
from pprint import pprint 
from tkinter import filedialog as dlg
import os
from copilot_functions import Copiloto 
import bitmap as bp


def get_suts(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    suts = re.findall('>SUT.*<',content)
    print(suts.sort())




if __name__ == "__main__":


    file = dlg.askopenfile()
    get_suts(file)