import cv2


detector = cv2.QRCodeDetector()

"""
3 variable pour recuperer la valeur du qr code, les point qui le compose (comme
il s'agit d'une image), et les données contextuelles du qr code
"""
val, points, qrcode = detector.detectAndDecode(cv2.imread("qrcode.png"))

print(val)
