# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1131, 717)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.jfrog_result_label = QtWidgets.QLabel(self.centralwidget)
        self.jfrog_result_label.setObjectName("jfrog_result_label")
        self.verticalLayout_8.addWidget(self.jfrog_result_label)
        self.jfrog_result_table = QtWidgets.QTableView(self.centralwidget)
        self.jfrog_result_table.setObjectName("jfrog_result_table")
        self.verticalLayout_8.addWidget(self.jfrog_result_table)
        self.merge_result_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.merge_result_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.merge_result_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.merge_result_buttom_button_frame.setObjectName("merge_result_buttom_button_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.merge_result_buttom_button_frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.jfrog_result_hide_pushbutton = QtWidgets.QPushButton(self.merge_result_buttom_button_frame)
        self.jfrog_result_hide_pushbutton.setObjectName("jfrog_result_hide_pushbutton")
        self.horizontalLayout_7.addWidget(self.jfrog_result_hide_pushbutton)
        self.jfrog_result_export_pushbutton = QtWidgets.QPushButton(self.merge_result_buttom_button_frame)
        self.jfrog_result_export_pushbutton.setObjectName("jfrog_result_export_pushbutton")
        self.horizontalLayout_7.addWidget(self.jfrog_result_export_pushbutton)
        self.verticalLayout_8.addWidget(self.merge_result_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.job_bundle_pkg_ver_label = QtWidgets.QLabel(self.centralwidget)
        self.job_bundle_pkg_ver_label.setObjectName("job_bundle_pkg_ver_label")
        self.verticalLayout_7.addWidget(self.job_bundle_pkg_ver_label)
        self.jbz_pkg_ver_table = QtWidgets.QTableView(self.centralwidget)
        self.jbz_pkg_ver_table.setObjectName("jbz_pkg_ver_table")
        self.verticalLayout_7.addWidget(self.jbz_pkg_ver_table)
        self.jbz_pkg_ver_buttom_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.jbz_pkg_ver_buttom_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.jbz_pkg_ver_buttom_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.jbz_pkg_ver_buttom_button_frame.setObjectName("jbz_pkg_ver_buttom_button_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.jbz_pkg_ver_buttom_button_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.jbz_pkg_version_hide_pushbutton = QtWidgets.QPushButton(self.jbz_pkg_ver_buttom_button_frame)
        self.jbz_pkg_version_hide_pushbutton.setObjectName("jbz_pkg_version_hide_pushbutton")
        self.horizontalLayout_2.addWidget(self.jbz_pkg_version_hide_pushbutton)
        self.jbz_pkg_version_export_pushbutton = QtWidgets.QPushButton(self.jbz_pkg_ver_buttom_button_frame)
        self.jbz_pkg_version_export_pushbutton.setObjectName("jbz_pkg_version_export_pushbutton")
        self.horizontalLayout_2.addWidget(self.jbz_pkg_version_export_pushbutton)
        self.verticalLayout_7.addWidget(self.jbz_pkg_ver_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.tms_param_hide_pushbutton = QtWidgets.QPushButton(self.tms_param_buttom_button_frame)
        self.tms_param_hide_pushbutton.setObjectName("tms_param_hide_pushbutton")
        self.horizontalLayout_3.addWidget(self.tms_param_hide_pushbutton)
        self.tms_param_export_pushbutton = QtWidgets.QPushButton(self.tms_param_buttom_button_frame)
        self.tms_param_export_pushbutton.setObjectName("tms_param_export_pushbutton")
        self.horizontalLayout_3.addWidget(self.tms_param_export_pushbutton)
        self.verticalLayout_6.addWidget(self.tms_param_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.manifest_hide_pushbutton = QtWidgets.QPushButton(self.manifest_buttom_button_frame)
        self.manifest_hide_pushbutton.setObjectName("manifest_hide_pushbutton")
        self.horizontalLayout_5.addWidget(self.manifest_hide_pushbutton)
        self.manifest_export_pushbutton = QtWidgets.QPushButton(self.manifest_buttom_button_frame)
        self.manifest_export_pushbutton.setObjectName("manifest_export_pushbutton")
        self.horizontalLayout_5.addWidget(self.manifest_export_pushbutton)
        self.verticalLayout_5.addWidget(self.manifest_buttom_button_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSource = QtWidgets.QMenu(self.menubar)
        self.menuSource.setObjectName("menuSource")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuResult = QtWidgets.QMenu(self.menuView)
        self.menuResult.setObjectName("menuResult")
        self.menuJob_Bundle_Package_Version = QtWidgets.QMenu(self.menuView)
        self.menuJob_Bundle_Package_Version.setObjectName("menuJob_Bundle_Package_Version")
        self.menuTMSParameter = QtWidgets.QMenu(self.menuView)
        self.menuTMSParameter.setObjectName("menuTMSParameter")
        self.menuManifest_File = QtWidgets.QMenu(self.menuView)
        self.menuManifest_File.setObjectName("menuManifest_File")
        self.menuEMV_Kernel_Version = QtWidgets.QMenu(self.menuView)
        self.menuEMV_Kernel_Version.setObjectName("menuEMV_Kernel_Version")
        self.menuShow_Only = QtWidgets.QMenu(self.menuView)
        self.menuShow_Only.setObjectName("menuShow_Only")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exit_MenuItem = QtWidgets.QAction(MainWindow)
        self.exit_MenuItem.setObjectName("exit_MenuItem")
        self.jbz_pkg_menuItem = QtWidgets.QAction(MainWindow)
        self.jbz_pkg_menuItem.setObjectName("jbz_pkg_menuItem")
        self.tmsLiteMenuItem = QtWidgets.QAction(MainWindow)
        self.tmsLiteMenuItem.setObjectName("tmsLiteMenuItem")
        self.manifestMenuItem = QtWidgets.QAction(MainWindow)
        self.manifestMenuItem.setObjectName("manifestMenuItem")
        self.emvMenuItem = QtWidgets.QAction(MainWindow)
        self.emvMenuItem.setObjectName("emvMenuItem")
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
        self.show_only_jfrog_result_menu_item = QtWidgets.QAction(MainWindow)
        self.show_only_jfrog_result_menu_item.setObjectName("show_only_jfrog_result_menu_item")
        self.show_only_jbz_menu_item = QtWidgets.QAction(MainWindow)
        self.show_only_jbz_menu_item.setObjectName("show_only_jbz_menu_item")
        self.show_only_tms_menu_item = QtWidgets.QAction(MainWindow)
        self.show_only_tms_menu_item.setObjectName("show_only_tms_menu_item")
        self.show_only_manifest_menu_item = QtWidgets.QAction(MainWindow)
        self.show_only_manifest_menu_item.setObjectName("show_only_manifest_menu_item")
        self.show_only_emv_menu_item = QtWidgets.QAction(MainWindow)
        self.show_only_emv_menu_item.setObjectName("show_only_emv_menu_item")
        self.show_all_menu_item = QtWidgets.QAction(MainWindow)
        self.show_all_menu_item.setObjectName("show_all_menu_item")
        self.jfrogMenuItem = QtWidgets.QAction(MainWindow)
        self.jfrogMenuItem.setObjectName("jfrogMenuItem")
        self.menuFile.addAction(self.exit_MenuItem)
        self.menuSource.addAction(self.jbz_pkg_menuItem)
        self.menuSource.addAction(self.tmsLiteMenuItem)
        self.menuSource.addAction(self.emvMenuItem)
        self.menuSource.addAction(self.jfrogMenuItem)
        self.menuResult.addAction(self.jfrog_show_menu_item)
        self.menuResult.addAction(self.jfrog_hide_menu_item)
        self.menuJob_Bundle_Package_Version.addAction(self.jbz_show_menu_item)
        self.menuJob_Bundle_Package_Version.addAction(self.jbz_hide_menu_item)
        self.menuTMSParameter.addAction(self.tms_show_menu_item)
        self.menuTMSParameter.addAction(self.tms_hide_menu_item)
        self.menuManifest_File.addAction(self.manifest_show_menu_item)
        self.menuManifest_File.addAction(self.manifest_hide_menu_item)
        self.menuEMV_Kernel_Version.addAction(self.emv_show_menu_item)
        self.menuEMV_Kernel_Version.addAction(self.emv_hide_menu_item)
        self.menuShow_Only.addAction(self.show_only_jfrog_result_menu_item)
        self.menuShow_Only.addAction(self.show_only_jbz_menu_item)
        self.menuShow_Only.addAction(self.show_only_tms_menu_item)
        self.menuShow_Only.addAction(self.show_only_manifest_menu_item)
        self.menuShow_Only.addAction(self.show_only_emv_menu_item)
        self.menuView.addAction(self.menuResult.menuAction())
        self.menuView.addAction(self.menuJob_Bundle_Package_Version.menuAction())
        self.menuView.addAction(self.menuTMSParameter.menuAction())
        self.menuView.addAction(self.menuManifest_File.menuAction())
        self.menuView.addAction(self.menuEMV_Kernel_Version.menuAction())
        self.menuView.addAction(self.menuShow_Only.menuAction())
        self.menuView.addAction(self.show_all_menu_item)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSource.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.exit_MenuItem.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Version Checker"))
        self.title_label.setText(_translate("MainWindow", "VERSION CHECKER"))
        self.jfrog_result_label.setText(_translate("MainWindow", "Jfrog Artifactory"))
        self.jfrog_result_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.jfrog_result_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.job_bundle_pkg_ver_label.setText(_translate("MainWindow", "Package Version"))
        self.jbz_pkg_version_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.jbz_pkg_version_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.tms_param_label.setText(_translate("MainWindow", "TMSLite Parameters"))
        self.tms_param_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.tms_param_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.manifest_file_label.setText(_translate("MainWindow", "Manifest File"))
        self.manifest_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.manifest_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.emv_kernel_version_label.setText(_translate("MainWindow", "EMV Kernel Version"))
        self.emv_kernel_ver_hide_pushbutton.setText(_translate("MainWindow", "Hide"))
        self.emv_kernel_ver_export_pushbutton.setText(_translate("MainWindow", "Export"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSource.setTitle(_translate("MainWindow", "Source"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuResult.setTitle(_translate("MainWindow", "JFrog Artifactory"))
        self.menuJob_Bundle_Package_Version.setTitle(_translate("MainWindow", "Job Bundle Package Version"))
        self.menuTMSParameter.setTitle(_translate("MainWindow", "TMSLite Parameters"))
        self.menuManifest_File.setTitle(_translate("MainWindow", "Manifest File"))
        self.menuEMV_Kernel_Version.setTitle(_translate("MainWindow", "EMV Kernel Version"))
        self.menuShow_Only.setTitle(_translate("MainWindow", "Show Only"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.exit_MenuItem.setText(_translate("MainWindow", "Exit"))
        self.jbz_pkg_menuItem.setText(_translate("MainWindow", "Packages"))
        self.tmsLiteMenuItem.setText(_translate("MainWindow", "TMSLite"))
        self.manifestMenuItem.setText(_translate("MainWindow", "Manifest"))
        self.emvMenuItem.setText(_translate("MainWindow", "EMV"))
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
        self.show_only_jfrog_result_menu_item.setText(_translate("MainWindow", "Jfrog Artifactory"))
        self.show_only_jbz_menu_item.setText(_translate("MainWindow", "Job Bundle Package Version"))
        self.show_only_tms_menu_item.setText(_translate("MainWindow", "TMSLite Parameters"))
        self.show_only_manifest_menu_item.setText(_translate("MainWindow", "Manifest File"))
        self.show_only_emv_menu_item.setText(_translate("MainWindow", "EMV Kernel Version"))
        self.show_all_menu_item.setText(_translate("MainWindow", "Show All"))
        self.jfrogMenuItem.setText(_translate("MainWindow", "JFrog"))
