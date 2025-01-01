import uuid
import qrcode
import os
from datetime import datetime

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# Clé secrète pour le chiffrement (doit être de 16, 24 ou 32 octets)
secret_key = b'macleinsecreten32octets.'  # Exemple de clé en bytes

def crypter_message(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_message = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(encrypted_message).decode('utf-8')


date= datetime.now().strftime("%Y-%m-%d")
date_heure = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

nom_dossier = f"Dossier_{date}"
nbre_qr_code = int(input("Combien de qr_code à générer ?"))

while nbre_qr_code > 0:
    code_uuid = uuid.uuid4()
    print(code_uuid)
    qr_data = f"scop_{date_heure}_{code_uuid}"
    qr_data_chiffre = crypter_message(qr_data, secret_key)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,
        border=4,
    )
    qr.add_data(qr_data_chiffre)
    qr.make(fit=True)
    qr = qr.make_image(fill_color="#000000", back_color="white").convert('RGB')


    if not os.path.exists(nom_dossier):
        os.makedirs(nom_dossier)
    qr.save(f"{nom_dossier}/qr_{nbre_qr_code}_{date_heure}.png")
    nbre_qr_code -= 1

