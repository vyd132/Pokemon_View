# import pokepy
# client = pokepy.V2Client()
# print(client.get_pokemon())
import requests,json,ui_mainwindow,pokemon_list_model
from PySide6.QtWidgets import QApplication,QMainWindow
a=requests.get('https://pokeapi.co/api/v2/pokemon/1')
print(a.content)
# b=json.loads(a.content)
# print(b)
poklist=pokemon_list_model.PokList()
ui=ui_mainwindow.Ui_MainWindow()
c=QApplication()
main_window=QMainWindow()
ui.setupUi(main_window)
ui.pokemonView.setModel(poklist)
main_window.show()
c.exec()
#
# def fill_window():