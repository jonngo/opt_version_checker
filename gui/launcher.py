from PyQt5.QtWidgets import QFileDialog
from gui import Ui_MainWindow
from gui import Ui_pkg_widget
from gui import Ui_emv_widget
from gui import Ui_tms_widget
from PyQt5 import QtCore, QtGui, QtWidgets
from jbz_extraction import JobBundleExtraction
from emv_version import EmvExtraction
from tms_parameters import TmsExtraction
import sys
from PyQt5.QtCore import Qt
import pandas as pd
import json



class Launcher(Ui_MainWindow, Ui_pkg_widget, Ui_emv_widget, Ui_tms_widget):
    def __init__(self):
        """
            Configuration variables of package version
                - conf_base_xtrak_path
                - conf_sevenZ_exe
                - conf_manifest
                - conf_regexp_string
        """

        with open("config.json") as json_data_file:
            data = json.load(json_data_file)
            for conf in data['pkg_version_cfg']:
                if 'base_xtrak_path' in conf:
                    self.conf_base_xtrak_path = conf['base_xtrak_path']
                elif 'sevenZ_exe' in conf:
                    self.conf_sevenZ_exe = conf['sevenZ_exe']
                elif 'manifest_file' in conf:
                    self.conf_manifest = conf['manifest_file']
                elif 'regexp_string' in conf:
                    self.conf_regexp_string = conf['regexp_string']

    #MAIN
    def extendUI(self,version_checker_mainwindow):
        self.jbz_pkg_menuItem.triggered.connect(self.openPkgWidget)
        self.emvMenuItem.triggered.connect(self.openEmvWidget)
        self.tmsLiteMenuItem.triggered.connect(self.openTmsWidget)


        #Initialize Widgets
        self.initPkgWidget()
        self.initEmvWidget()
        self.initTmsWidget()

        #hide pushbutton
        self.merge_result_hide_pushbutton.clicked.connect(lambda state, x={'result':False}: self.show_hide_panel(x))
        self.jbz_pkg_version_hide_pushbutton.clicked.connect(lambda state, x={'jbz':False}: self.show_hide_panel(x))
        self.tms_param_hide_pushbutton.clicked.connect(lambda state, x={'tms': False}: self.show_hide_panel(x))
        self.manifest_hide_pushbutton.clicked.connect(lambda state, x={'manifest': False}: self.show_hide_panel(x))
        self.emv_kernel_ver_hide_pushbutton.clicked.connect(lambda state, x={'emv': False}: self.show_hide_panel(x))
        #show_all view
        self.show_all_menu_item.triggered.connect(lambda state, x={'result':True,'jbz':True,'tms': True,'manifest': True,'emv': True}: self.show_hide_panel(x))
        #show_only_view
        self.show_only_merge_result_menu_item.triggered.connect(lambda state, x={'result':True,'jbz':False,'tms': False,'manifest': False,'emv': False}: self.show_hide_panel(x))
        self.show_only_jbz_menu_item.triggered.connect(lambda state, x={'result':False,'jbz':True,'tms': False,'manifest': False,'emv': False}: self.show_hide_panel(x))
        self.show_only_tms_menu_item.triggered.connect(lambda state, x={'result':False,'jbz':False,'tms': True,'manifest': False,'emv': False}: self.show_hide_panel(x))
        self.show_only_manifest_menu_item.triggered.connect(lambda state, x={'result':False,'jbz':False,'tms': False,'manifest': True,'emv': False}: self.show_hide_panel(x))
        self.show_only_emv_menu_item.triggered.connect(lambda state, x={'result':False,'jbz':False,'tms': False,'manifest': False,'emv': True}: self.show_hide_panel(x))
        #show
        self.merge_show_menu_item.triggered.connect(lambda state, x={'result':True}: self.show_hide_panel(x))
        self.jbz_show_menu_item.triggered.connect(lambda state, x={'jbz':True}: self.show_hide_panel(x))
        self.tms_show_menu_item.triggered.connect(lambda state, x={'tms': True}: self.show_hide_panel(x))
        self.manifest_show_menu_item.triggered.connect(lambda state, x={'manifest': True}: self.show_hide_panel(x))
        self.emv_show_menu_item.triggered.connect(lambda state, x={'emv': True}: self.show_hide_panel(x))
        #hide
        self.merge_hide_menu_item.triggered.connect(lambda state, x={'result':False}: self.show_hide_panel(x))
        self.jbz_hide_menu_item.triggered.connect(lambda state, x={'jbz':False}: self.show_hide_panel(x))
        self.tms_hide_menu_item.triggered.connect(lambda state, x={'tms':False}: self.show_hide_panel(x))
        self.manifest_hide_menu_item.triggered.connect(lambda state, x={'manifest':False}: self.show_hide_panel(x))
        self.emv_hide_menu_item.triggered.connect(lambda state, x={'emv':False}: self.show_hide_panel(x))

        version_checker_mainwindow.show()

    #JBZ PACKAGE VERSION
    def openPkgWidget(self):
        self.pkg_ui.extractionPathLineEdit.setText(self.conf_base_xtrak_path)
        self.pkg_ui.sevenZlineEdit.setText(self.conf_sevenZ_exe)
        self.pkg_ui.jbz_manifest_line_edit.setText(self.conf_manifest)
        self.pkg_ui.jbz_regex_match_ver_line_edit.setText(self.conf_regexp_string)
        self.pkg_widget.show()

    def open_file_dialog(self,line_edit):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName()

        if file:
            line_edit.setText(file)

    def searchJbzPath(self):
        self.open_file_dialog(self.pkg_ui.jbzPathLineEdit)

    def search_other_pkg_path_1(self):
        self.open_file_dialog(self.pkg_ui.conf_other_pkg_1_line_edit)

    def search_other_pkg_path_2(self):
        self.open_file_dialog(self.pkg_ui.conf_other_pkg_2_line_edit)

    def search_other_pkg_path_3(self):
        self.open_file_dialog(self.pkg_ui.conf_other_pkg_3_line_edit)

    def extractJbz(self):
        jbx = JobBundleExtraction()

        jbx.base_xtrak_path = self.conf_base_xtrak_path
        jbx.sevenZ_exe = self.conf_sevenZ_exe
        jbx.manifest_file = self.conf_manifest
        jbx.regexp_string = self.conf_regexp_string

        if self.pkg_ui.jbzPathLineEdit.text() != "":
            result_jbz,result_manifest = jbx.extract(self.pkg_ui.jbzPathLineEdit.text())

        if self.pkg_ui.conf_other_pkg_1_line_edit.text() != "":
            result_conf_other_1,_ = jbx.extract(self.pkg_ui.conf_other_pkg_1_line_edit.text())
            result_jbz = result_jbz + result_conf_other_1

        if self.pkg_ui.conf_other_pkg_2_line_edit.text() != "":
            result_conf_other_2,_ = jbx.extract(self.pkg_ui.conf_other_pkg_2_line_edit.text())
            result_jbz = result_jbz + result_conf_other_2

        if self.pkg_ui.conf_other_pkg_3_line_edit.text() != "":
            result_conf_other_3,_ = jbx.extract(self.pkg_ui.conf_other_pkg_3_line_edit.text())
            result_jbz = result_jbz + result_conf_other_3

        self.pkg_widget.hide()
        self.populate_jb_table(result_jbz)
        if result_manifest is not None:
            self.populate_manifest_table(result_manifest)

    def populate_jb_table(self,result):
        header = result.pop(0)
        rn = [str(c+1) for c in range(0,len(result))]
        data = pd.DataFrame(result, columns=header,index=rn)
        self.model = TableModel(data)
        self.jbz_pkg_ver_table.setModel(self.model)

    def populate_manifest_table(self,result):
        header = result.pop(0)
        rn = [str(c+1) for c in range(0,len(result))]
        data = pd.DataFrame(result, columns=header,index=rn)
        self.model = TableModel(data)
        self.manifest_table.setModel(self.model)

    def initPkgWidget(self):
        self.pkg_widget = QtWidgets.QWidget()
        self.pkg_ui = Ui_pkg_widget()
        self.pkg_ui.setupUi(self.pkg_widget)
        self.pkg_ui.jbzPathPushButton.clicked.connect(self.searchJbzPath)
        self.pkg_ui.extractPushButton.clicked.connect(self.extractJbz)
        self.pkg_ui.conf_other_pkg_1_push_button.clicked.connect(self.search_other_pkg_path_1)
        self.pkg_ui.conf_other_pkg_2_push_button.clicked.connect(self.search_other_pkg_path_2)
        self.pkg_ui.conf_other_pkg_3_push_button.clicked.connect(self.search_other_pkg_path_3)

    #EMV KERNEL VERSION
    def initEmvWidget(self):
        self.emv_widget = QtWidgets.QWidget()
        self.emv_ui = Ui_emv_widget()
        self.emv_ui.setupUi(self.emv_widget)
        self.emv_ui.extractEMVPushButton.clicked.connect(self.extractEMV)
        self.device_customer_list = ["G6-300","G7-100 NCR","G7-100 Canada","G6-200"]
        self.emv_ui.emv_device_comboBox.addItems(self.device_customer_list)

    def openEmvWidget(self):
        emvx = EmvExtraction()
        self.emv_ui.emv_ver_url_lineedit.setText(emvx.emv_ver_url)
        self.emv_ui.chrome_driver_lineEdit.setText(emvx.chrome_driver_filepath)
        self.emv_widget.show()

    def extractEMV(self):
        #login to confluence and get EMV version
        emvx = EmvExtraction()
        index = self.emv_ui.emv_device_comboBox.currentIndex()
        dc = self.device_customer_list[index].split(' ')
        if len(dc) == 1:
            selected_device = dc[0]
            selected_customer = "ALL"
        else:
            selected_device = dc[0]
            selected_customer = dc[1]
        result = emvx.login(self.emv_ui.usernameLineEdit.text(),self.emv_ui.passwordLineEdit.text(),selected_device,selected_customer)
        self.populate_emv_table(result)
        self.emv_widget.hide()

    def populate_emv_table(self,result):
        header = result.pop(0)
        rn = [str(c+1) for c in range(0,len(result))]
        data = pd.DataFrame(result, columns=header,index=rn)
        self.model = TableModel(data)
        # self.emv_widget.hide()
        self.emv_kernel_ver_table.setModel(self.model)

    #TMSLITE PARAMETERS
    def initTmsWidget(self):
        self.tms_widget = QtWidgets.QWidget()
        self.tms_ui = Ui_tms_widget()
        self.tms_ui.setupUi(self.tms_widget)
        self.tms_ui.tms_param_search_push_button.clicked.connect(self.search_tms_params_csv)
        self.tms_ui.tms_param_load_push_button.clicked.connect(self.loadTMS)

    def openTmsWidget(self):
        self.tms_widget.show()

    def loadTMS(self):
        tmsx = TmsExtraction()
        result = tmsx.load_tms_parameters(self.tms_ui.tmslite_param_line_edit.text())
        self.tms_widget.hide()
        self.populate_tms_table(result)

    def search_tms_params_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(None,'Open file','D:\\JonNgoStorage',"csv files (*.csv))")

        #file = str(QFileDialog.getExistingDirectory())
        if file:
            self.tms_ui.tmslite_param_line_edit.setText(file)

    def populate_tms_table(self,result):
        header = result.pop(0)
        rn = [str(c+1) for c in range(0,len(result))]
        data = pd.DataFrame(result, columns=header,index=rn)
        self.model = TableModel(data)
        self.tms_param_table.setModel(self.model)

    #Hide panel
    def show_hide_panel(self, hs_dict):
        for key, value in hs_dict.items():
            # print(key)
            if key == 'result':
                if value:
                    #show result
                    self.merge_result_buttom_button_frame.show()
                    self.merge_result_table.show()
                    self.merge_result_label.show()
                else:
                    #hide result
                    self.merge_result_buttom_button_frame.hide()
                    self.merge_result_table.hide()
                    self.merge_result_label.hide()
            if key == 'jbz':
                 if value:
                     #show jbz
                     self.jbz_pkg_ver_buttom_button_frame.show()
                     self.jbz_pkg_ver_table.show()
                     self.job_bundle_pkg_ver_label.show()
                 else:
                     #hide jbz
                     self.jbz_pkg_ver_buttom_button_frame.hide()
                     self.jbz_pkg_ver_table.hide()
                     self.job_bundle_pkg_ver_label.hide()

            if key == 'tms':
                 if value:
                     #show tms
                     self.tms_param_buttom_button_frame.show()
                     self.tms_param_table.show()
                     self.tms_param_label.show()
                 else:
                     #hide tms
                     self.tms_param_buttom_button_frame.hide()
                     self.tms_param_table.hide()
                     self.tms_param_label.hide()

            if key == 'manifest':
                if value:
                    # show manifest
                    self.manifest_buttom_button_frame.show()
                    self.manifest_table.show()
                    self.manifest_file_label.show()
                else:
                    # hide manifest
                    self.manifest_buttom_button_frame.hide()
                    self.manifest_table.hide()
                    self.manifest_file_label.hide()

            if key == 'emv':
                if value:
                    # show emv
                    self.emv_kernel_ver_buttom_button_frame.show()
                    self.emv_kernel_ver_table.show()
                    self.emv_kernel_version_label.show()
                else:
                    # hide emv
                    self.emv_kernel_ver_buttom_button_frame.hide()
                    self.emv_kernel_ver_table.hide()
                    self.emv_kernel_version_label.hide()

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    version_checker_mainwindow = QtWidgets.QMainWindow()
    ui = Launcher()
    ui.setupUi(version_checker_mainwindow)
    ui.extendUI(version_checker_mainwindow)
    sys.exit(app.exec_())

# To convert ui to py
# pyuic5 main.ui -o main.py
# pyuic5 emv.ui -o emv.py
# pyuic5 tms_param.ui -o tms_param.py
# pyuic5 jbz_pkg.ui -o jbz_pkg.py

# To make .exe
# pyinstaller --noconsole --onefile --windowed --icon=../vc.ico launcher.py

# does not work
# pyinstaller --noconsole --onefile --windowed --icon=vc.ico gui/launcher.py
