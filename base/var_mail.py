import os

# variable d'environnement 
# creer une variable d'environnement dans parametre windows 
#enregistrer la valeur 
#on ensuite y acceder de partout

email_user = os.environ.get('EMAIL_USER')

email_pass = os.environ.get('EMAIL_PASS')



print(email_user)
print(email_pass)









