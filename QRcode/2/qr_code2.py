import qrcode
from qrcode.constants import  ERROR_CORRECT_L

# fonctionne avec pilow
# une variable qr qui va contenir l'objet qr code et l'image generer
qr = qrcode.QRCode(
    # nombre entre 1 et 40 qui est la taille du qr code
    version=3,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=5
)

qr.add_data("https://www.youtube.com")
qr.make(fit=True)

# generer le qr code
# melanger les couleurs de sorte a lire le qr code
img = qr.make_image(fill_color="green", back_color="white")
img.save('qrcode.png')
