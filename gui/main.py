# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1386, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.jfrog_label = QtWidgets.QLabel(self.centralwidget)
        self.jfrog_label.setObjectName("jfrog_label")
        self.verticalLayout_8.addWidget(self.jfrog_label)
        self.jfrog_table = QtWidgets.QTableView(self.centralwidget)
        self.jfrog_table.setObjectName("jfrog_table")
        self.verticalLayout_8.addWidget(self.jfrog_table)
        self.jfrog_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.jfrog_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.jfrog_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.jfrog_buttom_button_frame.setObjectName("jfrog_buttom_button_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.jfrog_buttom_button_frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.jfrog_hide_pushbutton = QtWidgets.QPushButton(self.jfrog_buttom_button_frame)
        self.jfrog_hide_pushbutton.setObjectName("jfrog_hide_pushbutton")
        self.horizontalLayout_7.addWidget(self.jfrog_hide_pushbutton)
        self.jfrog_export_pushbutton = QtWidgets.QPushButton(self.jfrog_buttom_button_frame)
        self.jfrog_export_pushbutton.setObjectName("jfrog_export_pushbutton")
        self.horizontalLayout_7.addWidget(self.jfrog_export_pushbutton)
        self.verticalLayout_8.addWidget(self.jfrog_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.job_bundle_pkg_ver_label = QtWidgets.QLabel(self.centralwidget)
        self.job_bundle_pkg_ver_label.setObjectName("job_bundle_pkg_ver_label")
        self.verticalLayout_7.addWidget(self.job_bundle_pkg_ver_label)
        self.jbz_pkg_ver_table = QtWidgets.QTableView(self.centralwidget)
        self.jbz_pkg_ver_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.jbz_pkg_ver_table.setObjectName("jbz_pkg_ver_table")
        self.verticalLayout_7.addWidget(self.jbz_pkg_ver_table)
        self.pkg_listview = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pkg_listview.sizePolicy().hasHeightForWidth())
        self.pkg_listview.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.pkg_listview.setFont(font)
        self.pkg_listview.setObjectName("pkg_listview")
        self.verticalLayout_7.addWidget(self.pkg_listview)
        self.jbz_pkg_ver_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.jbz_pkg_ver_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.jbz_pkg_ver_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.jbz_pkg_ver_buttom_button_frame.setObjectName("jbz_pkg_ver_buttom_button_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.jbz_pkg_ver_buttom_button_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.pkg_header_pushbutton = QtWidgets.QPushButton(self.jbz_pkg_ver_buttom_button_frame)
        self.pkg_header_pushbutton.setObjectName("pkg_header_pushbutton")
        self.horizontalLayout_8.addWidget(self.pkg_header_pushbutton)
        self.jbz_pkg_version_hide_pushbutton = QtWidgets.QPushButton(self.jbz_pkg_ver_buttom_button_frame)
        self.jbz_pkg_version_hide_pushbutton.setObjectName("jbz_pkg_version_hide_pushbutton")
        self.horizontalLayout_8.addWidget(self.jbz_pkg_version_hide_pushbutton)
        self.jbz_pkg_version_export_pushbutton = QtWidgets.QPushButton(self.jbz_pkg_ver_buttom_button_frame)
        self.jbz_pkg_version_export_pushbutton.setObjectName("jbz_pkg_version_export_pushbutton")
        self.horizontalLayout_8.addWidget(self.jbz_pkg_version_export_pushbutton)
        self.verticalLayout_7.addWidget(self.jbz_pkg_ver_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.first_conf_other_pkg_ver_label = QtWidgets.QLabel(self.centralwidget)
        self.first_conf_other_pkg_ver_label.setObjectName("first_conf_other_pkg_ver_label")
        self.verticalLayout_9.addWidget(self.first_conf_other_pkg_ver_label)
        self.first_conf_other_pkg_ver_table = QtWidgets.QTableView(self.centralwidget)
        self.first_conf_other_pkg_ver_table.setObjectName("first_conf_other_pkg_ver_table")
        self.verticalLayout_9.addWidget(self.first_conf_other_pkg_ver_table)
        self.first_conf_other_pkg_listview = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_conf_other_pkg_listview.sizePolicy().hasHeightForWidth())
        self.first_conf_other_pkg_listview.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.first_conf_other_pkg_listview.setFont(font)
        self.first_conf_other_pkg_listview.setObjectName("first_conf_other_pkg_listview")
        self.verticalLayout_9.addWidget(self.first_conf_other_pkg_listview)
        self.first_conf_other_pkg_ver_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.first_conf_other_pkg_ver_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.first_conf_other_pkg_ver_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_conf_other_pkg_ver_buttom_button_frame.setObjectName("first_conf_other_pkg_ver_buttom_button_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.first_conf_other_pkg_ver_buttom_button_frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.first_conf_other_pkg_header_pushbutton = QtWidgets.QPushButton(self.first_conf_other_pkg_ver_buttom_button_frame)
        self.first_conf_other_pkg_header_pushbutton.setObjectName("first_conf_other_pkg_header_pushbutton")
        self.horizontalLayout_9.addWidget(self.first_conf_other_pkg_header_pushbutton)
        self.first_conf_other_pkg_version_hide_pushbutton = QtWidgets.QPushButton(self.first_conf_other_pkg_ver_buttom_button_frame)
        self.first_conf_other_pkg_version_hide_pushbutton.setObjectName("first_conf_other_pkg_version_hide_pushbutton")
        self.horizontalLayout_9.addWidget(self.first_conf_other_pkg_version_hide_pushbutton)
        self.first_conf_other_pkg_version_export_pushbutton = QtWidgets.QPushButton(self.first_conf_other_pkg_ver_buttom_button_frame)
        self.first_conf_other_pkg_version_export_pushbutton.setObjectName("first_conf_other_pkg_version_export_pushbutton")
        self.horizontalLayout_9.addWidget(self.first_conf_other_pkg_version_export_pushbutton)
        self.verticalLayout_9.addWidget(self.first_conf_other_pkg_ver_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.second_conf_other_pkg_ver_label = QtWidgets.QLabel(self.centralwidget)
        self.second_conf_other_pkg_ver_label.setObjectName("second_conf_other_pkg_ver_label")
        self.verticalLayout_10.addWidget(self.second_conf_other_pkg_ver_label)
        self.second_conf_other_pkg_ver_table = QtWidgets.QTableView(self.centralwidget)
        self.second_conf_other_pkg_ver_table.setObjectName("second_conf_other_pkg_ver_table")
        self.verticalLayout_10.addWidget(self.second_conf_other_pkg_ver_table)
        self.second_conf_other_pkg_listview = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.second_conf_other_pkg_listview.sizePolicy().hasHeightForWidth())
        self.second_conf_other_pkg_listview.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.second_conf_other_pkg_listview.setFont(font)
        self.second_conf_other_pkg_listview.setObjectName("second_conf_other_pkg_listview")
        self.verticalLayout_10.addWidget(self.second_conf_other_pkg_listview)
        self.second_conf_other_pkg_ver_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.second_conf_other_pkg_ver_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.second_conf_other_pkg_ver_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_conf_other_pkg_ver_buttom_button_frame.setObjectName("second_conf_other_pkg_ver_buttom_button_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.second_conf_other_pkg_ver_buttom_button_frame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.second_conf_other_pkg_header_pushbutton = QtWidgets.QPushButton(self.second_conf_other_pkg_ver_buttom_button_frame)
        self.second_conf_other_pkg_header_pushbutton.setObjectName("second_conf_other_pkg_header_pushbutton")
        self.horizontalLayout_10.addWidget(self.second_conf_other_pkg_header_pushbutton)
        self.second_conf_other_pkg_version_hide_pushbutton = QtWidgets.QPushButton(self.second_conf_other_pkg_ver_buttom_button_frame)
        self.second_conf_other_pkg_version_hide_pushbutton.setObjectName("second_conf_other_pkg_version_hide_pushbutton")
        self.horizontalLayout_10.addWidget(self.second_conf_other_pkg_version_hide_pushbutton)
        self.second_conf_other_pkg_version_export_pushbutton = QtWidgets.QPushButton(self.second_conf_other_pkg_ver_buttom_button_frame)
        self.second_conf_other_pkg_version_export_pushbutton.setObjectName("second_conf_other_pkg_version_export_pushbutton")
        self.horizontalLayout_10.addWidget(self.second_conf_other_pkg_version_export_pushbutton)
        self.verticalLayout_10.addWidget(self.second_conf_other_pkg_ver_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.third_conf_other_pkg_ver_label = QtWidgets.QLabel(self.centralwidget)
        self.third_conf_other_pkg_ver_label.setObjectName("third_conf_other_pkg_ver_label")
        self.verticalLayout_11.addWidget(self.third_conf_other_pkg_ver_label)
        self.third_conf_other_pkg_ver_table = QtWidgets.QTableView(self.centralwidget)
        self.third_conf_other_pkg_ver_table.setObjectName("third_conf_other_pkg_ver_table")
        self.verticalLayout_11.addWidget(self.third_conf_other_pkg_ver_table)
        self.third_conf_other_pkg_listview = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.third_conf_other_pkg_listview.sizePolicy().hasHeightForWidth())
        self.third_conf_other_pkg_listview.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.third_conf_other_pkg_listview.setFont(font)
        self.third_conf_other_pkg_listview.setObjectName("third_conf_other_pkg_listview")
        self.verticalLayout_11.addWidget(self.third_conf_other_pkg_listview)
        self.third_conf_other_pkg_ver_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.third_conf_other_pkg_ver_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.third_conf_other_pkg_ver_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.third_conf_other_pkg_ver_buttom_button_frame.setObjectName("third_conf_other_pkg_ver_buttom_button_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.third_conf_other_pkg_ver_buttom_button_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.third_conf_other_pkg_header_pushbutton = QtWidgets.QPushButton(self.third_conf_other_pkg_ver_buttom_button_frame)
        self.third_conf_other_pkg_header_pushbutton.setObjectName("third_conf_other_pkg_header_pushbutton")
        self.horizontalLayout_2.addWidget(self.third_conf_other_pkg_header_pushbutton)
        self.third_conf_other_pkg_version_hide_pushbutton = QtWidgets.QPushButton(self.third_conf_other_pkg_ver_buttom_button_frame)
        self.third_conf_other_pkg_version_hide_pushbutton.setObjectName("third_conf_other_pkg_version_hide_pushbutton")
        self.horizontalLayout_2.addWidget(self.third_conf_other_pkg_version_hide_pushbutton)
        self.third_conf_other_pkg_version_export_pushbutton = QtWidgets.QPushButton(self.third_conf_other_pkg_ver_buttom_button_frame)
        self.third_conf_other_pkg_version_export_pushbutton.setObjectName("third_conf_other_pkg_version_export_pushbutton")
        self.horizontalLayout_2.addWidget(self.third_conf_other_pkg_version_export_pushbutton)
        self.verticalLayout_11.addWidget(self.third_conf_other_pkg_ver_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.manifest_file_label = QtWidgets.QLabel(self.centralwidget)
        self.manifest_file_label.setObjectName("manifest_file_label")
        self.verticalLayout_5.addWidget(self.manifest_file_label)
        self.manifest_table = QtWidgets.QTableView(self.centralwidget)
        self.manifest_table.setObjectName("manifest_table")
        self.verticalLayout_5.addWidget(self.manifest_table)
        self.manifest_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.manifest_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.manifest_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.manifest_buttom_button_frame.setObjectName("manifest_buttom_button_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.manifest_buttom_button_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.manifest_hide_pushbutton = QtWidgets.QPushButton(self.manifest_buttom_button_frame)
        self.manifest_hide_pushbutton.setObjectName("manifest_hide_pushbutton")
        self.horizontalLayout_5.addWidget(self.manifest_hide_pushbutton)
        self.manifest_export_pushbutton = QtWidgets.QPushButton(self.manifest_buttom_button_frame)
        self.manifest_export_pushbutton.setObjectName("manifest_export_pushbutton")
        self.horizontalLayout_5.addWidget(self.manifest_export_pushbutton)
        self.verticalLayout_5.addWidget(self.manifest_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tms_param_label = QtWidgets.QLabel(self.centralwidget)
        self.tms_param_label.setObjectName("tms_param_label")
        self.verticalLayout_6.addWidget(self.tms_param_label)
        self.tms_param_table = QtWidgets.QTableView(self.centralwidget)
        self.tms_param_table.setObjectName("tms_param_table")
        self.verticalLayout_6.addWidget(self.tms_param_table)
        self.tms_param_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.tms_param_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.tms_param_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tms_param_buttom_button_frame.setObjectName("tms_param_buttom_button_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tms_param_buttom_button_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.tms_param_hide_pushbutton = QtWidgets.QPushButton(self.tms_param_buttom_button_frame)
        self.tms_param_hide_pushbutton.setObjectName("tms_param_hide_pushbutton")
        self.horizontalLayout_3.addWidget(self.tms_param_hide_pushbutton)
        self.tms_param_export_pushbutton = QtWidgets.QPushButton(self.tms_param_buttom_button_frame)
        self.tms_param_export_pushbutton.setObjectName("tms_param_export_pushbutton")
        self.horizontalLayout_3.addWidget(self.tms_param_export_pushbutton)
        self.verticalLayout_6.addWidget(self.tms_param_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.emv_kernel_version_label = QtWidgets.QLabel(self.centralwidget)
        self.emv_kernel_version_label.setObjectName("emv_kernel_version_label")
        self.verticalLayout_2.addWidget(self.emv_kernel_version_label)
        self.emv_kernel_ver_table = QtWidgets.QTableView(self.centralwidget)
        self.emv_kernel_ver_table.setObjectName("emv_kernel_ver_table")
        self.verticalLayout_2.addWidget(self.emv_kernel_ver_table)
        self.emv_kernel_ver_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.emv_kernel_ver_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.emv_kernel_ver_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emv_kernel_ver_buttom_button_frame.setObjectName("emv_kernel_ver_buttom_button_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.emv_kernel_ver_buttom_button_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.emv_kernel_ver_hide_pushbutton = QtWidgets.QPushButton(self.emv_kernel_ver_buttom_button_frame)
        self.emv_kernel_ver_hide_pushbutton.setObjectName("emv_kernel_ver_hide_pushbutton")
        self.horizontalLayout_6.addWidget(self.emv_kernel_ver_hide_pushbutton)
        self.emv_kernel_ver_export_pushbutton = QtWidgets.QPushButton(self.emv_kernel_ver_buttom_button_frame)
        self.emv_kernel_ver_export_pushbutton.setObjectName("emv_kernel_ver_export_pushbutton")
        self.horizontalLayout_6.addWidget(self.emv_kernel_ver_export_pushbutton)
        self.verticalLayout_2.addWidget(self.emv_kernel_ver_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1386, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSource = QtWidgets.QMenu(self.menubar)
        self.menuSource.setObjectName("menuSource")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.show_menu = QtWidgets.QMenu(self.menuView)
        self.show_menu.setObjectName("show_menu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exit_menu_item = QtWidgets.QAction(MainWindow)
        self.exit_menu_item.setObjectName("exit_menu_item")
        self.jbz_pkg_menu_item = QtWidgets.QAction(MainWindow)
        self.jbz_pkg_menu_item.setObjectName("jbz_pkg_menu_item")
        self.tmsLite_menu_item = QtWidgets.QAction(MainWindow)
        self.tmsLite_menu_item.setObjectName("tmsLite_menu_item")
        self.manifestMenuItem = QtWidgets.QAction(MainWindow)
        self.manifestMenuItem.setObjectName("manifestMenuItem")
        self.emv_menu_item = QtWidgets.QAction(MainWindow)
        self.emv_menu_item.setObjectName("emv_menu_item")
        self.jfrog_show_menu_item = QtWidgets.QAction(MainWindow)
        self.jfrog_show_menu_item.setObjectName("jfrog_show_menu_item")
        self.jfrog_hide_menu_item = QtWidgets.QAction(MainWindow)
        self.jfrog_hide_menu_item.setObjectName("jfrog_hide_menu_item")
        self.jbz_show_menu_item = QtWidgets.QAction(MainWindow)
        self.jbz_show_menu_item.setObjectName("jbz_show_menu_item")
        self.jbz_hide_menu_item = QtWidgets.QAction(MainWindow)
        self.jbz_hide_menu_item.setObjectName("jbz_hide_menu_item")
        self.tms_show_menu_item = QtWidgets.QAction(MainWindow)
        self.tms_show_menu_item.setObjectName("tms_show_menu_item")
        self.tms_hide_menu_item = QtWidgets.QAction(MainWindow)
        self.tms_hide_menu_item.setObjectName("tms_hide_menu_item")
        self.manifest_show_menu_item = QtWidgets.QAction(MainWindow)
        self.manifest_show_menu_item.setObjectName("manifest_show_menu_item")
        self.manifest_hide_menu_item = QtWidgets.QAction(MainWindow)
        self.manifest_hide_menu_item.setObjectName("manifest_hide_menu_item")
        self.emv_show_menu_item = QtWidgets.QAction(MainWindow)
        self.emv_show_menu_item.setObjectName("emv_show_menu_item")
        self.emv_hide_menu_item = QtWidgets.QAction(MainWindow)
        self.emv_hide_menu_item.setObjectName("emv_hide_menu_item")
        self.show_jfrog_menu_item = QtWidgets.QAction(MainWindow)
        self.show_jfrog_menu_item.setObjectName("show_jfrog_menu_item")
        self.show_jbz_menu_item = QtWidgets.QAction(MainWindow)
        self.show_jbz_menu_item.setObjectName("show_jbz_menu_item")
        self.show_tms_menu_item = QtWidgets.QAction(MainWindow)
        self.show_tms_menu_item.setObjectName("show_tms_menu_item")
        self.show_manifest_menu_item = QtWidgets.QAction(MainWindow)
        self.show_manifest_menu_item.setObjectName("show_manifest_menu_item")
        self.show_emv_menu_item = QtWidgets.QAction(MainWindow)
        self.show_emv_menu_item.setObjectName("show_emv_menu_item")
        self.show_all_menu_item = QtWidgets.QAction(MainWindow)
        self.show_all_menu_item.setObjectName("show_all_menu_item")
        self.jfrog_menu_item = QtWidgets.QAction(MainWindow)
        self.jfrog_menu_item.setObjectName("jfrog_menu_item")
        self.show_first_conf_other_menu_item = QtWidgets.QAction(MainWindow)
        self.show_first_conf_other_menu_item.setObjectName("show_first_conf_other_menu_item")
        self.show_second_conf_other_menu_item = QtWidgets.QAction(MainWindow)
        self.show_second_conf_other_menu_item.setObjectName("show_second_conf_other_menu_item")
        self.show_third_conf_other_menu_item = QtWidgets.QAction(MainWindow)
        self.show_third_conf_other_menu_item.setObjectName("show_third_conf_other_menu_item")
        self.save_menu_item = QtWidgets.QAction(MainWindow)
        self.save_menu_item.setObjectName("save_menu_item")
        self.load_menu_item = QtWidgets.QAction(MainWindow)
        self.load_menu_item.setObjectName("load_menu_item")
        self.menuFile.addAction(self.save_menu_item)
        self.menuFile.addAction(self.load_menu_item)
        self.menuFile.addAction(self.exit_menu_item)
        self.menuSource.addAction(self.jfrog_menu_item)
        self.menuSource.addAction(self.jbz_pkg_menu_item)
        self.menuSource.addAction(self.tmsLite_menu_item)
        self.menuSource.addAction(self.emv_menu_item)
        self.show_menu.addAction(self.show_jfrog_menu_item)
        self.show_menu.addAction(self.show_jbz_menu_item)
        self.show_menu.addAction(self.show_first_conf_other_menu_item)
        self.show_menu.addAction(self.show_second_conf_other_menu_item)
        self.show_menu.addAction(self.show_third_conf_other_menu_item)
        self.show_menu.addAction(self.show_manifest_menu_item)
        self.show_menu.addAction(self.show_tms_menu_item)
        self.show_menu.addAction(self.show_emv_menu_item)
        self.menuView.addAction(self.show_menu.menuAction())
        self.menuView.addAction(self.show_all_menu_item)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSource.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.exit_menu_item.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Version Checker"))
        self.jfrog_label.setText(_translate("MainWindow", "Jfrog Artifactory"))
        self.jfrog_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.jfrog_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.job_bundle_pkg_ver_label.setText(_translate("MainWindow", "Package Version"))
        self.pkg_header_pushbutton.setText(_translate("MainWindow", "Header"))
        self.jbz_pkg_version_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.jbz_pkg_version_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.first_conf_other_pkg_ver_label.setText(_translate("MainWindow", "1st Conf and Other Version"))
        self.first_conf_other_pkg_header_pushbutton.setText(_translate("MainWindow", "Header"))
        self.first_conf_other_pkg_version_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.first_conf_other_pkg_version_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.second_conf_other_pkg_ver_label.setText(_translate("MainWindow", "2nd Conf and Other Version"))
        self.second_conf_other_pkg_header_pushbutton.setText(_translate("MainWindow", "Header"))
        self.second_conf_other_pkg_version_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.second_conf_other_pkg_version_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.third_conf_other_pkg_ver_label.setText(_translate("MainWindow", "3rd Conf and Other Version"))
        self.third_conf_other_pkg_header_pushbutton.setText(_translate("MainWindow", "Header"))
        self.third_conf_other_pkg_version_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.third_conf_other_pkg_version_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.manifest_file_label.setText(_translate("MainWindow", "Manifest File"))
        self.manifest_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.manifest_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.tms_param_label.setText(_translate("MainWindow", "TMSLite Parameters"))
        self.tms_param_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.tms_param_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.emv_kernel_version_label.setText(_translate("MainWindow", "EMV Kernel Version"))
        self.emv_kernel_ver_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.emv_kernel_ver_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSource.setTitle(_translate("MainWindow", "Source"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.show_menu.setTitle(_translate("MainWindow", "Show"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.exit_menu_item.setText(_translate("MainWindow", "Exit"))
        self.jbz_pkg_menu_item.setText(_translate("MainWindow", "Packages"))
        self.tmsLite_menu_item.setText(_translate("MainWindow", "TMSLite"))
        self.manifestMenuItem.setText(_translate("MainWindow", "Manifest"))
        self.emv_menu_item.setText(_translate("MainWindow", "EMV"))
        self.jfrog_show_menu_item.setText(_translate("MainWindow", "Show"))
        self.jfrog_hide_menu_item.setText(_translate("MainWindow", "Hide"))
        self.jbz_show_menu_item.setText(_translate("MainWindow", "Show"))
        self.jbz_hide_menu_item.setText(_translate("MainWindow", "Hide"))
        self.tms_show_menu_item.setText(_translate("MainWindow", "Show"))
        self.tms_hide_menu_item.setText(_translate("MainWindow", "Hide"))
        self.manifest_show_menu_item.setText(_translate("MainWindow", "Show"))
        self.manifest_hide_menu_item.setText(_translate("MainWindow", "Hide"))
        self.emv_show_menu_item.setText(_translate("MainWindow", "Show"))
        self.emv_hide_menu_item.setText(_translate("MainWindow", "Hide"))
        self.show_jfrog_menu_item.setText(_translate("MainWindow", "Jfrog Artifactory"))
        self.show_jbz_menu_item.setText(_translate("MainWindow", "Job Bundle Version"))
        self.show_tms_menu_item.setText(_translate("MainWindow", "TMSLite Parameters"))
        self.show_manifest_menu_item.setText(_translate("MainWindow", "Manifest File"))
        self.show_emv_menu_item.setText(_translate("MainWindow", "EMV Kernel Version"))
        self.show_all_menu_item.setText(_translate("MainWindow", "Show All"))
        self.jfrog_menu_item.setText(_translate("MainWindow", "JFrog"))
        self.show_first_conf_other_menu_item.setText(_translate("MainWindow", "1 - Conf / Other Version"))
        self.show_second_conf_other_menu_item.setText(_translate("MainWindow", "2 - Conf / Other Version"))
        self.show_third_conf_other_menu_item.setText(_translate("MainWindow", "3 - Conf / Other Version"))
        self.save_menu_item.setText(_translate("MainWindow", "Save"))
        self.load_menu_item.setText(_translate("MainWindow", "Load"))
