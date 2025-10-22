# import pokepy
# client = pokepy.V2Client()
# print(client.get_pokemon())
import requests,json,ui_mainwindow,pokemon_list_model,random,pokemon_search,ui_widget,pokemon_widget,imageWindowMain
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



# ui.Pokwidget.hide()
ui.tableView.setModel(poklist)
ui.pokemonView.setModel(poklist)


pokwidget=pokemon_widget.Pok_Widget(ui.Pokwidget)
# image_main_widget=imageWindowMain.Image_Mian_Window(None)

def aba():
    print(ui.pokemonView.currentIndex())
    model=ui.pokemonView.model()
    index=ui.pokemonView.currentIndex()
    if not index.isValid():
        return
    index_url=model.index(index.row(),1)
    pokwidget.widget_change(model.data(index_url))


# ui.pokemonView.clicked.connect(aba)
# b.selectionChanged.connect(aba)



pok_search1=pokemon_search.PokemonSearch(ui.pokemonView)


ui.pokemonView.selectionModel().currentChanged.connect(aba)


main_window.show()
c.exec()




#
# def fill_window():