# Form implementation generated from reading ui file '.\\templates\\venPrincipal.ui'
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
        venPrincipal.resize(1298, 1160)
        venPrincipal.setMinimumSize(QtCore.QSize(0, 1160))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\\\templates\\../../../../../.designer/backup/img/house.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        venPrincipal.setWindowIcon(icon)
        venPrincipal.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        venPrincipal.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 3, 1, 1)
        self.panPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.panPrincipal.setMinimumSize(QtCore.QSize(200, 0))
        self.panPrincipal.setStyleSheet("")
        self.panPrincipal.setObjectName("panPrincipal")
        self.pesClientes = QtWidgets.QWidget()
        self.pesClientes.setObjectName("pesClientes")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pesClientes)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.pesClientes)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 5, 1, 1, 1)
        self.tabClientes = QtWidgets.QTableWidget(parent=self.pesClientes)
        self.tabClientes.setAlternatingRowColors(True)
        self.tabClientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabClientes.setObjectName("tabClientes")
        self.tabClientes.setColumnCount(7)
        self.tabClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(6, item)
        self.tabClientes.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tabClientes, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, 15, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btnGrabarCli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnGrabarCli.setMinimumSize(QtCore.QSize(80, 25))
        self.btnGrabarCli.setObjectName("btnGrabarCli")
        self.horizontalLayout.addWidget(self.btnGrabarCli)
        self.btnModificarCliente = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnModificarCliente.setMinimumSize(QtCore.QSize(80, 25))
        self.btnModificarCliente.setObjectName("btnModificarCliente")
        self.horizontalLayout.addWidget(self.btnModificarCliente)
        self.btnEliminarCliente = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnEliminarCliente.setMinimumSize(QtCore.QSize(80, 25))
        self.btnEliminarCliente.setObjectName("btnEliminarCliente")
        self.horizontalLayout.addWidget(self.btnEliminarCliente)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.chkHistoricoCli = QtWidgets.QCheckBox(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkHistoricoCli.sizePolicy().hasHeightForWidth())
        self.chkHistoricoCli.setSizePolicy(sizePolicy)
        self.chkHistoricoCli.setObjectName("chkHistoricoCli")
        self.horizontalLayout.addWidget(self.chkHistoricoCli)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 1, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtBajaCliente = QtWidgets.QLineEdit(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtBajaCliente.sizePolicy().hasHeightForWidth())
        self.txtBajaCliente.setSizePolicy(sizePolicy)
        self.txtBajaCliente.setMinimumSize(QtCore.QSize(80, 0))
        self.txtBajaCliente.setMaximumSize(QtCore.QSize(80, 16777215))
        self.txtBajaCliente.setObjectName("txtBajaCliente")
        self.horizontalLayout_3.addWidget(self.txtBajaCliente)
        self.btnBajaCli = QtWidgets.QPushButton(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBajaCli.sizePolicy().hasHeightForWidth())
        self.btnBajaCli.setSizePolicy(sizePolicy)
        self.btnBajaCli.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnBajaCli.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\\\templates\\../img/calendar.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnBajaCli.setIcon(icon1)
        self.btnBajaCli.setIconSize(QtCore.QSize(21, 21))
        self.btnBajaCli.setObjectName("btnBajaCli")
        self.horizontalLayout_3.addWidget(self.btnBajaCli)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 8, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem9, 3, 9, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem10, 2, 0, 1, 1)
        self.cmbMunicipioCli = QtWidgets.QComboBox(parent=self.pesClientes)
        self.cmbMunicipioCli.setMinimumSize(QtCore.QSize(170, 0))
        self.cmbMunicipioCli.setObjectName("cmbMunicipioCli")
        self.gridLayout.addWidget(self.cmbMunicipioCli, 3, 8, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtAltaCliente = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtAltaCliente.setMinimumSize(QtCore.QSize(80, 0))
        self.txtAltaCliente.setMaximumSize(QtCore.QSize(80, 16777215))
        self.txtAltaCliente.setObjectName("txtAltaCliente")
        self.horizontalLayout_2.addWidget(self.txtAltaCliente)
        self.btnAltaCli = QtWidgets.QPushButton(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAltaCli.sizePolicy().hasHeightForWidth())
        self.btnAltaCli.setSizePolicy(sizePolicy)
        self.btnAltaCli.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnAltaCli.setText("")
        self.btnAltaCli.setIcon(icon1)
        self.btnAltaCli.setIconSize(QtCore.QSize(21, 21))
        self.btnAltaCli.setObjectName("btnAltaCli")
        self.horizontalLayout_2.addWidget(self.btnAltaCli)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 5, 1, 1)
        self.txtMovilCliente = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtMovilCliente.setMinimumSize(QtCore.QSize(200, 0))
        self.txtMovilCliente.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtMovilCliente.setText("")
        self.txtMovilCliente.setObjectName("txtMovilCliente")
        self.gridLayout.addWidget(self.txtMovilCliente, 2, 5, 1, 1)
        self.cmbProvCli = QtWidgets.QComboBox(parent=self.pesClientes)
        self.cmbProvCli.setMinimumSize(QtCore.QSize(150, 0))
        self.cmbProvCli.setObjectName("cmbProvCli")
        self.gridLayout.addWidget(self.cmbProvCli, 3, 5, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem12, 3, 6, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem13, 3, 3, 1, 1)
        self.lblDniCliente_2 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDniCliente_2.sizePolicy().hasHeightForWidth())
        self.lblDniCliente_2.setSizePolicy(sizePolicy)
        self.lblDniCliente_2.setObjectName("lblDniCliente_2")
        self.gridLayout.addWidget(self.lblDniCliente_2, 2, 1, 1, 1)
        self.txtNombreCliente = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtNombreCliente.setMinimumSize(QtCore.QSize(200, 0))
        self.txtNombreCliente.setMaximumSize(QtCore.QSize(250, 16777215))
        self.txtNombreCliente.setObjectName("txtNombreCliente")
        self.gridLayout.addWidget(self.txtNombreCliente, 1, 5, 1, 1)
        self.txtEmailCliente = QtWidgets.QLineEdit(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtEmailCliente.sizePolicy().hasHeightForWidth())
        self.txtEmailCliente.setSizePolicy(sizePolicy)
        self.txtEmailCliente.setMinimumSize(QtCore.QSize(200, 0))
        self.txtEmailCliente.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtEmailCliente.setObjectName("txtEmailCliente")
        self.gridLayout.addWidget(self.txtEmailCliente, 2, 2, 1, 1)
        self.txtApellidosCliente = QtWidgets.QLineEdit(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtApellidosCliente.sizePolicy().hasHeightForWidth())
        self.txtApellidosCliente.setSizePolicy(sizePolicy)
        self.txtApellidosCliente.setMinimumSize(QtCore.QSize(300, 0))
        self.txtApellidosCliente.setMaximumSize(QtCore.QSize(300, 16777215))
        self.txtApellidosCliente.setObjectName("txtApellidosCliente")
        self.gridLayout.addWidget(self.txtApellidosCliente, 1, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblDniCliente = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDniCliente.sizePolicy().hasHeightForWidth())
        self.lblDniCliente.setSizePolicy(sizePolicy)
        self.lblDniCliente.setObjectName("lblDniCliente")
        self.horizontalLayout_5.addWidget(self.lblDniCliente)
        self.label_2 = QtWidgets.QLabel(parent=self.pesClientes)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.txtDniCliente = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDniCliente.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txtDniCliente.setAutoFillBackground(False)
        self.txtDniCliente.setStyleSheet("background-color:rgb(255, 255, 222);")
        self.txtDniCliente.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDniCliente.setObjectName("txtDniCliente")
        self.gridLayout.addWidget(self.txtDniCliente, 0, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(parent=self.pesClientes)
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblDniCliente_4 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDniCliente_4.sizePolicy().hasHeightForWidth())
        self.lblDniCliente_4.setSizePolicy(sizePolicy)
        self.lblDniCliente_4.setObjectName("lblDniCliente_4")
        self.horizontalLayout_8.addWidget(self.lblDniCliente_4)
        self.label_6 = QtWidgets.QLabel(parent=self.pesClientes)
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)
        self.txtDirecionCliente = QtWidgets.QLineEdit(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDirecionCliente.sizePolicy().hasHeightForWidth())
        self.txtDirecionCliente.setSizePolicy(sizePolicy)
        self.txtDirecionCliente.setMinimumSize(QtCore.QSize(350, 0))
        self.txtDirecionCliente.setObjectName("txtDirecionCliente")
        self.gridLayout.addWidget(self.txtDirecionCliente, 3, 2, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lblAltaCliente = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblAltaCliente.setObjectName("lblAltaCliente")
        self.horizontalLayout_9.addWidget(self.lblAltaCliente)
        self.label_7 = QtWidgets.QLabel(parent=self.pesClientes)
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 4, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.label_9 = QtWidgets.QLabel(parent=self.pesClientes)
        self.label_9.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 4, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblDniCliente_3 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDniCliente_3.sizePolicy().hasHeightForWidth())
        self.lblDniCliente_3.setSizePolicy(sizePolicy)
        self.lblDniCliente_3.setObjectName("lblDniCliente_3")
        self.horizontalLayout_11.addWidget(self.lblDniCliente_3)
        self.label_10 = QtWidgets.QLabel(parent=self.pesClientes)
        self.label_10.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.gridLayout.addLayout(self.horizontalLayout_11, 2, 4, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblDniCliente_5 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDniCliente_5.sizePolicy().hasHeightForWidth())
        self.lblDniCliente_5.setSizePolicy(sizePolicy)
        self.lblDniCliente_5.setObjectName("lblDniCliente_5")
        self.horizontalLayout_12.addWidget(self.lblDniCliente_5)
        self.label_8 = QtWidgets.QLabel(parent=self.pesClientes)
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        self.gridLayout.addLayout(self.horizontalLayout_12, 3, 4, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lblMunicipio = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblMunicipio.setObjectName("lblMunicipio")
        self.horizontalLayout_13.addWidget(self.lblMunicipio)
        self.label_11 = QtWidgets.QLabel(parent=self.pesClientes)
        self.label_11.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.gridLayout.addLayout(self.horizontalLayout_13, 3, 7, 1, 1)
        self.lblBajaCliente = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblBajaCliente.setObjectName("lblBajaCliente")
        self.gridLayout.addWidget(self.lblBajaCliente, 0, 7, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.panPrincipal.addTab(self.pesClientes, "")
        self.tabEnConstruccion = QtWidgets.QWidget()
        self.tabEnConstruccion.setObjectName("tabEnConstruccion")
        self.label = QtWidgets.QLabel(parent=self.tabEnConstruccion)
        self.label.setGeometry(QtCore.QRect(176, 170, 111, 20))
        self.label.setObjectName("label")
        self.panPrincipal.addTab(self.tabEnConstruccion, "")
        self.gridLayout_3.addWidget(self.panPrincipal, 0, 4, 1, 1)
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=venPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1298, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHerramientas = QtWidgets.QMenu(parent=self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        self.menuAyuda = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        venPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=venPrincipal)
        self.toolBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.toolBar.setObjectName("toolBar")
        venPrincipal.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionSalir = QtGui.QAction(parent=venPrincipal)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\\\templates\\../img/log-out.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSalir.setIcon(icon2)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCrear_Backup = QtGui.QAction(parent=venPrincipal)
        self.actionCrear_Backup.setObjectName("actionCrear_Backup")
        self.actionRestaurar_Backup = QtGui.QAction(parent=venPrincipal)
        self.actionRestaurar_Backup.setObjectName("actionRestaurar_Backup")
        self.actionbarLimpiar = QtGui.QAction(parent=venPrincipal)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\\\templates\\../img/eraser.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionbarLimpiar.setIcon(icon3)
        self.actionbarLimpiar.setObjectName("actionbarLimpiar")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHerramientas.addAction(self.actionCrear_Backup)
        self.menuHerramientas.addAction(self.actionRestaurar_Backup)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionbarLimpiar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(venPrincipal)
        self.panPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)
        venPrincipal.setTabOrder(self.panPrincipal, self.txtAltaCliente)
        venPrincipal.setTabOrder(self.txtAltaCliente, self.btnAltaCli)
        venPrincipal.setTabOrder(self.btnAltaCli, self.txtNombreCliente)
        venPrincipal.setTabOrder(self.txtNombreCliente, self.txtEmailCliente)
        venPrincipal.setTabOrder(self.txtEmailCliente, self.txtMovilCliente)
        venPrincipal.setTabOrder(self.txtMovilCliente, self.cmbProvCli)
        venPrincipal.setTabOrder(self.cmbProvCli, self.cmbMunicipioCli)
        venPrincipal.setTabOrder(self.cmbMunicipioCli, self.btnGrabarCli)
        venPrincipal.setTabOrder(self.btnGrabarCli, self.btnModificarCliente)
        venPrincipal.setTabOrder(self.btnModificarCliente, self.btnEliminarCliente)
        venPrincipal.setTabOrder(self.btnEliminarCliente, self.tabClientes)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "InmoTeis"))
        self.tabClientes.setSortingEnabled(False)
        item = self.tabClientes.horizontalHeaderItem(0)
        item.setText(_translate("venPrincipal", "DNI/NIF"))
        item = self.tabClientes.horizontalHeaderItem(1)
        item.setText(_translate("venPrincipal", "Apellidos"))
        item = self.tabClientes.horizontalHeaderItem(2)
        item.setText(_translate("venPrincipal", "Nombre"))
        item = self.tabClientes.horizontalHeaderItem(3)
        item.setText(_translate("venPrincipal", "Movil"))
        item = self.tabClientes.horizontalHeaderItem(4)
        item.setText(_translate("venPrincipal", "Provincia"))
        item = self.tabClientes.horizontalHeaderItem(5)
        item.setText(_translate("venPrincipal", "Municipio"))
        item = self.tabClientes.horizontalHeaderItem(6)
        item.setText(_translate("venPrincipal", "Fecha de baja"))
        self.btnGrabarCli.setText(_translate("venPrincipal", "Grabar"))
        self.btnModificarCliente.setText(_translate("venPrincipal", "Modificar"))
        self.btnEliminarCliente.setText(_translate("venPrincipal", "Eliminar"))
        self.chkHistoricoCli.setText(_translate("venPrincipal", "Historico"))
        self.lblDniCliente_2.setText(_translate("venPrincipal", "Email"))
        self.lblDniCliente.setText(_translate("venPrincipal", "DNI/CIF"))
        self.label_2.setToolTip(_translate("venPrincipal", "Campo obligatorio"))
        self.label_2.setText(_translate("venPrincipal", "*"))
        self.label_3.setText(_translate("venPrincipal", "Apellidos"))
        self.label_5.setStatusTip(_translate("venPrincipal", "Campo obligatorio"))
        self.label_5.setText(_translate("venPrincipal", "*"))
        self.lblDniCliente_4.setText(_translate("venPrincipal", "Dirección"))
        self.label_6.setToolTip(_translate("venPrincipal", "Campo obligatorio"))
        self.label_6.setText(_translate("venPrincipal", "*"))
        self.lblAltaCliente.setText(_translate("venPrincipal", "Fecha Alta"))
        self.label_7.setToolTip(_translate("venPrincipal", "Campo obligatorio"))
        self.label_7.setText(_translate("venPrincipal", "*"))
        self.label_4.setText(_translate("venPrincipal", "Nombre"))
        self.label_9.setToolTip(_translate("venPrincipal", "Campo obligatorio"))
        self.label_9.setText(_translate("venPrincipal", "*"))
        self.lblDniCliente_3.setText(_translate("venPrincipal", "Movil"))
        self.label_10.setToolTip(_translate("venPrincipal", "Campo obligatorio"))
        self.label_10.setText(_translate("venPrincipal", "*"))
        self.lblDniCliente_5.setText(_translate("venPrincipal", "Provincia"))
        self.label_8.setToolTip(_translate("venPrincipal", "Campo obligatorio"))
        self.label_8.setText(_translate("venPrincipal", "*"))
        self.lblMunicipio.setText(_translate("venPrincipal", "Municipio"))
        self.label_11.setToolTip(_translate("venPrincipal", "Campo obligatorio"))
        self.label_11.setText(_translate("venPrincipal", "*"))
        self.lblBajaCliente.setText(_translate("venPrincipal", "Fecha Baja"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.pesClientes), _translate("venPrincipal", "Clientes"))
        self.label.setText(_translate("venPrincipal", "En construccion"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.tabEnConstruccion), _translate("venPrincipal", "Tab 2"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.menuHerramientas.setTitle(_translate("venPrincipal", "Herramientas"))
        self.menuAyuda.setTitle(_translate("venPrincipal", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("venPrincipal", "toolBar"))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
        self.actionSalir.setShortcut(_translate("venPrincipal", "Ctrl+Alt+F4"))
        self.actionCrear_Backup.setText(_translate("venPrincipal", "Crear Backup"))
        self.actionRestaurar_Backup.setText(_translate("venPrincipal", "Restaurar Backup"))
        self.actionbarLimpiar.setText(_translate("venPrincipal", "barLimpiar"))
        self.actionbarLimpiar.setToolTip(_translate("venPrincipal", "Limpiar"))
        self.actionbarLimpiar.setShortcut(_translate("venPrincipal", "Alt+R"))
