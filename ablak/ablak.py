from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel(self)
        self.label1.setText('Még nyilnak')
        self.label1.move(100, 100)

        button1 = QPushButton(self)
        button1.setText('Ceg.hu')
        button1.move(100,130)
        button1.clicked.connect(self.on_click_mehet_button)

        self.edit1 = QLineEdit(self)
        self.edit1.move(100, 180)


        self.setGeometry(100, 100, 750, 600)
        self.setWindowTitle('Itt vagyok')
        self.show()
    
    def on_click_mehet_button(self):
        print('mükszik')
        szoveg  = self.edit1.text()
        self.label1.setText(szoveg)
        self.setWindowTitle('IDK why its working')


application = QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(application.exec_())