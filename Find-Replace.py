from tkinter import Tk
from tkinter.filedialog import askopenfilename, askopenfilenames, askdirectory
from Crypto.Cipher import AES
import base64
from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding
import hashlib
import json
from pprint import pprint
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import bitmap

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
        path = bitmap.listar_arquivos(pasta)[0]
        for self.nomes in path:
            tipo = self.nomes.split('.',-1)
            if tipo[1] == 'txt':
                self.f=open(f'{self.nomes}',encoding='utf_8')
                self.txt_data=self.f.read()
                self.f.close()
                # self.txt_data2 = self.txt_data.replace(self.find.get(),self.replace.get())
                self.txt_data2 = re.sub(fr'{self.find.get()}',fr'{self.replace.get()}',self.txt_data)
                self.f=open(f'{self.nomes}','w',encoding='utf_8')
                self.f.write(self.txt_data2)
            if tipo[1] == 'json':
                self.f=open(f'{self.nomes}',encoding='utf_8')
                self.json_data=self.f.read()
                self.json_dict = json.loads(self.json_data)
                self.comandos=self.json_dict['comandos']
                self.hsh = self.json_dict['hash']
                if  self.hsh == "":
                    self.comandos2 = re.sub(self.find.get(), self.replace.get(),self.comandos)
                    self.json_dict.update(comandos = self.comandos2)
                    self.f = open(f'{self.nomes}', 'w',encoding='utf-8')
                    json.dump(self.json_dict, self.f,ensure_ascii=False)
                else:
                    self.arquivos2()
                    self.comandos=self.json_dict['comandos']
                    self.comandos2= re.sub(self.find.get(), self.replace.get(),self.comandos)
                    self.json_dict.update(comandos = self.comandos2)
                    self.f = open(f'{self.nomes}', 'w',encoding='utf-8')
                    json.dump(self.json_dict, self.f,ensure_ascii=False)
                self.f.close()
                    

    def arquivos(self):
        self.AES_pkcs5_obj = AES_pkcs5(self.comandos)
        self.encrypted_message = self.AES_pkcs5_obj.encrypt(self.comandos)
        self.json_dict.update(comandos=self.encrypted_message)
        self.json_dict.update(hash=base64.b64encode(self.AES_pkcs5_obj.key).decode('utf-8'))
        print(self.json_dict)


    def arquivos2(self):
        self.AES_pkcs5_obj = AES_pkcs5(self.comandos)
        self.decrypted_comandos = self.AES_pkcs5_obj.decrypt(self.hsh,self.comandos)
        self.json_dict.update(comandos=self.decrypted_comandos)
        self.json_dict.update(hash='')
        return self.json_dict

        
        
class AES_pkcs5:
    def __init__(self,key:str, mode:AES.MODE_CBC=AES.MODE_CBC,block_size:int=16):
        self.key = self.setKey(key)
        self.mode = mode
        self.block_size = block_size

    def pad(self,byte_array:bytearray):
        pad_len = (self.block_size - len(byte_array) % self.block_size) *  chr(self.block_size - len(byte_array) % self.block_size)
        return byte_array.decode() + pad_len
    

    def unpad(self,byte_array:bytearray):
        return byte_array[:-ord(byte_array[-1:])]


    def setKey(self,key:str):
        key = key.encode('utf-8')
        md5 = hashlib.md5
        key = md5(key).digest()[:16]
        key = key.zfill(16)
        return key

    def encrypt(self,message:str)->str:
        self.iv = bytearray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        byte_array = message.encode("UTF-8")
        padded = self.pad(byte_array)
        cipher = AES.new(self.key, AES.MODE_CBC,self.iv)
        encrypted = cipher.encrypt(padded.encode())
        message=  base64.b64encode(encrypted).decode('utf-8')
        return message


    def decrypt(self,hsh,message:str)->str:
        self.iv = bytearray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        byte_array = message.encode("utf-8")
        message = base64.b64decode(byte_array)
        hsh = base64.b64decode(hsh)
        cipher= AES.new(hsh, AES.MODE_CBC, self.iv)
        decrypted = cipher.decrypt(message).decode('utf-8')
        return self.unpad(decrypted)

  
if __name__ == '__main__':
    VariosArquivos()
    mainloop()