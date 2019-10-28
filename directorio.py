from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Directorio(object):
    
    def setupUi(self, Directorio):
        Directorio.setObjectName("Directorio")
        Directorio.resize(443, 406)
        self.gridLayout = QtWidgets.QGridLayout(Directorio)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Directorio)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vistaDirectorio = QtWidgets.QTreeView(self.frame_2)
        self.vistaDirectorio.setToolTip("")
        self.vistaDirectorio.setStatusTip("")
        self.vistaDirectorio.setWhatsThis("")
        self.vistaDirectorio.setAccessibleName("")
        self.vistaDirectorio.setAccessibleDescription("")
        self.vistaDirectorio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vistaDirectorio.setAutoScroll(False)
        self.vistaDirectorio.setObjectName("vistaDirectorio")
        self.vistaDirectorio.header().setDefaultSectionSize(350)
        self.vistaDirectorio.header().setMinimumSectionSize(50)
        self.gridLayout_3.addWidget(self.vistaDirectorio, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnCancelarBrowser = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancelarBrowser.sizePolicy().hasHeightForWidth())
        self.btnCancelarBrowser.setSizePolicy(sizePolicy)
        self.btnCancelarBrowser.setObjectName("btnCancelarBrowser")
        self.gridLayout_4.addWidget(self.btnCancelarBrowser, 0, 1, 1, 1)
        self.btnAbrirCarpeta = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAbrirCarpeta.sizePolicy().hasHeightForWidth())
        self.btnAbrirCarpeta.setSizePolicy(sizePolicy)
        self.btnAbrirCarpeta.setObjectName("btnAbrirCarpeta")
        self.gridLayout_4.addWidget(self.btnAbrirCarpeta, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Directorio)
        QtCore.QMetaObject.connectSlotsByName(Directorio)
        
        
        
        
        
        
    
        

    def retranslateUi(self, Directorio):
        _translate = QtCore.QCoreApplication.translate
        Directorio.setWindowTitle(_translate("Directorio", "Directorio"))
        self.btnCancelarBrowser.setText(_translate("Directorio", "Cancelar"))
        self.btnAbrirCarpeta.setText(_translate("Directorio", "Abrir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Directorio = QtWidgets.QDialog()
    ui = Ui_Directorio()
    ui.setupUi(Directorio)
    Directorio.show()
    sys.exit(app.exec_())

