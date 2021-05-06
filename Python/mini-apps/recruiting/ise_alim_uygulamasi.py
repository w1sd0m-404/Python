import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QRadioButton, QMessageBox, QCheckBox


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,350,500,200)
        self.setWindowTitle("Özeller A.Ş iş başvurusu")
        self.initUI()
    def initUI(self):
        #isim soyisim ve input alma
        self.name = QtWidgets.QLabel()
        self.name.setText("Ad Soyad: ")
        #
        self.lineName = QtWidgets.QLineEdit()

        #Bilinen diller
        self.lang = QtWidgets.QLabel()
        self.lang.setText("Bildiğiniz diller: ")
        #
        self.us = QCheckBox("İngilizce")
        self.ru = QCheckBox("Rusça")
        self.de = QCheckBox("Almanca")

        #Maaş beklentisi
        self.salary = QtWidgets.QLabel()
        self.salary.setText("Maaş beklentiniz: ")
        #
        self.r1 = QRadioButton("2000-3000")
        self.r2 = QRadioButton("3000-4000")
        self.r3 = QRadioButton("4000-5000")

        #Neden siz
        self.question = QtWidgets.QLabel()
        self.question.setText("Neden siz? ")
        #
        self.textArea = QtWidgets.QTextEdit()

        #Başvuru tamamlama
        self.save = QtWidgets.QPushButton()
        self.save.setText("Başvur")
        self.save.clicked.connect(self.clicked)

        #Yerleştirme
        self.possition(self.name,self.lineName,self.lang,self.us,self.ru,self.de,self.salary,self.r1,self.r2,self.r3,self.question,self.textArea,self.save)
    def possition(self,*args):
        #Yerleştime fonksiyonu
        hBox = QtWidgets.QHBoxLayout()
        vBox = QtWidgets.QVBoxLayout()
        for i in args:
            vBox.addWidget(i)
        hBox.addStretch()
        hBox.addLayout(vBox)
        hBox.addStretch()
        self.setLayout(hBox)
    def clicked(self):
        self.inf = self.name.text() + self.lineName.text()
        arry1 = [self.us,self.ru,self.de]
        arry2 = [self.r1,self.r2,self.r3]
        for i in arry1 :
            if i.isChecked() :
                self.lng = self.lang.text() + i.text()
        for i in arry2:
            if i.isChecked():
                self.slr = self.salary.text() + i.text()
        self.ques = self.question.text() + self.textArea.toPlainText()
        #popup window
        self.popWin(self.inf,self.lng,self.slr,self.ques)
    def popWin(self,*args):
        msg = QMessageBox()
        msg.setWindowTitle("Başvuru")
        msg.setText("Başvuru durumu")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.setInformativeText("Kayıt oluşturulmak üzere...")
        text = ''
        for i in args:
            text += i + "\n"
        msg.setDetailedText(text)
        msg.buttonClicked.connect(self.ok)
        msg.exec_()
    def ok(self,i):
        if i.text() == "&Yes":
            msg = QMessageBox()
            msg.setWindowTitle("Kaydet")
            msg.setText("Başvuru tamamlandı")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Yes)
            msg.exec_()
def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())
window()