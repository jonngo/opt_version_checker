# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emv.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_emv_widget(object):
    def setupUi(self, emv_widget):
        emv_widget.setObjectName("emv_widget")
        emv_widget.resize(598, 243)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        emv_widget.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(emv_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.emv_label = QtWidgets.QLabel(emv_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.emv_label.setFont(font)
        self.emv_label.setObjectName("emv_label")
        self.verticalLayout.addWidget(self.emv_label)
        self.frame = QtWidgets.QFrame(emv_widget)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.chrome_driver_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.chrome_driver_lineEdit.setObjectName("chrome_driver_lineEdit")
        self.gridLayout.addWidget(self.chrome_driver_lineEdit, 3, 1, 1, 1)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)
        self.emv_ver_url_lineedit = QtWidgets.QLineEdit(self.frame)
        self.emv_ver_url_lineedit.setObjectName("emv_ver_url_lineedit")
        self.gridLayout.addWidget(self.emv_ver_url_lineedit, 2, 1, 1, 1)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameLineEdit.setEnabled(True)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.gridLayout.addWidget(self.usernameLineEdit, 0, 1, 1, 1)
        self.chromeDriverPushButton = QtWidgets.QPushButton(self.frame)
        self.chromeDriverPushButton.setObjectName("chromeDriverPushButton")
        self.gridLayout.addWidget(self.chromeDriverPushButton, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.emv_device_comboBox = QtWidgets.QComboBox(self.frame)
        self.emv_device_comboBox.setObjectName("emv_device_comboBox")
        self.gridLayout.addWidget(self.emv_device_comboBox, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.extractEMVPushButton = QtWidgets.QPushButton(emv_widget)
        self.extractEMVPushButton.setObjectName("extractEMVPushButton")
        self.horizontalLayout_3.addWidget(self.extractEMVPushButton)
        self.closeEMVPushButton = QtWidgets.QPushButton(emv_widget)
        self.closeEMVPushButton.setObjectName("closeEMVPushButton")
        self.horizontalLayout_3.addWidget(self.closeEMVPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(emv_widget)
        self.closeEMVPushButton.clicked.connect(emv_widget.close)
        self.usernameLineEdit.returnPressed.connect(self.passwordLineEdit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(emv_widget)

    def retranslateUi(self, emv_widget):
        _translate = QtCore.QCoreApplication.translate
        emv_widget.setWindowTitle(_translate("emv_widget", "EMV Kernel Version"))
        self.emv_label.setText(_translate("emv_widget", "EMV Kernel Version"))
        self.label_3.setText(_translate("emv_widget", "Password"))
        self.label_2.setText(_translate("emv_widget", "Username"))
        self.label_5.setText(_translate("emv_widget", "Chrome driver"))
        self.label_4.setText(_translate("emv_widget", "EMV Version URL"))
        self.chromeDriverPushButton.setText(_translate("emv_widget", "Search"))
        self.label.setText(_translate("emv_widget", "Device"))
        self.extractEMVPushButton.setText(_translate("emv_widget", "Extract"))
        self.closeEMVPushButton.setText(_translate("emv_widget", "Close"))
