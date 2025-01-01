from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Clé secrète pour le déchiffrement 
secret_key = b'macleinsecreten32octets.'  


def decrypter_message(message_chiffre, key):
    
    encrypted_message = base64.b64decode(message_chiffre)
    cipher = AES.new(key, AES.MODE_ECB)
    
    decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size)
    return decrypted_message.decode('utf-8')

#valeur lu une fois le qr code scanné
valeur = "oGYLSHfe8DTeJ3i/4IdjEtAcD09Q8TG+uH/z0NM3Hcd5+Ti7aNd5zdrO9CFoAL3+Pjh2VZJWUlIV3NgkkBuV7g=="
#scop_2024-11-02_09-21-43_f3ef27b4-bcab-4d98-9569-ee3a18f50a02
message_chiffre = valeur
message_dechiffre = decrypter_message(message_chiffre, secret_key)
print("Message déchiffré :", message_dechiffre)
