from PyQt5 import QtCore, QtGui, QtWidgets
from math import pi
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 600)
        MainWindow.setMinimumSize(QtCore.QSize(470, 600))
        MainWindow.setMaximumSize(QtCore.QSize(470, 600))
        MainWindow.setBaseSize(QtCore.QSize(470, 600))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 450, 80))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("background-color:#FFFFFF;")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 481, 121))
        self.frame.setStyleSheet("background-color:#FFB718;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(180, 80, 20, 61))
        self.frame_4.setStyleSheet("background-color:#FFB718;\n"
"opacity: 0.7;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(20, 10, 20, 41))
        self.frame_6.setStyleSheet("background-color:#FFB718;\n"
"opacity: 0.7;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 120, 452, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TriBase = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TriBase.sizePolicy().hasHeightForWidth())
        self.TriBase.setSizePolicy(sizePolicy)
        self.TriBase.setMinimumSize(QtCore.QSize(119, 35))
        self.TriBase.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.TriBase.setFont(font)
        self.TriBase.setStyleSheet("border:1px solid black;")
        self.TriBase.setObjectName("TriBase")
        self.gridLayout.addWidget(self.TriBase, 2, 1, 1, 1)
        self.ButtonRes_Sqr = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonRes_Sqr.sizePolicy().hasHeightForWidth())
        self.ButtonRes_Sqr.setSizePolicy(sizePolicy)
        self.ButtonRes_Sqr.setMinimumSize(QtCore.QSize(75, 35))
        self.ButtonRes_Sqr.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonRes_Sqr.setFont(font)
        self.ButtonRes_Sqr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonRes_Sqr.setStyleSheet("QPushButton{\n"
"border:2px solid #ffb718;\n"
"background-color: #FFFFFF;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#fafafa;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#f1c565;\n"
"color:white;\n"
"border:2px solid white;\n"
"}")
        self.ButtonRes_Sqr.setObjectName("ButtonRes_Sqr")
        self.gridLayout.addWidget(self.ButtonRes_Sqr, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 4)
        self.TriHeight = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.TriHeight.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TriHeight.sizePolicy().hasHeightForWidth())
        self.TriHeight.setSizePolicy(sizePolicy)
        self.TriHeight.setMinimumSize(QtCore.QSize(119, 35))
        self.TriHeight.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.TriHeight.setFont(font)
        self.TriHeight.setStyleSheet("border:1px solid black;")
        self.TriHeight.setObjectName("TriHeight")
        self.gridLayout.addWidget(self.TriHeight, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 4)
        spaceritem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spaceritem2, 6, 0, 1, 4)
        self.SqrSide = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SqrSide.sizePolicy().hasHeightForWidth())
        self.SqrSide.setSizePolicy(sizePolicy)
        self.SqrSide.setMinimumSize(QtCore.QSize(243, 35))
        self.SqrSide.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SqrSide.setFont(font)
        self.SqrSide.setStyleSheet("border:1px solid black;")
        self.SqrSide.setObjectName("SqrSide")
        self.gridLayout.addWidget(self.SqrSide, 5, 0, 1, 2)
        self.Res_Tri = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Res_Tri.sizePolicy().hasHeightForWidth())
        self.Res_Tri.setSizePolicy(sizePolicy)
        self.Res_Tri.setMinimumSize(QtCore.QSize(119, 35))
        self.Res_Tri.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Res_Tri.setFont(font)
        self.Res_Tri.setStyleSheet("border:1px solid black;")
        self.Res_Tri.setObjectName("Res_Tri")
        self.gridLayout.addWidget(self.Res_Tri, 2, 3, 1, 1)
        self.Res_Sqr = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Res_Sqr.sizePolicy().hasHeightForWidth())
        self.Res_Sqr.setSizePolicy(sizePolicy)
        self.Res_Sqr.setMinimumSize(QtCore.QSize(119, 35))
        self.Res_Sqr.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Res_Sqr.setFont(font)
        self.Res_Sqr.setStyleSheet("border:1px solid black;")
        self.Res_Sqr.setObjectName("Res_Sqr")
        self.gridLayout.addWidget(self.Res_Sqr, 5, 3, 1, 1)
        self.ButtonRes_Tri = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonRes_Tri.sizePolicy().hasHeightForWidth())
        self.ButtonRes_Tri.setSizePolicy(sizePolicy)
        self.ButtonRes_Tri.setMinimumSize(QtCore.QSize(75, 35))
        self.ButtonRes_Tri.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonRes_Tri.setFont(font)
        self.ButtonRes_Tri.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonRes_Tri.setStyleSheet("QPushButton{\n"
"border:2px solid #ffb718;\n"
"background-color: #FFFFFF;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#fafafa;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#f1c565;\n"
"color:white;\n"
"border:2px solid white;\n"
"}")
        self.ButtonRes_Tri.setCheckable(False)
        self.ButtonRes_Tri.setObjectName("ButtonRes_Tri")
        self.gridLayout.addWidget(self.ButtonRes_Tri, 2, 2, 1, 1)
        self.CirRad = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CirRad.sizePolicy().hasHeightForWidth())
        self.CirRad.setSizePolicy(sizePolicy)
        self.CirRad.setMinimumSize(QtCore.QSize(243, 35))
        self.CirRad.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.CirRad.setFont(font)
        self.CirRad.setStyleSheet("border:1px solid black;")
        self.CirRad.setObjectName("CirRad")
        self.gridLayout.addWidget(self.CirRad, 8, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 4)
        self.Res_Cir = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Res_Cir.sizePolicy().hasHeightForWidth())
        self.Res_Cir.setSizePolicy(sizePolicy)
        self.Res_Cir.setMinimumSize(QtCore.QSize(119, 35))
        self.Res_Cir.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Res_Cir.setFont(font)
        self.Res_Cir.setStyleSheet("border:1px solid black;")
        self.Res_Cir.setObjectName("Res_Cir")
        self.gridLayout.addWidget(self.Res_Cir, 8, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(2, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 4)
        self.ButtonRes_Cir = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonRes_Cir.sizePolicy().hasHeightForWidth())
        self.ButtonRes_Cir.setSizePolicy(sizePolicy)
        self.ButtonRes_Cir.setMinimumSize(QtCore.QSize(75, 35))
        self.ButtonRes_Cir.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonRes_Cir.setFont(font)
        self.ButtonRes_Cir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonRes_Cir.setStyleSheet("QPushButton{\n"
"border:2px solid #ffb718;\n"
"background-color: #FFFFFF;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#fafafa;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#f1c565;\n"
"color:white;\n"
"border:2px solid white;\n"
"}")
        self.ButtonRes_Cir.setObjectName("ButtonRes_Cir")
        self.gridLayout.addWidget(self.ButtonRes_Cir, 8, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(-20, 109, 490, 591))
        self.frame_3.setStyleSheet("background-color:#FFFFFF;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setGeometry(QtCore.QRect(310, -40, 181, 601))
        self.frame_2.setStyleSheet("background-color:#F1C565;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(320, 10, 20, 41))
        self.frame_5.setStyleSheet("background-color:#FFB718;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_3.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.gridLayoutWidget.raise_()
        self.frame_6.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def ResTri():
            bibik1=False
            bibik2=False
            l=""
            h=self.TriHeight.text()
            base=self.TriBase.text()
            if h=="" or base=="":
                self.Res_Tri.setText(str())
            else:
                for i in range(ord("A"), ord("Z")+1):
                    l+=chr(i)
                    l+=","
                for i in range(ord("a"),ord("z")+1):
                    l+=chr(i)
                    l+=","
                for i in range(ord("А"),ord("Я")+1):
                    l+=chr(i)
                    l+=","
                for i in range(ord("а"),ord("я")+1):
                    l+=chr(i)
                    l+=","
                for i in range(0,len(h)):
                    for g in range(0,len(l)-1):
                        if h[i]==l[g] and bibik1==False:
                            bibik1=True
                for i in range(0,len(base)):
                    for g in range(0,len(l)-1):
                        if base[i]==l[g] and bibik2==False:
                            bibik2=True
                if bibik1==True or bibik2==True:
                    self.Res_Tri.setText(str("Invalid input"))
                else:
                    h=float(h)
                    base=float(base)
                    if h<0 or base<0:
                        self.Res_Tri.setText(str("Invalid input"))
                    else:
                        Tri=h*base*0.5
                        self.Res_Tri.setText(str("%.2f" % Tri))
        def ResSqr():
            bibik=False
            l=""
            Sqr=self.SqrSide.text()
            if Sqr=="":
                self.Res_Sqr.setText(str())
            else:
                for i in range(ord("A"), ord("Z")+1):
                    l+=chr(i)
                    l+=","
                for i in range(ord("a"),ord("z")+1):
                    l+=chr(i)
                    l+=","
                for i in range(ord("А"),ord("Я")+1):
                    l+=chr(i)
                    l+=","
                for i in range(ord("а"),ord("я")+1):
                    l+=chr(i)
                    l+=","
                for i in range(0,len(Sqr)):
                    for g in range(0,len(l)-1):
                        if Sqr[i]==l[g] and bibik==False:
                            bibik=True
                if bibik==True:
                    self.Res_Sqr.setText(str("Invalid input"))
                else:
                    Sqr=float(Sqr)
                    if Sqr<0:
                        self.Res_Sqr.setText(str("Invalid input"))
                    else:
                        Sqr=Sqr**2
                        self.Res_Sqr.setText(str("%.2f" % Sqr))
        def ResCir():
            bibik=False
            l=""
            Cir=self.CirRad.text()
            if Cir=="":
                self.Res_Cir.setText(str())
            else:
                for i in range(ord("A"), ord("Z")+1):
                    l+=chr(i)
                    l+=","
                for i in range(ord("a"),ord("z")+1):
                    l+=chr(i)
                    l+=","
                for i in range(ord("А"),ord("Я")+1):
                    l+=chr(i)
                    l+=","
                for i in range(ord("а"),ord("я")+1):
                    l+=chr(i)
                    l+=","
                for i in range(0,len(Cir)):
                    for g in range(0,len(l)-1):
                        if Cir[i]==l[g] and bibik==False:
                            bibik=True
                if bibik==True:
                    self.Res_Cir.setText(str("Invalid input"))
                else:
                    Cir=float(Cir)
                    if Cir<0:
                        self.Res_Cir.setText(str("Invalid input"))
                    else:
                        Cir=Cir**2*pi
                        self.Res_Cir.setText(str("%.2f" % Cir))
        self.TriHeight.setPlaceholderText("Высота")
        self.TriBase.setPlaceholderText("Осн.")
        self.SqrSide.setPlaceholderText("Сторона")
        self.CirRad.setPlaceholderText("Радиус")
        self.Res_Tri.setPlaceholderText("Ответ")
        self.Res_Sqr.setPlaceholderText("Ответ")
        self.Res_Cir.setPlaceholderText("Ответ")
        self.Res_Tri.setReadOnly(True)
        self.Res_Sqr.setReadOnly(True)
        self.Res_Cir.setReadOnly(True)
        self.ButtonRes_Tri.clicked.connect(ResTri)
        self.ButtonRes_Sqr.clicked.connect(ResSqr)
        self.ButtonRes_Cir.clicked.connect(ResCir)
        
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ВЫЧИСЛЯТОР ПЛОЩАДЕЙ"))
        self.label.setText(_translate("MainWindow", "ВЫЧИСЛЯТОР ПЛОЩАДЕЙ БЕСПЛАТНО"))
        self.ButtonRes_Sqr.setText(_translate("MainWindow", "="))
        self.ButtonRes_Tri.setText(_translate("MainWindow", "="))
        self.label_5.setText(_translate("MainWindow", "Площадь окружности:"))
        self.label_3.setText(_translate("MainWindow", "Площадь треугольника:"))
        self.label_4.setText(_translate("MainWindow", "Площадь квадрата:"))
        self.ButtonRes_Cir.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
