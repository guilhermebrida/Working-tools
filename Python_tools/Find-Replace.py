# from tkinter import Tk
from tkinter.filedialog import askopenfilename, askopenfilenames, askdirectory
import json
from tkinter import *
from tkinter import messagebox
import re
import bitmap
from encrypter import AES_pkcs5
import logging

root = Tk()
root.geometry("200x120")
root.title("Encriptador")
root.configure(background="#dde")

class VariosArquivos():
    def __init__(self):
        Label(root, text= "Find: ", background="#dde", foreground="#009", anchor=W).pack()
        self.find = Entry(root)
        self.find.bind('<Return>')
        self.find.pack()

        Label(root, text= "Replace: ", background="#dde", foreground="#009", anchor=W).pack()
        self.replace = Entry(root)
        self.replace.bind('<Return>')
        self.replace.pack()

        Button(root, text='Do it!',command=lambda: self.Replace() ,background="#dde", foreground="#009" ).pack(pady=10, ipadx=10)
        

    def Replace(self):
        pasta = askdirectory()
        path_completo = bitmap.listar_arquivos(pasta)
        path = list(path_completo[0])
        path.extend(path_completo[1]) 
        for self.nomes in path:

            if self.nomes.endswith(".txt"):
                with open(f'{self.nomes}','r',encoding='utf_8')as self.f:
                    self.txt_data=self.f.read()
                self.txt_data2 = re.sub(fr'{self.find.get()}',fr'{self.replace.get()}',self.txt_data)
                print(self.txt_data2)
                with open(f'{self.nomes}','w',encoding='utf_8') as self.f:
                    self.f.write(self.txt_data2)

            if self.nomes.endswith(".json"):
                try:
                    with open(f'{self.nomes}',encoding='utf_8') as self.f:
                        self.json_data=self.f.read()
                    self.json_dict = json.loads(self.json_data)
                    self.comandos=self.json_dict['comandos']
                    self.hsh = self.json_dict['hash']
                    if  self.hsh != "":
                        aes_object = AES_pkcs5(self.comandos)
                        self.comandos = aes_object.decrypt(self.hsh, self.comandos)
                        self.json_dict.update({'comandos': self.comandos, 'hash': ""})
                    self.comandos2 = re.sub(self.find.get(), self.replace.get(),self.comandos)
                    self.json_dict.update(comandos = self.comandos2)
                    with open(f'{self.nomes}', 'w',encoding='utf-8') as self.f:
                        json.dump(self.json_dict, self.f,ensure_ascii=False)
                except:
                    logging.exception("Erro", self.nomes)
                    messagebox.showinfo("Erro", self.nomes)
                
                    
  
if __name__ == '__main__':
    VariosArquivos()
    mainloop()