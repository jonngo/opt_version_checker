# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jfrog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jfrog_widget(object):
    def setupUi(self, jfrog_widget):
        jfrog_widget.setObjectName("jfrog_widget")
        jfrog_widget.resize(887, 613)
        self.verticalLayout = QtWidgets.QVBoxLayout(jfrog_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(jfrog_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(jfrog_widget)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.jfrog_build_ver_line_edit = QtWidgets.QLineEdit(self.frame)
        self.jfrog_build_ver_line_edit.setObjectName("jfrog_build_ver_line_edit")
        self.gridLayout.addWidget(self.jfrog_build_ver_line_edit, 0, 1, 1, 1)
        self.jfrog_all_tableview = QtWidgets.QTableView(self.frame)
        self.jfrog_all_tableview.setObjectName("jfrog_all_tableview")
        self.gridLayout.addWidget(self.jfrog_all_tableview, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.jfrog_load_push_button = QtWidgets.QPushButton(jfrog_widget)
        self.jfrog_load_push_button.setObjectName("jfrog_load_push_button")
        self.horizontalLayout_3.addWidget(self.jfrog_load_push_button)
        self.jfrog_close_push_button = QtWidgets.QPushButton(jfrog_widget)
        self.jfrog_close_push_button.setObjectName("jfrog_close_push_button")
        self.horizontalLayout_3.addWidget(self.jfrog_close_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(jfrog_widget)
        self.jfrog_close_push_button.clicked.connect(jfrog_widget.close)
        QtCore.QMetaObject.connectSlotsByName(jfrog_widget)

    def retranslateUi(self, jfrog_widget):
        _translate = QtCore.QCoreApplication.translate
        jfrog_widget.setWindowTitle(_translate("jfrog_widget", "JFrog Artifactory"))
        self.label.setText(_translate("jfrog_widget", "JFrog Artifactory"))
        self.label_2.setText(_translate("jfrog_widget", "Build version"))
        self.jfrog_load_push_button.setText(_translate("jfrog_widget", "Load"))
        self.jfrog_close_push_button.setText(_translate("jfrog_widget", "Close"))
