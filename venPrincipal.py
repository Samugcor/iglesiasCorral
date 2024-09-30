# Form implementation generated from reading ui file 'venPrincipal.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        venPrincipal.resize(1092, 769)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/house.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        venPrincipal.setWindowIcon(icon)
        venPrincipal.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        venPrincipal.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.panPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.panPrincipal.setMinimumSize(QtCore.QSize(200, 0))
        self.panPrincipal.setStyleSheet("")
        self.panPrincipal.setObjectName("panPrincipal")
        self.pesClientes = QtWidgets.QWidget()
        self.pesClientes.setObjectName("pesClientes")
        self.gridLayout = QtWidgets.QGridLayout(self.pesClientes)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblDniCliente = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblDniCliente.setObjectName("lblDniCliente")
        self.gridLayout_2.addWidget(self.lblDniCliente, 0, 0, 1, 1)
        self.lblDniCliente_6 = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblDniCliente_6.setObjectName("lblDniCliente_6")
        self.gridLayout_2.addWidget(self.lblDniCliente_6, 3, 7, 1, 1)
        self.txtDniCliente = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDniCliente.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txtDniCliente.setAutoFillBackground(False)
        self.txtDniCliente.setStyleSheet("background-color:rgb(255, 255, 222);")
        self.txtDniCliente.setObjectName("txtDniCliente")
        self.gridLayout_2.addWidget(self.txtDniCliente, 0, 1, 1, 1)
        self.txtDniCliente_5 = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDniCliente_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtDniCliente_5.setText("")
        self.txtDniCliente_5.setObjectName("txtDniCliente_5")
        self.gridLayout_2.addWidget(self.txtDniCliente_5, 2, 5, 1, 4)
        self.label_4 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 2)
        self.lblDniCliente_3 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDniCliente_3.sizePolicy().hasHeightForWidth())
        self.lblDniCliente_3.setSizePolicy(sizePolicy)
        self.lblDniCliente_3.setObjectName("lblDniCliente_3")
        self.gridLayout_2.addWidget(self.lblDniCliente_3, 2, 3, 1, 2)
        self.lblDniCliente_4 = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblDniCliente_4.setObjectName("lblDniCliente_4")
        self.gridLayout_2.addWidget(self.lblDniCliente_4, 3, 0, 1, 1)
        self.txtDniCliente_6 = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDniCliente_6.setMinimumSize(QtCore.QSize(300, 0))
        self.txtDniCliente_6.setObjectName("txtDniCliente_6")
        self.gridLayout_2.addWidget(self.txtDniCliente_6, 3, 1, 1, 2)
        self.lblDniCliente_5 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDniCliente_5.sizePolicy().hasHeightForWidth())
        self.lblDniCliente_5.setSizePolicy(sizePolicy)
        self.lblDniCliente_5.setObjectName("lblDniCliente_5")
        self.gridLayout_2.addWidget(self.lblDniCliente_5, 3, 3, 1, 2)
        self.lblDniCliente_2 = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblDniCliente_2.setObjectName("lblDniCliente_2")
        self.gridLayout_2.addWidget(self.lblDniCliente_2, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 2, 1, 1)
        self.txtDniCliente_4 = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDniCliente_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtDniCliente_4.setObjectName("txtDniCliente_4")
        self.gridLayout_2.addWidget(self.txtDniCliente_4, 2, 1, 1, 1)
        self.txtDniCliente_2 = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDniCliente_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.txtDniCliente_2.setObjectName("txtDniCliente_2")
        self.gridLayout_2.addWidget(self.txtDniCliente_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.pesClientes)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 2, 1, 1)
        self.cmbProvincia = QtWidgets.QComboBox(parent=self.pesClientes)
        self.cmbProvincia.setMinimumSize(QtCore.QSize(120, 0))
        self.cmbProvincia.setObjectName("cmbProvincia")
        self.gridLayout_2.addWidget(self.cmbProvincia, 3, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 1, 6, 1, 1)
        self.chkHistoricoCli = QtWidgets.QCheckBox(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkHistoricoCli.sizePolicy().hasHeightForWidth())
        self.chkHistoricoCli.setSizePolicy(sizePolicy)
        self.chkHistoricoCli.setObjectName("chkHistoricoCli")
        self.gridLayout_2.addWidget(self.chkHistoricoCli, 1, 7, 1, 1)
        self.cmbMunicipio = QtWidgets.QComboBox(parent=self.pesClientes)
        self.cmbMunicipio.setMinimumSize(QtCore.QSize(160, 0))
        self.cmbMunicipio.setObjectName("cmbMunicipio")
        self.gridLayout_2.addWidget(self.cmbMunicipio, 3, 9, 1, 1)
        self.txtDniCliente_3 = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDniCliente_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.txtDniCliente_3.setObjectName("txtDniCliente_3")
        self.gridLayout_2.addWidget(self.txtDniCliente_3, 1, 5, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.btnGrabarCli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnGrabarCli.setMinimumSize(QtCore.QSize(80, 25))
        self.btnGrabarCli.setObjectName("btnGrabarCli")
        self.horizontalLayout.addWidget(self.btnGrabarCli)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.pesClientes)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.pesClientes)
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(parent=self.pesClientes)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.tabClientes = QtWidgets.QTableWidget(parent=self.pesClientes)
        self.tabClientes.setObjectName("tabClientes")
        self.tabClientes.setColumnCount(0)
        self.tabClientes.setRowCount(0)
        self.verticalLayout.addWidget(self.tabClientes)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.panPrincipal.addTab(self.pesClientes, "")
        self.tabEnConstruccion = QtWidgets.QWidget()
        self.tabEnConstruccion.setObjectName("tabEnConstruccion")
        self.label = QtWidgets.QLabel(parent=self.tabEnConstruccion)
        self.label.setGeometry(QtCore.QRect(176, 170, 111, 20))
        self.label.setObjectName("label")
        self.panPrincipal.addTab(self.tabEnConstruccion, "")
        self.gridLayout_3.addWidget(self.panPrincipal, 0, 1, 1, 1)
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=venPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        venPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(parent=venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(venPrincipal)
        self.panPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "InmoTeis"))
        self.lblDniCliente.setText(_translate("venPrincipal", "DNI/CIF"))
        self.lblDniCliente_6.setText(_translate("venPrincipal", "Municipio"))
        self.label_4.setText(_translate("venPrincipal", "Nombre"))
        self.lblDniCliente_3.setText(_translate("venPrincipal", "Movil"))
        self.lblDniCliente_4.setText(_translate("venPrincipal", "Dirección"))
        self.lblDniCliente_5.setText(_translate("venPrincipal", "Provincia"))
        self.lblDniCliente_2.setText(_translate("venPrincipal", "Email"))
        self.label_3.setText(_translate("venPrincipal", "Apellidos"))
        self.chkHistoricoCli.setText(_translate("venPrincipal", "Historico"))
        self.btnGrabarCli.setText(_translate("venPrincipal", "Grabar"))
        self.pushButton_2.setText(_translate("venPrincipal", "Modificar"))
        self.pushButton_3.setText(_translate("venPrincipal", "Eliminar"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.pesClientes), _translate("venPrincipal", "Tab 1"))
        self.label.setText(_translate("venPrincipal", "En construccion"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.tabEnConstruccion), _translate("venPrincipal", "Tab 2"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
