import os
import pyaes

# abrir a engine criptografada
file_name = 'miojo.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# chave de descriptografia
key = b'ninhomafagafinho'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# remover o arquivo encriptografado
os.remove(file_name)

# criar um novo arquivo descriptografado
new_file = 'miojo.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
