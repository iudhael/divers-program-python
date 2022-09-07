import ast
import base64

import  Crypto
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from Crypto.Cipher import PKCS1_v1_5
import gmpy2
from Crypto.Util.py3compat import tobytes






# ouvertue du fichier pubkey en mode lecture
f = open('pubkey.txt', 'r')

key = RSA.import_key(f.read())
#key
n=key.n
e=key.e


# affichage de n et e
print(f"n ={n}")
print(f"e ={e}")



# ouvertue du fichier b16.txt contenant le message a decode en base64 en mode lecture
b =  open('b16.txt', 'r')

# ouvertue du fichier message.txt contenant le message a decoder en mode lecture
msg = open('message.txt', 'r')
#decryp = key.decrypt(ast.literal_eval(str(msg.read())))

#print(f"msg={decryp}")



p = 965445304326998194798282228842484732438457170596000297175243

q = 965445304326998194798282228842484732438457170596000553527601


f= (p-1)*(q-1)
print(f"f={f}")

# obtention de la valeur de d
d=gmpy2.invert(e,f)
#affichage de d
print(f"d={d}")

#verification
print(f"(e*d)%f={(e*d)%f}")

#print(f"key : ((n={hex(n)}, d={hex(d)})")


print("decryptage")
dd = pow(e,-1,f)
#obtention de la clé privé avec le module  privatekey
pk = rsa.PrivateKey(int(n),int(e),int(dd),int(p),int(q))
#exp1 = pk.exp1
#exp2 = pk.exp2
#coef = pk.coef

#pubkey = open('pubkey.txt', 'r')

print(pk)



def export_private_key(private_key, filename):
    fichier = open(filename, "w")
    priv_k = private_key.save_pkcs1().decode('utf8')
    fichier.write(priv_k)
    fichier.close()

#File to store the private key : .pem file
pkf = "priv_key.pem"

export_private_key(pk,pkf)



""""
dd = pow(e,-1,f)

"""
# I directly use the cipher here. I don't want to bother myself with a file
# That's all I did.
c= b'A\x10\x8e\x9c2\xe8y\x95J\xbdz\xdc\x1d\xe0A-|=)\xba>i\x93]\xfd\x9eg\xe3\xa2\xfd\xf5\x0e|"\xe7\xb2\x02\x8f1\x13\xcc_\x08\xce\xc55\x1bo\xff\xd6'

def decrypt(cipher_text, private_key_path):

    private_key = RSA.importKey(open(private_key_path, "r").read())

    rsa_object = PKCS1_v1_5.new(private_key)
    plaintext = rsa_object.decrypt(cipher_text, private_key)
    return plaintext



decrpt_msg = open('msg_decrypt.txt', "wb")

decrpt_msg.write(decrypt(c, pkf))
decrpt_msg.close()







