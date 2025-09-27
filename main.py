# import pokepy
# client = pokepy.V2Client()
# print(client.get_pokemon())
import requests,json,ui_mainwindow,pokemon_list_model,random,pokemon_search
from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter
from PySide6.QtCore import QSortFilterProxyModel
a=requests.get('https://pokeapi.co/api/v2/pokemon/')
pokemon_list=json.loads(a.content)
print(pokemon_list)
# b=json.loads(a.content)
# print(b)
poklist=pokemon_list_model.PokList()
poklist.rowCount()
search=QCompleter(poklist)




c=QApplication()
main_window=QMainWindow()

ui=ui_mainwindow.Ui_MainWindow()
ui.setupUi(main_window)


pok_search1=pokemon_search.PokemonSearch(ui.pokemonView)
pok_search2=pokemon_search.PokemonSearch(ui.poklist)


main_window.show()
c.exec()




#
# def fill_window():