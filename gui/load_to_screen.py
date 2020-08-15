# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load_to_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_load_widget(object):
    def setupUi(self, load_widget):
        load_widget.setObjectName("load_widget")
        load_widget.resize(768, 100)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        load_widget.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(load_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(load_widget)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.load_browse_filename_push_button = QtWidgets.QPushButton(self.frame)
        self.load_browse_filename_push_button.setObjectName("load_browse_filename_push_button")
        self.gridLayout.addWidget(self.load_browse_filename_push_button, 0, 2, 1, 1)
        self.load_filename_label = QtWidgets.QLabel(self.frame)
        self.load_filename_label.setObjectName("load_filename_label")
        self.gridLayout.addWidget(self.load_filename_label, 0, 0, 1, 1)
        self.load_filename_line_edit = QtWidgets.QLineEdit(self.frame)
        self.load_filename_line_edit.setEnabled(True)
        self.load_filename_line_edit.setObjectName("load_filename_line_edit")
        self.gridLayout.addWidget(self.load_filename_line_edit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.load_load_push_button = QtWidgets.QPushButton(load_widget)
        self.load_load_push_button.setObjectName("load_load_push_button")
        self.horizontalLayout_3.addWidget(self.load_load_push_button)
        self.load_close_push_button = QtWidgets.QPushButton(load_widget)
        self.load_close_push_button.setObjectName("load_close_push_button")
        self.horizontalLayout_3.addWidget(self.load_close_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(load_widget)
        self.load_close_push_button.clicked.connect(load_widget.hide)
        QtCore.QMetaObject.connectSlotsByName(load_widget)

    def retranslateUi(self, load_widget):
        _translate = QtCore.QCoreApplication.translate
        load_widget.setWindowTitle(_translate("load_widget", "Load"))
        self.load_browse_filename_push_button.setText(_translate("load_widget", "Browse"))
        self.load_filename_label.setText(_translate("load_widget", "File Name"))
        self.load_load_push_button.setText(_translate("load_widget", "Load"))
        self.load_close_push_button.setText(_translate("load_widget", "Close"))
