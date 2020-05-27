# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tms_param.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tms_widget(object):
    def setupUi(self, tms_widget):
        tms_widget.setObjectName("tms_widget")
        tms_widget.resize(599, 140)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tms_widget.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(tms_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(tms_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(tms_widget)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.tms_param_search_push_button = QtWidgets.QPushButton(self.frame)
        self.tms_param_search_push_button.setObjectName("tms_param_search_push_button")
        self.gridLayout.addWidget(self.tms_param_search_push_button, 0, 2, 1, 1)
        self.tms_param_label = QtWidgets.QLabel(self.frame)
        self.tms_param_label.setObjectName("tms_param_label")
        self.gridLayout.addWidget(self.tms_param_label, 0, 0, 1, 1)
        self.tmslite_param_line_edit = QtWidgets.QLineEdit(self.frame)
        self.tmslite_param_line_edit.setEnabled(True)
        self.tmslite_param_line_edit.setObjectName("tmslite_param_line_edit")
        self.gridLayout.addWidget(self.tmslite_param_line_edit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.tms_param_load_push_button = QtWidgets.QPushButton(tms_widget)
        self.tms_param_load_push_button.setObjectName("tms_param_load_push_button")
        self.horizontalLayout_3.addWidget(self.tms_param_load_push_button)
        self.tms_param_close_push_button = QtWidgets.QPushButton(tms_widget)
        self.tms_param_close_push_button.setObjectName("tms_param_close_push_button")
        self.horizontalLayout_3.addWidget(self.tms_param_close_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(tms_widget)
        self.tms_param_close_push_button.clicked.connect(tms_widget.hide)
        QtCore.QMetaObject.connectSlotsByName(tms_widget)

    def retranslateUi(self, tms_widget):
        _translate = QtCore.QCoreApplication.translate
        tms_widget.setWindowTitle(_translate("tms_widget", "TMSLite Parameters"))
        self.label.setText(_translate("tms_widget", "TMSLite Parameters"))
        self.tms_param_search_push_button.setText(_translate("tms_widget", "Search"))
        self.tms_param_label.setText(_translate("tms_widget", "TMSLite Parameter"))
        self.tms_param_load_push_button.setText(_translate("tms_widget", "Load"))
        self.tms_param_close_push_button.setText(_translate("tms_widget", "Close"))
