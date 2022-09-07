import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart




# activer dans les parametre gmail l'onglet securité --> appareil non securisé l'autorisatio pour que sa fonctionne





















# mettre ene place un serveur
server = smtplib.SMTP('smtp.gmail.com', 25)  # l'adress du serveur smtp depend du fournisseur  ,port 25 pour le smtp

server.starttls()

# se connecte a notre compte gmail
# server.login('email', 'password') # pas recommander


with open('password.txt', 'r') as f:
    password = f.read()

#password = input(str("entrez votre mot de passee : "))

server.login("adikpetoiudhael@gmail.com", password)
print("Connexion réussit")
print("Envoi...")

# creer le message avec des pieces jointe

msg = MIMEMultipart()
msg['From'] = 'judi'
msg['To'] = 'landryespere@gmail.com'
msg['Subject'] = 'just un test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
# piece jointe
attachment = open(filename, 'rb')  # l'image est lu en binaire

# creer une charge utile d'objet
p = MIMEBase('application', 'octet-stream')  # octet-stream est un flux pour traiter l'image

p.set_payload(attachment.read())

encoders.encode_base64(p)

# ajouter une entete a p(piece jointe)
p.add_header('Content-Disposition', f'attachment; filename{filename}')
# attacher la piece jointe au message
msg.attach(p)

text = msg.as_string()  # obtenir le tout sous forme de chaine
server.sendmail('adikpetoiudhael@gmail.com', 'landryespere@gmail.com', text)
print("Mail envoyé !!")