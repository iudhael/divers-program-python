import qrcode


# variable pour contenir l'image du QR code
# entre parenthese les données a recuppérer lorsque le qr code sera scaner
# sa peut etre un lien ou des donné en brutes

img = qrcode.make('le petit prince')
img.save('qrcode.png')










