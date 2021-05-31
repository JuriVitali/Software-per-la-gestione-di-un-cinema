from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QSpacerItem, QHBoxLayout

from Utilità.User_int_utility import User_int_utility
from Film.Views.VistaAggiungiFilm import VistaAggiungiFilm
from Film.Views.VistaVisualizzaFilm import VistaVisualizzaFilm


class VistaGestisciFilm(QWidget):
    def __init__(self, callback, parent=None):
        super(VistaGestisciFilm, self).__init__()

        self.setWindowTitle("Gestione Film")
        self.setStyleSheet("background-color : " + User_int_utility.primary_color + ";")
        self.setGeometry(0, 0, 1200, 650)
        User_int_utility.sposta_al_centro(self)

        self.callback = callback
        self.callback()

        grid_layout = QGridLayout()
        grid_layout.addWidget(User_int_utility.crea_push_button("Aggiungi film", self.show_new_film,
                                                                "Cliccare per aggiungere un film al sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0)
        grid_layout.addWidget(User_int_utility.crea_push_button("Visualizza tutti i film", self.show_lista_film,
                                                                "Cliccare per visualizzare tutti i film inseriti nel sistema",
                                                                QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        grid_layout.addItem(QSpacerItem(20, 95, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 0, 1, 2)
        grid_layout.addWidget(self.crea_box_ricerca(), 2, 0, 1, 2)
        grid_layout.addWidget(User_int_utility.crea_label_con_imm(QPixmap("Immagini/Sfondi/film_back.png"), QSizePolicy.Minimum, QSizePolicy.Expanding),
                              0, 2, 3, 1)
        grid_layout.setContentsMargins(20,0,0, 0)

        v_layout = QVBoxLayout()
        v_layout.addLayout(User_int_utility.crea_banda_superiore("Fi"))
        v_layout.addLayout(grid_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(v_layout)


    def show_new_film(self):
        self.vista_aggiungi_film = VistaAggiungiFilm(self.modifica_visibilita)
        self.vista_aggiungi_film.show()


    def show_lista_film(self, titolo=None):
        self.vista_lista_film = VistaVisualizzaFilm(self.titolo_ricerca.text(),self.modifica_visibilita)
        self.vista_lista_film.show()

    def crea_box_ricerca(self):
        box = QGroupBox()
        box.setTitle("Cerca un film")
        box.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        box.setStyleSheet("QGroupBox"
                          "{"
                          "background-color: #222;"
                          "border-radius: 8px"
                          "}"
                          "QGroupBox::title"
                          "{"
                          "background-color: " + User_int_utility.tertiary_color + ";"
                          "border-radius: 4px"
                          "}"
                          )
        layout = QHBoxLayout()

        self.titolo_ricerca = User_int_utility.crea_casella_testo()

        layout.addWidget(User_int_utility.crea_label("Titolo"))
        layout.addWidget(self.titolo_ricerca)
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(User_int_utility.crea_push_button("Cerca film", self.show_lista_film,
                                              "Cliccare per ricercare il film",
                                              QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.setContentsMargins(15,35,15,25)
        box.setLayout(layout)
        return box

    def modifica_visibilita(self):
        User_int_utility.modifica_visibilita_finestra(self)

    def closeEvent(self, event):
        self.callback()