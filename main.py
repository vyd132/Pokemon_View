# import pokepy
# client = pokepy.V2Client()
# print(client.get_pokemon())
import requests,json,ui_mainwindow,pokemon_list_model,random,pokemon_search
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import QSortFilterProxyModel
a=requests.get('https://pokeapi.co/api/v2/pokemon/')
pokemon_list=json.loads(a.content)
print(pokemon_list)
# b=json.loads(a.content)
# print(b)
poklist=pokemon_list_model.PokList()
poklist.rowCount()

sort=QSortFilterProxyModel()
sort.setSourceModel(poklist)
sort.setFilterFixedString('sa')
sort.sort(0)
ui=ui_mainwindow.Ui_MainWindow()
c=QApplication()
main_window=QMainWindow()
ui.setupUi(main_window)
ui.pokemonView.setModel(sort)
# ui.move_left.clicked.connect(poklist.spicok_change)
# ui.move_right.clicked.connect(poklist.spicok_change)
main_window.show()
c.exec()

pok_search=pokemon_search.PokemonSearch(ui.centralwidget)


#
# def fill_window():