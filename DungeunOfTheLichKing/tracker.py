from random import randint
from PyQt5 import QtCore, QtGui
import sys

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QStatusBar, QMenuBar, QPushButton, QListWidget, \
    QWidget, QLabel

import BattleFunction
import Traderf


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        """Создание фона игры"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#MainWindow{border-image:url(Background.png)}")
        """Полноэкранный режим"""
        MainWindow.setWindowState((MainWindow.windowState() &
                                   ~(QtCore.Qt.WindowMinimized | QtCore.Qt.WindowMaximized))
                                  | QtCore.Qt.WindowFullScreen)
        """Создание текстового поля"""
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(36)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QRect(420, 440, 515, 200))
        self.listWidget.setObjectName("listWidget")
        ###############################################################################
        """Раздел создающий лейблы для изображений и размещение спрайтов"""
        self.label6 = QLabel(self.centralwidget)
        self.label6.move(429, 10)
        self.label6.show()

        self.label5 = QLabel(self.centralwidget)
        self.label5.move(429, 10)
        self.label5.show()

        self.label4 = QLabel(self.centralwidget)
        self.label4.move(429, 10)
        self.label4.show()

        self.label3 = QLabel(self.centralwidget)
        self.label3.move(429, 10)
        self.label3.show()

        self.label2 = QLabel(self.centralwidget)
        self.label2.move(429, 10)
        self.label2.show()



        self.label = QLabel(self.centralwidget)
        self.label.move(429, 10)
        self.pixmap = QPixmap('Lady.jpg')
        self.pixmap = self.pixmap.scaled(500, 400)
        self.pixmap = self.pixmap.scaled(self.pixmap.width(), self.pixmap.height())
        self.label.setPixmap(self.pixmap)
        #######################################################################################

        self.listWidget.addItem(
            "С древних врёмен, когда боги ходили по земле, существовала страна под названием\nАльбион!\n"
            "Жили в ней храбрые рыцари, сталью и кровью они служили своей Вечной Королёве и \nбыли защитниками своей страны.\n"

            "Но злой Король Лич напал на великое королевство.\n"
            "Убив Лорда защитника и похитив его дочь он скрылся в своём древнем подземелье.\n"

            "Большинство рыцарей либо пали, либо в далёких землях, о храбрый рыцарь,\n"
            "тебе предстоит спасти принцессу и защитить свою родину! \n"
            "Но помни, Лич поднял мертвых на свою сторону, сможешь ли ты победить?")
        """Создание вводного текста"""
#################################Создание кнопок#################################################################
        self.pushButton = QPushButton("Продолжить", self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 640, 101, 41))

        self.pushButton_2 = QPushButton("Зелье здоровья", self.centralwidget)
        self.pushButton_2.setGeometry(QRect(720, 640, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
##################################################################################################
        """Создание меню"""
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QMenu("Меню", self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.action_2 = QAction("Выход")
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowTitle("Игра")
        self.action_2.triggered.connect(self.Exit)
        self.pushButton.clicked.connect(self.BattleFunction)  # чтобы вызвать функцию битвы
        self.pushButton_2.clicked.connect(self.XP)
        """Создание кнопок торговца"""
        self.pushButton_3 = QPushButton("Купить зелье\n здоровья", self.centralwidget)
        self.pushButton_3.setGeometry(QRect(950, 500, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QPushButton("Заточить меч", self.centralwidget)
        self.pushButton_4.setGeometry(QRect(950, 550, 101, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3.hide()
        self.pushButton_4.hide()


    def BattleFunction(self):
        """Уберание всех изобращений с экрана"""
        self.label6.hide()
        self.label5.hide()
        self.label4.hide()
        self.label3.hide()
        self.label2.hide()
        self.label.hide()
        """Уберание кнопок торговца"""
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.listWidget.clear()
        rand = randint(1, 100)
        """Определение рандомных моментов"""
        if rand <= 20:
            """Появление кнопкок и вызов модуля торговца"""
            self.pushButton_3.show()
            self.pushButton_4.show()
            self.pushButton_3.clicked.connect(self.Health)
            self.pushButton_4.clicked.connect(self.Batt)
            Traderf.Trad.Trader(self)  # функция для торговца

        else:
            BattleFunction.clicked.clicked_resum(self) # вызов модуля битвы

    def Health(self):
        """Функция покупки зелий"""
        Traderf.Trad.Health_Po(self)

    def Batt(self):
        """Функция уселения персонажа"""
        Traderf.Trad.Bat(self)

    def XP(self):
        """Функция выстоновление здоровья"""
        BattleFunction.Health.Health_Potion(self)

    def Exit(self):
        """Функция выхода из игры"""
        self.close
######################################Появление спрайтов персонажей#####################################################
    def Artmaus(self):

        image = 'Art/maus.jpg'
        self.pixmap = QPixmap(image)
        self.pixmap = self.pixmap.scaled(500, 400)
        self.pixmap = self.pixmap.scaled(self.pixmap.width(), self.pixmap.height())
        self.label2.setPixmap(self.pixmap)
        self.label2.adjustSize()
        self.label2.show()

    def ArtSkeleton(self):
        image = 'Art/Skeleton.jpg'
        self.pixmap = QPixmap(image)
        self.pixmap = self.pixmap.scaled(500, 400)
        self.pixmap = self.pixmap.scaled(self.pixmap.width(), self.pixmap.height())
        self.label3.setPixmap(self.pixmap)
        self.label3.adjustSize()
        self.label3.show()

    def ArtZombie(self):
        image = 'Art/Zombie.jpg'
        self.pixmap = QPixmap(image)
        self.pixmap = self.pixmap.scaled(500, 400)
        self.pixmap = self.pixmap.scaled(self.pixmap.width(), self.pixmap.height())
        self.label4.setPixmap(self.pixmap)
        self.label4.adjustSize()
        self.label4.show()

    def ArtLichboss(self):
        image = 'Art/Lichboss.jpg'
        self.pixmap = QPixmap(image)
        self.pixmap = self.pixmap.scaled(500, 400)
        self.pixmap = self.pixmap.scaled(self.pixmap.width(), self.pixmap.height())
        self.label5.setPixmap(self.pixmap)
        self.label5.adjustSize()
        self.label5.show()

    def ArtTrader(self):
        image = 'Art/Trader.jpg'
        self.pixmap = QPixmap(image)
        self.pixmap = self.pixmap.scaled(500, 430)
        self.pixmap = self.pixmap.scaled(self.pixmap.width(), self.pixmap.height())
        self.label6.setPixmap(self.pixmap)
        self.label6.adjustSize()
        self.label6.show()
########################################################################################################################


"""Раскраска меню"""
qss = """
QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 lightgray, stop:1 darkgray);
}
QMenuBar::item {          
    padding: 5px 20px;
    background-color: rgb(300,105,40);
    color: rgb(255,255,255);  
}
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qss)
    MainWindow.show()
    app.exec()
