from PyQt5.QtGui import QStandardItem, QStandardItemModel, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QSizePolicy
from Utilità.User_int_utility import User_int_utility


class VistaVisualizzaFilm(QWidget):
    def __init__(self, titolo, callback, parent=None):
        super(VistaVisualizzaFilm, self).__init__()
        self.setWindowTitle("Visualizzazione film")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)
        ext_layout = QGridLayout()
        ext_layout.setContentsMargins(0, 0, 0, 0)

        self.callback = callback
        self.callback()

        self.titolo = titolo

        self.list_view = User_int_utility.crea_list_view()
        # self.lista_filtrata = self.get_film_by_titolo()
        # self.update_ui()

        butt_layout = QHBoxLayout()
        butt_layout.addWidget(User_int_utility.crea_push_button("Visualizza info", self.show_info_film,
                                                                "Visualizza le informazioni del film selezionato",
                                                                QSizePolicy.Expanding, QSizePolicy.Minimum))
        butt_layout.addWidget(User_int_utility.crea_green_or_red_push_button("Elimina", self.elimina_film_by_index,
                                                           QSizePolicy.Expanding, QSizePolicy.Minimum, "R"))

        ext_layout.addLayout(User_int_utility.crea_banda_superiore("Fi"), 0, 0, 1, 2)
        ext_layout.addWidget(self.list_view, 1, 0)
        ext_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/film_back.png"), QSizePolicy.Minimum,
                                                QSizePolicy.Expanding), 1, 1, 2, 1)
        ext_layout.addLayout(butt_layout, 2, 0)
        self.setLayout(ext_layout)

    def get_film_by_titolo(self):
        pass

    def get_film_by_index(self):
        pass

    def show_info_film(self):
        pass

    def elimina_film_by_index(self):
        pass

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for film in self.lista_filtrata:
            item = QStandardItem()
            item.setText(film.titolo)
            item.setEditable(False)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.callback()