# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_on_screen_data.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_save_widget(object):
    def setupUi(self, save_widget):
        save_widget.setObjectName("save_widget")
        save_widget.resize(763, 79)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(save_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(save_widget)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.save_filename_line_edit = QtWidgets.QLineEdit(self.frame)
        self.save_filename_line_edit.setObjectName("save_filename_line_edit")
        self.gridLayout_3.addWidget(self.save_filename_line_edit, 0, 1, 1, 1)
        self.save_filename_label = QtWidgets.QLabel(self.frame)
        self.save_filename_label.setObjectName("save_filename_label")
        self.gridLayout_3.addWidget(self.save_filename_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.save_save_button = QtWidgets.QPushButton(save_widget)
        self.save_save_button.setObjectName("save_save_button")
        self.horizontalLayout_5.addWidget(self.save_save_button)
        self.save_close_button = QtWidgets.QPushButton(save_widget)
        self.save_close_button.setObjectName("save_close_button")
        self.horizontalLayout_5.addWidget(self.save_close_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(save_widget)
        self.save_close_button.clicked.connect(save_widget.hide)
        QtCore.QMetaObject.connectSlotsByName(save_widget)

    def retranslateUi(self, save_widget):
        _translate = QtCore.QCoreApplication.translate
        save_widget.setWindowTitle(_translate("save_widget", "Save"))
        self.save_filename_label.setText(_translate("save_widget", "File Name"))
        self.save_save_button.setText(_translate("save_widget", "Save"))
        self.save_close_button.setText(_translate("save_widget", "Close"))
