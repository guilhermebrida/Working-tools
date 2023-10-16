import base64
from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding
from Crypto.Cipher import AES
import hashlib


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