# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jbz_pkg.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pkg_widget(object):
    def setupUi(self, pkg_widget):
        pkg_widget.setObjectName("pkg_widget")
        pkg_widget.resize(602, 359)
        self.verticalLayout = QtWidgets.QVBoxLayout(pkg_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(pkg_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(pkg_widget)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.jbzPathPushButton = QtWidgets.QPushButton(self.frame)
        self.jbzPathPushButton.setObjectName("jbzPathPushButton")
        self.gridLayout.addWidget(self.jbzPathPushButton, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.sevenZpushButton = QtWidgets.QPushButton(self.frame)
        self.sevenZpushButton.setObjectName("sevenZpushButton")
        self.gridLayout.addWidget(self.sevenZpushButton, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.jbz_manifest_line_edit = QtWidgets.QLineEdit(self.frame)
        self.jbz_manifest_line_edit.setObjectName("jbz_manifest_line_edit")
        self.gridLayout.addWidget(self.jbz_manifest_line_edit, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.sevenZlineEdit = QtWidgets.QLineEdit(self.frame)
        self.sevenZlineEdit.setObjectName("sevenZlineEdit")
        self.gridLayout.addWidget(self.sevenZlineEdit, 5, 1, 1, 1)
        self.extractionPathLineEdit = QtWidgets.QLineEdit(self.frame)
        self.extractionPathLineEdit.setObjectName("extractionPathLineEdit")
        self.gridLayout.addWidget(self.extractionPathLineEdit, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.jbz_regex_match_ver_line_edit = QtWidgets.QLineEdit(self.frame)
        self.jbz_regex_match_ver_line_edit.setObjectName("jbz_regex_match_ver_line_edit")
        self.gridLayout.addWidget(self.jbz_regex_match_ver_line_edit, 7, 1, 1, 1)
        self.extractionPushButton = QtWidgets.QPushButton(self.frame)
        self.extractionPushButton.setObjectName("extractionPushButton")
        self.gridLayout.addWidget(self.extractionPushButton, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.jbzPathLineEdit = QtWidgets.QLineEdit(self.frame)
        self.jbzPathLineEdit.setEnabled(True)
        self.jbzPathLineEdit.setObjectName("jbzPathLineEdit")
        self.gridLayout.addWidget(self.jbzPathLineEdit, 0, 1, 1, 1)
        self.conf_other_pkg_1_push_button = QtWidgets.QPushButton(self.frame)
        self.conf_other_pkg_1_push_button.setObjectName("conf_other_pkg_1_push_button")
        self.gridLayout.addWidget(self.conf_other_pkg_1_push_button, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.conf_other_pkg_2_line_edit = QtWidgets.QLineEdit(self.frame)
        self.conf_other_pkg_2_line_edit.setObjectName("conf_other_pkg_2_line_edit")
        self.gridLayout.addWidget(self.conf_other_pkg_2_line_edit, 2, 1, 1, 1)
        self.conf_other_pkg_2_push_button = QtWidgets.QPushButton(self.frame)
        self.conf_other_pkg_2_push_button.setObjectName("conf_other_pkg_2_push_button")
        self.gridLayout.addWidget(self.conf_other_pkg_2_push_button, 2, 2, 1, 1)
        self.conf_other_pkg_3_line_edit = QtWidgets.QLineEdit(self.frame)
        self.conf_other_pkg_3_line_edit.setObjectName("conf_other_pkg_3_line_edit")
        self.gridLayout.addWidget(self.conf_other_pkg_3_line_edit, 3, 1, 1, 1)
        self.conf_other_pkg_3_push_button = QtWidgets.QPushButton(self.frame)
        self.conf_other_pkg_3_push_button.setObjectName("conf_other_pkg_3_push_button")
        self.gridLayout.addWidget(self.conf_other_pkg_3_push_button, 3, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.conf_other_pkg_1_line_edit = QtWidgets.QLineEdit(self.frame)
        self.conf_other_pkg_1_line_edit.setObjectName("conf_other_pkg_1_line_edit")
        self.gridLayout.addWidget(self.conf_other_pkg_1_line_edit, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.show_path_checkbox = QtWidgets.QCheckBox(self.frame)
        self.show_path_checkbox.setObjectName("show_path_checkbox")
        self.gridLayout.addWidget(self.show_path_checkbox, 9, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.extractPushButton = QtWidgets.QPushButton(pkg_widget)
        self.extractPushButton.setObjectName("extractPushButton")
        self.horizontalLayout_3.addWidget(self.extractPushButton)
        self.closePushButton = QtWidgets.QPushButton(pkg_widget)
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout_3.addWidget(self.closePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(pkg_widget)
        self.closePushButton.clicked.connect(pkg_widget.hide)
        QtCore.QMetaObject.connectSlotsByName(pkg_widget)

    def retranslateUi(self, pkg_widget):
        _translate = QtCore.QCoreApplication.translate
        pkg_widget.setWindowTitle(_translate("pkg_widget", "Job Bundle Package Version"))
        self.label.setText(_translate("pkg_widget", "Job Bundle Package Version"))
        self.jbzPathPushButton.setText(_translate("pkg_widget", "Search"))
        self.label_2.setText(_translate("pkg_widget", "Job Bundle File Path"))
        self.label_4.setText(_translate("pkg_widget", "7z Path"))
        self.sevenZpushButton.setText(_translate("pkg_widget", "Search"))
        self.label_5.setText(_translate("pkg_widget", "Manifest File"))
        self.label_6.setText(_translate("pkg_widget", "Version Regex"))
        self.extractionPushButton.setText(_translate("pkg_widget", "Search"))
        self.label_3.setText(_translate("pkg_widget", "Extraction File Path"))
        self.conf_other_pkg_1_push_button.setText(_translate("pkg_widget", "Search"))
        self.label_8.setText(_translate("pkg_widget", "Conf or Other Pkg 2"))
        self.label_7.setText(_translate("pkg_widget", "Conf or Other Pkg 1"))
        self.conf_other_pkg_2_push_button.setText(_translate("pkg_widget", "Search"))
        self.conf_other_pkg_3_push_button.setText(_translate("pkg_widget", "Search"))
        self.label_9.setText(_translate("pkg_widget", "Conf or Other Pkg 3"))
        self.label_10.setText(_translate("pkg_widget", "Show Path"))
        self.show_path_checkbox.setText(_translate("pkg_widget", "Enable"))
        self.extractPushButton.setText(_translate("pkg_widget", "Extract"))
        self.closePushButton.setText(_translate("pkg_widget", "Close"))
