# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compare.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_compare_widget(object):
    def setupUi(self, compare_widget):
        compare_widget.setObjectName("compare_widget")
        compare_widget.resize(1005, 579)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        compare_widget.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(compare_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.compare_filter_name_label = QtWidgets.QLabel(compare_widget)
        self.compare_filter_name_label.setObjectName("compare_filter_name_label")
        self.gridLayout.addWidget(self.compare_filter_name_label, 0, 0, 1, 1)
        self.compare_line_edit = QtWidgets.QLineEdit(compare_widget)
        self.compare_line_edit.setObjectName("compare_line_edit")
        self.gridLayout.addWidget(self.compare_line_edit, 0, 1, 1, 1)
        self.compare_browse_push_button = QtWidgets.QPushButton(compare_widget)
        self.compare_browse_push_button.setObjectName("compare_browse_push_button")
        self.gridLayout.addWidget(self.compare_browse_push_button, 0, 2, 1, 1)
        self.frame = QtWidgets.QFrame(compare_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.compare_load_push_button = QtWidgets.QPushButton(self.frame)
        self.compare_load_push_button.setObjectName("compare_load_push_button")
        self.horizontalLayout.addWidget(self.compare_load_push_button)
        self.compare_close_push_button = QtWidgets.QPushButton(self.frame)
        self.compare_close_push_button.setObjectName("compare_close_push_button")
        self.horizontalLayout.addWidget(self.compare_close_push_button)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 3)
        self.compare_table = QtWidgets.QTableView(compare_widget)
        self.compare_table.setObjectName("compare_table")
        self.gridLayout.addWidget(self.compare_table, 1, 0, 1, 3)

        self.retranslateUi(compare_widget)
        self.compare_close_push_button.clicked.connect(compare_widget.hide)
        QtCore.QMetaObject.connectSlotsByName(compare_widget)

    def retranslateUi(self, compare_widget):
        _translate = QtCore.QCoreApplication.translate
        compare_widget.setWindowTitle(_translate("compare_widget", "Compare Version"))
        self.compare_filter_name_label.setText(_translate("compare_widget", "Filter Name"))
        self.compare_browse_push_button.setText(_translate("compare_widget", "Browse"))
        self.compare_load_push_button.setText(_translate("compare_widget", "Load"))
        self.compare_close_push_button.setText(_translate("compare_widget", "Close"))
