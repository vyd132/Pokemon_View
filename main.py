# import pokepy
# client = pokepy.V2Client()
# print(client.get_pokemon())
import requests,json
from PySide6.QtWidgets import QApplication,QMainWindow
a=requests.get('https://pokeapi.co/api/v2/pokemon/1')
print(a.content)
# b=json.loads(a.content)
# print(b)

c=QApplication()
d=QMainWindow()

d.show()
c.exec()