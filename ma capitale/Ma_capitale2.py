import random
import json




"""
data = json.loads(open('pays_capitale.json').read())

print(data["Nigeria"])

indice = random.randrange(0, len(data))
print(indice)
"""
read_file = open('pays.txt', 'r')
data = read_file.read()
read_file.close()

print(data)

