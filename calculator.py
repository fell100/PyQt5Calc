# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percent = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("%"))
        self.percent.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percent.setFont(font)
        self.percent.setObjectName("percent")
        self.clear = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("c"))
        self.clear.setGeometry(QtCore.QRect(99, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.clear_all = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("ac"))
        self.clear_all.setGeometry(QtCore.QRect(188, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clear_all.setFont(font)
        self.clear_all.setObjectName("clear_all")
        self.divide = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("/"))
        self.divide.setGeometry(QtCore.QRect(276, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divide.setFont(font)
        self.divide.setObjectName("divide")
        self.b7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("7"))
        self.b7.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b7.setFont(font)
        self.b7.setObjectName("b7")
        self.b9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("9"))
        self.b9.setGeometry(QtCore.QRect(188, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b9.setFont(font)
        self.b9.setObjectName("b9")
        self.b8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("8"))
        self.b8.setGeometry(QtCore.QRect(99, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b8.setFont(font)
        self.b8.setObjectName("b8")
        self.multiply = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("*"))
        self.multiply.setGeometry(QtCore.QRect(276, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiply.setFont(font)
        self.multiply.setObjectName("multiply")
        self.b4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("4"))
        self.b4.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.b6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("6"))
        self.b6.setGeometry(QtCore.QRect(188, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b6.setFont(font)
        self.b6.setObjectName("b6")
        self.b2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("2"))
        self.b2.setGeometry(QtCore.QRect(99, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("5"))
        self.b5.setGeometry(QtCore.QRect(99, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b5.setFont(font)
        self.b5.setObjectName("b5")
        self.b1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("1"))
        self.b1.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.sum = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("+"))
        self.sum.setGeometry(QtCore.QRect(276, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sum.setFont(font)
        self.sum.setObjectName("sum")
        self.subtract = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("-"))
        self.subtract.setGeometry(QtCore.QRect(276, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.subtract.setFont(font)
        self.subtract.setObjectName("subtract")
        self.b3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("3"))
        self.b3.setGeometry(QtCore.QRect(188, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.plus_minus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("+/-"))
        self.plus_minus.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plus_minus.setFont(font)
        self.plus_minus.setObjectName("plus_minus")
        self.b0 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("0"))
        self.b0.setGeometry(QtCore.QRect(99, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.b0.setFont(font)
        self.b0.setObjectName("b0")
        self.decimal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("."))
        self.decimal.setGeometry(QtCore.QRect(188, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimal.setFont(font)
        self.decimal.setObjectName("decimal")
        self.equal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press("="))
        self.equal.setGeometry(QtCore.QRect(276, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equal.setFont(font)
        self.equal.setObjectName("equal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def result(self):
        aux = ""
        final = ""
        if "+" in self.outputLabel.text():
            aux = self.outputLabel.text().split("+")
            if aux[1] != "":
                try:
                    aux = list(map(int, aux))
                except:
                    aux = list(map(float, aux))
                final = str(sum(aux))
            else:
                final = str(aux[0])
        elif "-" in self.outputLabel.text():
            aux = self.outputLabel.text().split("-")
            if aux[1] != "":
                try:
                    aux = list(map(int, aux))
                except:
                    aux = list(map(float, aux))
                final = str(aux[0]-aux[1])
            else:
                final = str(aux[0])
        elif "*" in self.outputLabel.text():
            aux = self.outputLabel.text().split("*")
            if aux[1] != "":
                try:
                    aux = list(map(int, aux))
                except:
                    aux = list(map(float, aux))
                final = str(aux[0]*aux[1])
            else:
                final = str(aux[0])
        elif "/" in self.outputLabel.text():
            aux = self.outputLabel.text().split("/")
            if aux[1] != "":
                try:
                    aux = list(map(int, aux))
                except:
                    aux = list(map(float, aux))
                final = str(aux[0]/aux[1])
            else:
                final = str(aux[0])
        return final

    def press(self, pressed):
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        operations = ["/","*","+","-"]
        exceptions = ["+/-","%"]
        aux = ""
        index = 0
        isvalue = False
        text = self.outputLabel.text()
        if text != "Error":
            if pressed == "ac":
                self.outputLabel.setText("0")
            else:
                if text == "0":
                    if pressed in operations:
                        self.outputLabel.setText(f'{text}{pressed}')
                    elif pressed == ".":
                        self.outputLabel.setText(f'{text}{pressed}')
                    elif pressed in exceptions or pressed == "c":
                        self.outputLabel.setText("0")
                    elif pressed in numbers:
                        self.outputLabel.setText(pressed)      
                else:
                    if pressed == "%":
                        aux = str(float(text)/100)
                        if len(aux) > 8:
                            self.outputLabel.setText("Error")
                        else:
                            self.outputLabel.setText(aux)
                    elif pressed == "c":
                        self.outputLabel.setText(text[:-1])
                    elif pressed == "+/-":
                        try:
                            aux = str(int(text)*(-1))
                        except:
                            try:
                                aux = str(float(text)*(-1))
                            except:
                                text = text[:-1]
                                try:
                                    aux = str(int(text)*(-1))
                                except:
                                    aux = str(float(text)*(-1))
                        self.outputLabel.setText(aux)
                    elif pressed in operations:
                        for i in range(4):
                            try:
                                index = text.index(operations[i])
                                isvalue = True 
                            except: pass      
                        if isvalue:
                            aux = text.split(text[index])
                            if len(aux) == 2:
                                if aux[1] != "":
                                    temp = self.result()
                                    if len(temp) > 8:
                                        self.outputLabel.setText("Error")
                                    else:
                                        self.outputLabel.setText(f'{temp}{pressed}')
                                else:
                                    self.outputLabel.setText(str(aux[0])+pressed)
                            else:
                                self.outputLabel.setText(f'{text}{pressed}')
                        else:
                            self.outputLabel.setText(f'{text}{pressed}')
                    elif pressed == "=":
                        temp = self.result()
                        if len(temp) > 8:
                            self.outputLabel.setText("Error")
                        else:
                            self.outputLabel.setText(f'{temp}')
                    elif pressed == ".":
                        for i in range(4):
                            try:
                                index = text.index(operations[i])
                                isvalue = True 
                            except: pass
                        if isvalue:
                            aux = text.split(text[index])
                            if len(aux) == 2:
                                if aux[1] != "":
                                    if "." in aux[1]:
                                        self.outputLabel.setText(text)
                                    else:
                                        self.outputLabel.setText(f'{text}{pressed}')
                                else:
                                    self.outputLabel.setText(text)
                            else:
                                self.outputLabel.setText(text)
                        else:
                            if "." in text:
                                self.outputLabel.setText(text)
                            else:
                                self.outputLabel.setText(f'{text}{pressed}')
                    else:
                        for i in range(4):
                            try:
                                index = text.index(operations[i])
                                isvalue = True 
                            except: pass
                        if isvalue:
                            aux = text.split(text[index])
                            if len(aux) == 2:
                                if aux[1] != "":
                                    if len(aux[1]) == 8:
                                        self.outputLabel.setText(f'{text}')
                                    else:
                                        self.outputLabel.setText(f'{text}{pressed}')
                                else:
                                    self.outputLabel.setText(f'{text}{pressed}')
                        else:
                            if len(text) == 8:
                                self.outputLabel.setText(text)
                            else:  
                                self.outputLabel.setText(f'{text}{pressed}')
        else:
            self.outputLabel.setText("0")        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percent.setText(_translate("MainWindow", "%"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.clear_all.setText(_translate("MainWindow", "AC"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.b7.setText(_translate("MainWindow", "7"))
        self.b9.setText(_translate("MainWindow", "9"))
        self.b8.setText(_translate("MainWindow", "8"))
        self.multiply.setText(_translate("MainWindow", "x"))
        self.b4.setText(_translate("MainWindow", "4"))
        self.b6.setText(_translate("MainWindow", "6"))
        self.b2.setText(_translate("MainWindow", "2"))
        self.b5.setText(_translate("MainWindow", "5"))
        self.b1.setText(_translate("MainWindow", "1"))
        self.sum.setText(_translate("MainWindow", "+"))
        self.subtract.setText(_translate("MainWindow", "-"))
        self.b3.setText(_translate("MainWindow", "3"))
        self.plus_minus.setText(_translate("MainWindow", "+/-"))
        self.b0.setText(_translate("MainWindow", "0"))
        self.decimal.setText(_translate("MainWindow", "."))
        self.equal.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
