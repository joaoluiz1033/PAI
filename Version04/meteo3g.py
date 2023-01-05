import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime
from meteo3c import Controler
import sys

# TODO : remplacer QGroupBox par QWidget pour supprimer les cadres et les titres de widget.
# QgroupBox permet ici de visualiser graphiquement la layout de l'application.

class ChartsWidget(QWidget):
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)        
        layout = QVBoxLayout()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.draw()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.drawgraph()

    def drawgraph(self):
        ax = self.figure.add_subplot(111)
        ax.set_title("graphique de test", fontsize=10)
        x = list(range(20))
        y = [random.random() for _ in x]
        ax.plot(x, y)
        self.figure.tight_layout()
        self.canvas.draw()

    def refresh(self):
        self.figure.clf()
        ax = self.figure.add_subplot()
        ville = sel.controler.town
        date = self.controler.date
        data = self.controler.data
        temperatures = [measure.temperature for mesure in data if mesure.date == date ] 
        heures = [mesure.date.strftime("%H:%M") for mesure in data if mesure.date == date ]
        ax.plot(heures, temperature)
        self.canvas.draw()
        


class LogWidget(QTextEdit):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)
        self.setFixedHeight(150)
        self.setReadOnly(True)
        self.append("LogWidget")        

    def refresh(self):
        message = self.controler.message        
        if message:
            self.append(message)


class ParamsWidget(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.controler = controler
        self.controler.addClient(self)        
        self.setFixedWidth(300)        
        combo=QComboBox()
        sorted_towns = sorted(controler.towns.keys())
        combo.addItems(sorted_towns)
        combo.currentTextChanged.connect(self.controler.select_town_by_name)
        calendar = QCalendarWidget()
        calendar.setMinimumDate(datetime(2016,1,1))
        calendar.setMaximumDate(datetime(2018,12,31))
        calendar.clicked.connect(self.on_calendar_clicked)
        layout=QVBoxLayout()
        layout.addWidget(combo)
        layout.addWidget(calendar)
        layout.addStretch()
        self.setLayout(layout)        
    
    def on_calendar_clicked(self, date):
        self.controler.select_date(date)        
        
    def refresh(self):
        print("Mise à jour", self.controler.date)    
    
    def call_select(self):
        town=self.combo.currentText()
        self.controler.select_town_by_name(town)

    
class MainWidget(QWidget):
    
    def __init__(self, parent, controler):
        super().__init__(parent)
        self.setMinimumSize(640, 480)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.paramswidget = ParamsWidget(self, controler)
        self.chartswidget = ChartsWidget(self, controler)
        self.logwidget = LogWidget(self, controler)
        hlayout.addWidget(self.paramswidget, 0)
        hlayout.addWidget(self.chartswidget, 1)
        vlayout.addLayout(hlayout, 1)
        vlayout.addWidget(self.logwidget, 0)
        self.setLayout(vlayout)


class MainWindow(QMainWindow):
    
    def __init__(self, controler):
        super().__init__()
        self.setWindowTitle("TITLE")
        self.mainwidget = MainWidget(self, controler)
        self.setCentralWidget(self.mainwidget)


def main():
    app = QApplication([])
    controler = Controler()
    win = MainWindow(controler)
    controler.__init__()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()