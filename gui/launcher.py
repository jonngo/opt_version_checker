import os
from pathlib import Path
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView, QMessageBox
import package
from gui import Ui_MainWindow
from gui import Ui_pkg_widget
from gui import Ui_emv_widget
from gui import Ui_tms_widget
from gui import Ui_jfrog_widget
from gui import Ui_save_widget
from gui import Ui_load_widget
from gui import Ui_map_widget
from gui import Ui_compare_widget
from gui import Ui_settings_widget
from PyQt5 import QtCore, QtWidgets
from jbz_extraction import JobBundleExtraction
from emv_version import EmvExtraction
from tms_parameters import TmsExtraction
from jfrog_artifactory import JfrogArtifactory
import sys
from PyQt5.QtCore import Qt
import pandas as pd
import json


class Launcher(Ui_MainWindow, Ui_pkg_widget, Ui_emv_widget, Ui_tms_widget, Ui_jfrog_widget, Ui_save_widget, Ui_load_widget, Ui_map_widget, Ui_compare_widget, Ui_settings_widget):

    # ██╗███╗   ██╗██╗████████╗██╗ █████╗ ██╗     ██╗███████╗███████╗
    # ██║████╗  ██║██║╚══██╔══╝██║██╔══██╗██║     ██║╚══███╔╝██╔════╝
    # ██║██╔██╗ ██║██║   ██║   ██║███████║██║     ██║  ███╔╝ █████╗
    # ██║██║╚██╗██║██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══╝
    # ██║██║ ╚████║██║   ██║   ██║██║  ██║███████╗██║███████╗███████╗
    # ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚══════╝

    def __init__(self):
        try:
            with open("config.json") as json_data_file:
                data = json.load(json_data_file)
                for conf in data['pkg_version_cfg']:
                    """
                        Configuration variables of package version
                            - conf_base_xtrak_path
                            - conf_sevenZ_exe
                            - conf_manifest
                            - conf_default_pkg_folder
                    """

                    if 'base_xtrak_path' in conf:
                        self.conf_base_xtrak_path = self.end_with_slash(self.determine_path(conf['base_xtrak_path']))
                    elif 'sevenZ_exe' in conf:
                        self.conf_sevenZ_exe = conf['sevenZ_exe']
                    elif 'manifest_file' in conf:
                        self.conf_manifest = conf['manifest_file']
                    elif 'default_pkg_location' in conf:
                        self.conf_default_pkg_folder = self.end_with_slash(self.determine_path(conf['default_pkg_location']))

                for conf in data['emv_version_cfg']:
                    """
                    Configuration variables of EMV version
                        - conf_emv_ver_url
                        - conf_chrome_driver_filepath
                    """

                    if 'emv_ver_url' in conf:
                        self.conf_emv_ver_url = conf['emv_ver_url']
                    elif 'chrome_driver_filepath' in conf:
                        self.conf_chrome_driver_filepath = conf['chrome_driver_filepath']

                for conf in data['load_cfg']:
                    """
                    Configuration variables of Load
                        - conf_load_path
                    """

                    # save path will also use this path
                    if 'load_path' in conf:
                        self.conf_load_path = self.end_with_slash(self.determine_path(conf['load_path']))

                for conf in data['tms_cfg']:
                    """
                    Configuration variables of TMSLite parameters
                        - conf_tms_path
                    """

                    if 'tms_path' in conf:
                        self.conf_tms_path = self.end_with_slash(self.determine_path(conf['tms_path']))

                for conf in data['compare_cfg']:
                    """
                    Configuration variables of version comparison
                        - conf_compare_path
                    """

                    if 'compare_path' in conf:
                        self.conf_compare_path = self.end_with_slash(self.determine_path(conf['compare_path']))

                for conf in data['jfrog_cfg']:
                    """
                    Configuration variables of jfrog repo path
                        - conf_jfrog_path
                    """

                    if 'jfrog_repo_path' in conf:
                        self.conf_jfrog_path = self.end_with_slash(self.determine_path(conf['jfrog_repo_path']))

                #Initialize all version result list
                self.result_jbz = None
                self.result_conf_other_1 = None
                self.result_conf_other_2 = None
                self.result_conf_other_3 = None
                self.result_manifest = None
                self.result_emv = None
                self.result_tms = None
                self.result_of_jfrog_list = None

                self.result_jbz_ref = None
                self.result_conf_other_1_ref = None
                self.result_conf_other_2_ref = None
                self.result_conf_other_3_ref = None
        except Exception as e:
            print (str(e))

    #return the home path if 'home' is used as path folder, otherwise, use the path in the config.
    def determine_path(self, path):
        try:
            return str(Path.home()).replace("\\","/") if path.lower() == 'home' else path.replace("\\","/")
        except Exception as e:
            print (str(e))

    #put a slash at the end of the path if it doesn't have.
    def end_with_slash(self, path):
        try:
            return path if path.endswith('/') else path+"/"
        except Exception as e:
            print (str(e))

    # ███╗   ███╗ █████╗ ██╗███╗   ██╗    ██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗    ██╗███╗   ██╗██╗████████╗
    # ████╗ ████║██╔══██╗██║████╗  ██║    ██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║    ██║████╗  ██║██║╚══██╔══╝
    # ██╔████╔██║███████║██║██╔██╗ ██║    ██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║    ██║██╔██╗ ██║██║   ██║
    # ██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║    ██║██║╚██╗██║██║   ██║
    # ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝    ██║██║ ╚████║██║   ██║
    # ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝

    def extendUI(self,version_checker_mainwindow):
        try:
            version_checker_mainwindow.resize(640, 480)
            #Initialize Widgets
            self.init_jfrog_widget()
            self.init_pkg_widget()
            self.init_emv_widget()
            self.init_tms_widget()
            self.init_save_widget()
            self.init_load_widget()
            self.init_map_widget()
            self.init_compare_widget()
            self.init_settings_widget()

            #Source Menu
            self.jbz_pkg_menu_item.triggered.connect(self.open_pkg_widget)
            self.emv_menu_item.triggered.connect(self.open_emv_widget)
            self.tmsLite_menu_item.triggered.connect(self.open_tms_widget)
            self.jfrog_menu_item.triggered.connect(self.open_jfrog_widget)
            self.save_menu_item.triggered.connect(self.open_save_widget)
            self.load_menu_item.triggered.connect(self.open_load_widget)
            self.map_menu_item.triggered.connect(self.open_map_widget)
            self.compare_menu_item.triggered.connect(self.open_compare_widget)
            self.settings_menu_item.triggered.connect(self.open_settings_widget)

            #View Menu - Show Menu
            #show_only_view
            self.show_jfrog_menu_item.triggered.connect(lambda state, x={'jfrog':True}: self.show_hide_panel(x))
            self.show_jbz_menu_item.triggered.connect(lambda state, x={'jbz':True}: self.show_hide_panel(x))
            self.show_first_conf_other_menu_item.triggered.connect(lambda state, x={'first': True}: self.show_hide_panel(x))
            self.show_second_conf_other_menu_item.triggered.connect(lambda state, x={'second': True}: self.show_hide_panel(x))
            self.show_third_conf_other_menu_item.triggered.connect(lambda state, x={'third': True}: self.show_hide_panel(x))
            self.show_manifest_menu_item.triggered.connect(lambda state, x={'manifest': True}: self.show_hide_panel(x))
            self.show_tms_menu_item.triggered.connect(lambda state, x={'tms': True}: self.show_hide_panel(x))
            self.show_emv_menu_item.triggered.connect(lambda state, x={'emv': True}: self.show_hide_panel(x))

            #List Model for the package header list
            self.pkg_header_list_model = QStandardItemModel(self.pkg_listview)
            self.first_conf_other_pkg_header_list_model = QStandardItemModel(self.first_conf_other_pkg_listview)
            self.second_conf_other_pkg_header_list_model = QStandardItemModel(self.second_conf_other_pkg_listview)
            self.third_conf_other_pkg_header_list_model = QStandardItemModel(self.third_conf_other_pkg_listview)

            #hide pushbutton
            self.jfrog_hide_pushbutton.clicked.connect(lambda state, x={'jfrog':False}: self.show_hide_panel(x))
            self.jbz_pkg_version_hide_pushbutton.clicked.connect(lambda state, x={'jbz':False}: self.show_hide_panel(x))
            self.first_conf_other_pkg_version_hide_pushbutton.clicked.connect(lambda state, x={'first':False}: self.show_hide_panel(x))
            self.second_conf_other_pkg_version_hide_pushbutton.clicked.connect(lambda state, x={'second': False}: self.show_hide_panel(x))
            self.third_conf_other_pkg_version_hide_pushbutton.clicked.connect(lambda state, x={'third': False}: self.show_hide_panel(x))
            self.tms_param_hide_pushbutton.clicked.connect(lambda state, x={'tms': False}: self.show_hide_panel(x))
            self.manifest_hide_pushbutton.clicked.connect(lambda state, x={'manifest': False}: self.show_hide_panel(x))
            self.emv_kernel_ver_hide_pushbutton.clicked.connect(lambda state, x={'emv': False}: self.show_hide_panel(x))

            #show_all view
            self.show_all_menu_item.triggered.connect(lambda state, x={'jfrog':True,'jbz':True,'first':True,'second':True,'third':True,'tms': True,'manifest': True,'emv': True}: self.show_hide_panel(x))

            #Hide all panel by default, only open when required.
            self.show_hide_panel({'jfrog':False,'jbz':False,'first':False,'second':False,'third':False,'tms': False,'manifest': False,'emv': False})

            #Display the main window
            version_checker_mainwindow.show()
        except Exception as e:
            print (str(e))

    # ███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
    # ██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
    # ███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
    # ╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
    # ███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
    # ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

    def init_settings_widget(self):
        try:
            self.settings_widget = QtWidgets.QWidget()
            self.settings_ui = Ui_settings_widget()
            self.settings_ui.setupUi(self.settings_widget)
            self.settings_ui.settings_extract_path_line_edit.setFocus()
            self.restore_previous_conf()
            self.settings_ui.settings_reset_push_button.clicked.connect(self.reset_config)
            self.settings_ui.settings_save_push_button.clicked.connect(self.save_config)
        except Exception as e:
            print (str(e))

    def open_settings_widget(self):
        try:
            self.settings_widget.hide()
            self.settings_widget.show()
        except Exception as e:
            print (str(e))

    def restore_previous_conf(self):
        self.settings_ui.settings_extract_path_line_edit.setText(self.conf_base_xtrak_path)
        self.settings_ui.settings_seven_zip_line_edit.setText(self.conf_sevenZ_exe)
        self.settings_ui.settings_mnf_file_line_edit.setText(self.conf_manifest)
        self.settings_ui.settings_pkg_loc_line_edit.setText(self.conf_default_pkg_folder)
        self.settings_ui.settings_conf_emv_url_line_edit.setText(self.conf_emv_ver_url)
        self.settings_ui.settings_chrome_wd_line_edit.setText(self.conf_chrome_driver_filepath)
        self.settings_ui.settings_load_save_path_line_edit.setText(self.conf_load_path)
        self.settings_ui.settings_tms_path_line_edit.setText(self.conf_tms_path)
        self.settings_ui.settings_compare_path_line_edit.setText(self.conf_compare_path)
        self.settings_ui.settings_jfrog_path_line_edit.setText(self.conf_jfrog_path)

    def reset_config(self):
        self.restore_previous_conf()

    def config_to_json(self):
        return '{"pkg_version_cfg": [{"base_xtrak_path": "'+self.conf_base_xtrak_path+'"},{"sevenZ_exe": "'+self.conf_sevenZ_exe+'"},{"manifest_file": "'+self.conf_manifest+'"},{"default_pkg_location": "'+self.conf_default_pkg_folder+'"}],"emv_version_cfg": [{"emv_ver_url": "'+self.conf_emv_ver_url+'"},{"chrome_driver_filepath": "'+self.conf_chrome_driver_filepath+'"}],"load_cfg": [{"load_path": "'+self.conf_load_path+'"}],"tms_cfg": [{"tms_path": "'+self.conf_tms_path+'"}],"compare_cfg": [{"compare_path": "'+self.conf_compare_path+'"}],"jfrog_cfg": [{"jfrog_repo_path": "'+self.conf_jfrog_path+'"}]}'

    def save_config(self):
        self.conf_base_xtrak_path = self.settings_ui.settings_extract_path_line_edit.text()
        self.conf_sevenZ_exe = self.settings_ui.settings_seven_zip_line_edit.text()
        self.conf_manifest = self.settings_ui.settings_mnf_file_line_edit.text()
        self.conf_default_pkg_folder = self.settings_ui.settings_pkg_loc_line_edit.text()
        self.conf_emv_ver_url = self.settings_ui.settings_conf_emv_url_line_edit.text()
        self.conf_chrome_driver_filepath = self.settings_ui.settings_chrome_wd_line_edit.text()
        self.conf_load_path = self.settings_ui.settings_load_save_path_line_edit.text()
        self.conf_tms_path = self.settings_ui.settings_tms_path_line_edit.text()
        self.conf_compare_path = self.settings_ui.settings_compare_path_line_edit.text()
        self.conf_jfrog_path = self.settings_ui.settings_jfrog_path_line_edit.text()

        try:
            with open('config.json', 'w') as outfile:
                json.dump(json.loads(self.config_to_json()), outfile)
                self.dialog('Saved to config.json', 'Save')
                self.settings_widget.hide()
        except Exception as e:
            self.dialog('Error saving.', 'Save')


    #  ██████╗ ██████╗ ███╗   ███╗██████╗  █████╗ ██████╗ ███████╗
    # ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗██╔══██╗██╔════╝
    # ██║     ██║   ██║██╔████╔██║██████╔╝███████║██████╔╝█████╗
    # ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██╔══██║██╔══██╗██╔══╝
    # ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║██║  ██║███████╗
    #  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

    #After making the filter rule in MAP, this option will compare the version using the rule made

    def init_compare_widget(self):
        try:
            self.compare_widget = QtWidgets.QWidget()
            self.compare_ui = Ui_compare_widget()
            self.compare_ui.setupUi(self.compare_widget)
            self.compare_ui.compare_browse_push_button.clicked.connect(lambda state, x=self.compare_ui.compare_line_edit: self.browse_compare_rule_file(x))
            self.compare_ui.compare_push_button.clicked.connect(self.compare_the_versions)
        except Exception as e:
            print (str(e))

    def browse_compare_rule_file(self, line_edit):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file, _ = QFileDialog.getOpenFileName(None,'Open file',self.conf_compare_path,"json files (*.json))")
            if file:
                line_edit.setText(file)
        except Exception as e:
            print (str(e))

    def open_compare_widget(self):
        try:
            self.compare_widget.hide()
            self.compare_widget.show()
        except Exception as e:
            print (str(e))

    def compare_the_versions(self):
        try:
            #Load the rule
            filename = self.compare_ui.compare_line_edit.text()
            print(filename)

            with open(filename) as results_json:
                data = json.load(results_json)

                self.active_comparison_list = []
                self.active_comparison_list.append(['Name','Package','Manifest','TMS','EMV'])

                for tag in data:
                    self.active_comparison_list.append([tag['ref'],self.find_package_version(tag['pkg']), self.find_manifest_version(tag['mnf']), self.find_tms_version(tag['tms']), self.find_emv_version(tag['emv'])])

                self.populate_generic_table(self.compare_ui.compare_table, self.active_comparison_list)

        except Exception as e:
            print (str(e))

    def find_emv_version(self,tag):
        try:
            if tag == '':
                return 'NA'
            for emv_list in self.result_tms:
                if tag in emv_list[0]:
                    return emv_list[1]
            return 'NA'
        except Exception as e:
            print (str(e))

    def find_tms_version(self,tag):
        try:
            if tag == '':
                return 'NA'
            for tms_list in self.result_tms:
                if tag in tms_list[0]:
                    return tms_list[1]
            return 'NA'
        except Exception as e:
            print (str(e))

    def find_manifest_version(self,tag):
        try:
            if tag == '':
                return 'NA'
            for mnf_list in self.result_manifest:
                if tag in mnf_list[0]:
                    return mnf_list[1]
            return 'NA'
        except Exception as e:
            print (str(e))

    def search_from_all_pkg_list(self, pkg):
        try:
            for jbz_list in self.result_jbz_ref:
                if pkg in jbz_list[0]:
                    return jbz_list[2]
            for conf_other_list_1 in self.result_conf_other_1_ref:
                if pkg in conf_other_list_1[0]:
                    return conf_other_list_1[2]
            for conf_other_list_2 in self.result_conf_other_2_ref:
                if pkg in conf_other_list_2[0]:
                    return conf_other_list_2[2]
            for conf_other_list_3 in self.result_conf_other_3_ref:
                if pkg in conf_other_list_3[0]:
                    return conf_other_list_3[2]
            return 'NA'
        except Exception as e:
            print (str(e))

    def find_package_version(self,tag):
        try:
            if tag == '':
                return 'NA'
            if '|' in tag:
                each_pkg = tag.split('|')
                print(each_pkg)
                return str(self.search_from_all_pkg_list(each_pkg[0]))+'\n'+str(self.search_from_all_pkg_list(each_pkg[1]))
            else:
                return self.search_from_all_pkg_list(tag)
        except Exception as e:
            print (str(e))

    # ███╗   ███╗ █████╗ ██████╗
    # ████╗ ████║██╔══██╗██╔══██╗
    # ██╔████╔██║███████║██████╔╝
    # ██║╚██╔╝██║██╔══██║██╔═══╝
    # ██║ ╚═╝ ██║██║  ██║██║
    # ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝

    # This is to map the key name from different sources which will be used for the filter rules

    def init_map_widget(self):
        try:
            self.map_widget = QtWidgets.QWidget()
            self.map_ui = Ui_map_widget()
            self.map_ui.setupUi(self.map_widget)

            self.map_ui.map_pkg_filter_Line_edit.textChanged['QString'].connect(self.map_filter_pkg_field)
            self.map_ui.map_manifest_filter_line_edit.textChanged['QString'].connect(self.map_filter_manifest_field)
            self.map_ui.map_emv_filter_line_edit.textChanged['QString'].connect(self.map_filter_emv_field)
            self.map_ui.map_tms_filter_line_edit.textChanged['QString'].connect(self.map_filter_tms_field)

            self.map_ui.map_add_push_button.clicked.connect(self.add_to_rule_table)
            self.map_ui.map_save_push_button.clicked.connect(self.save_rule_table)
        except Exception as e:
            print (str(e))

    def open_map_widget(self):
        try:
            self.map_widget.hide()

            #Init the rule result list, selected pkg/tag will be placed here
            self.rule_result_list = []

            #Merge the packages sources to one table and color code it.
            self.map_merged_pkg_result_orig = []

            if self.result_jbz:
                for p in self.result_jbz:
                    self.map_merged_pkg_result_orig.append(['0',p[0]])

            if self.result_conf_other_1:
                for p in self.result_conf_other_1:
                    self.map_merged_pkg_result_orig.append(['1',p[0]])

            if self.result_conf_other_2:
                for p in self.result_conf_other_2:
                    self.map_merged_pkg_result_orig.append(['2',p[0]])

            if self.result_conf_other_3:
                for p in self.result_conf_other_3:
                    self.map_merged_pkg_result_orig.append(['3',p[0]])

            if self.map_merged_pkg_result_orig:
                self.map_merged_pkg_result = self.map_merged_pkg_result_orig.copy()
                self.map_merged_pkg_result.insert(0, ['#', 'Pkg'])
                self.model_map_pkg_table = self.populate_map_pkg_table(self.map_ui.map_pkg_table, self.map_merged_pkg_result)
                self.map_ui.map_pkg_table.doubleClicked.connect(self.map_stage_the_pkg_name)

            if self.result_manifest:
                self.map_manifest_result_list = self.result_manifest.copy()
                self.map_manifest_result_list.insert(0, ['TAG', 'VERSION'])
                self.model_map_manifest_table = self.populate_generic_table(self.map_ui.map_manifest_table, self.map_manifest_result_list,color_code='manifest')
                self.map_ui.map_manifest_table.doubleClicked.connect(self.map_stage_manifest)

            if self.result_tms:
                self.map_tms_result_list = self.result_tms.copy()
                self.map_tms_result_list.insert(0, ['TAG', 'VALUE'])
                self.model_map_tms_table = self.populate_generic_table(self.map_ui.map_tms_table, self.map_tms_result_list,color_code='tms')
                self.map_ui.map_tms_table.doubleClicked.connect(self.map_stage_tms)

            if self.result_emv:
                self.map_emv_result_list = self.result_emv.copy()
                self.map_emv_result_list.insert(0,["TAG", "VERSION"])
                self.model_map_emv_table = self.populate_generic_table(self.map_ui.map_emv_table, self.map_emv_result_list,color_code='emv')
                self.map_ui.map_emv_table.doubleClicked.connect(self.map_stage_emv)

            self.map_widget.show()
        except Exception as e:
            print (str(e))

    def save_rule_table(self):
        try:
            if self.rule_result_list:
                filename = self.map_ui.map_rule_name_line_edit.text()
                if filename != '':
                    with open(filename + '.json', 'w') as outfile:
                        json.dump(json.loads(self.rule_result_to_json_string()), outfile)
        except Exception as e:
            print (str(e))

    #Convert the rule results to json string
    def rule_result_to_json_string(self):
        try:
            #open json array
            result_json_string = "["
            for rl in self.rule_result_list:
                result_json_string = result_json_string + '{"ref":"'+rl[0]+'","pkg":"'+rl[1]+'","mnf":"'+rl[2]+'","tms":"'+rl[3]+'","emv":"'+rl[4]+'"},'
            result_json_string = result_json_string[:-1]
            #close json array
            result_json_string = result_json_string + ']'
            return result_json_string
        except Exception as e:
            print (str(e))

    def add_to_rule_table(self):
        try:
            ref_text = self.map_ui.map_reference_line_edit.text()
            if self.map_ui.map_reference_line_edit.text() == '':
                return

            pkg_text = self.map_ui.map_pkg_ver_line_edit.text()
            mnf_text = self.map_ui.map_manifest_line_edit.text()
            tms_text = self.map_ui.map_tms_line_edit.text()
            emv_text = self.map_ui.map_emv_line_edit.text()
            single_line_rule_result_list = [ref_text, pkg_text, mnf_text, tms_text, emv_text]

            #Add to rule table
            self.rule_result_list.append(single_line_rule_result_list)
            self.rule_result_list.insert(0, ['Name', 'Package', 'Manifest', 'TMS', 'EMV'])
            self.populate_generic_table(self.map_ui.map_rule_table, self.rule_result_list)

            #Clear the stage line edit
            self.map_ui.map_reference_line_edit.setText('')
            self.map_ui.map_pkg_ver_line_edit.setText('')
            self.map_ui.map_manifest_line_edit.setText('')
            self.map_ui.map_tms_line_edit.setText('')
            self.map_ui.map_emv_line_edit.setText('')

        except Exception as e:
            print (str(e))

    #Filters the list in every character entered in the filter field
    def common_map_filter_field(self, is_pkg, orig_result_list,line_edit, header_list, table):
        try:
            result_list = [tag for tag in orig_result_list if tag[1 if is_pkg else 0].lower().find(line_edit.text().lower()) != -1]
            result_list.insert(0, header_list)
            if is_pkg:
                model = self.populate_map_pkg_table(table, result_list)
            else:
                model = self.populate_generic_table(table, result_list)
            return result_list, model
        except Exception as e:
            print (str(e))

    def map_filter_pkg_field(self):
        try:
            self.map_merged_pkg_result, self.model_map_pkg_table = self.common_map_filter_field(True, self.map_merged_pkg_result_orig, self.map_ui.map_pkg_filter_Line_edit, ['#', 'Pkg'], self.map_ui.map_pkg_table)
        except Exception as e:
            print (str(e))

    def map_filter_manifest_field(self):
        try:
            self.map_manifest_result_list, self.model_map_manifest_table = self.common_map_filter_field(False, self.result_manifest, self.map_ui.map_manifest_filter_line_edit, ['TAG', 'VERSION'], self.map_ui.map_manifest_table)
        except Exception as e:
            print (str(e))

    def map_filter_emv_field(self):
        try:
            self.map_emv_result_list, self.model_map_emv_table = self.common_map_filter_field(False, self.result_emv, self.map_ui.map_emv_filter_line_edit, ["TAG", "VERSION"], self.map_ui.map_emv_table)
        except Exception as e:
            print (str(e))

    def map_filter_tms_field(self):
        try:
            self.map_tms_result_list, self.model_map_tms_table = self.common_map_filter_field(False, self.result_tms, self.map_ui.map_tms_filter_line_edit, ['TAG', 'VALUE'], self.map_ui.map_tms_table)
        except Exception as e:
            print (str(e))

    #return the package name only from the package file name + version + KVC.
    def parse_package_name(self, p):
        try:
            return "_".join(p.split('_')[:-2])
        except Exception as e:
            print (str(e))

    def common_map_stage(self,signal,col,model,line_edit,pn):
        try:
            row = signal.row()
            index = signal.sibling(row, col) # col is the name column
            index_dict = model.itemData(index)
            index_value = index_dict.get(0)
            t = line_edit.text()
            delimeter = '' if t == '' else '|'
            if pn: #parse name or not
                line_edit.setText(self.parse_package_name(index_value)+delimeter+t)
            else:
                line_edit.setText(index_value+delimeter+t)
        except Exception as e:
            print (str(e))

    #Double clicking the table will put it in the staging field, ready to commit to the table below.
    def map_stage_the_pkg_name(self, signal):
        try:
            self.common_map_stage(signal,1,self.model_map_pkg_table,self.map_ui.map_pkg_ver_line_edit,True)
        except Exception as e:
            print (str(e))

    def map_stage_manifest(self, signal):
        try:
            self.common_map_stage(signal,0,self.model_map_manifest_table,self.map_ui.map_manifest_line_edit,False)
        except Exception as e:
            print (str(e))

    def map_stage_tms(self, signal):
        try:
            self.common_map_stage(signal,0,self.model_map_tms_table,self.map_ui.map_tms_line_edit,False)
        except Exception as e:
            print (str(e))

    def map_stage_emv(self, signal):
        try:
            self.common_map_stage(signal,0,self.model_map_emv_table,self.map_ui.map_emv_line_edit,False)
        except Exception as e:
            print (str(e))

    # ██╗      ██████╗  █████╗ ██████╗
    # ██║     ██╔═══██╗██╔══██╗██╔══██╗
    # ██║     ██║   ██║███████║██║  ██║
    # ██║     ██║   ██║██╔══██║██║  ██║
    # ███████╗╚██████╔╝██║  ██║██████╔╝
    # ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝

    def init_load_widget(self):
        try:
            self.load_to_screen_widget = QtWidgets.QWidget()
            self.load_to_screen_ui = Ui_load_widget()
            self.load_to_screen_ui.setupUi(self.load_to_screen_widget)
            self.load_to_screen_ui.load_browse_filename_push_button.clicked.connect(lambda state, x=self.load_to_screen_ui.load_filename_line_edit: self.browse_filename_to_load(x))
            self.load_to_screen_ui.load_load_push_button.clicked.connect(self.load_display_to_screen)
        except Exception as e:
            print (str(e))

    def open_load_widget(self):
        try:
            self.load_to_screen_widget.hide()
            self.load_to_screen_widget.show()
        except Exception as e:
            print (str(e))

    def browse_filename_to_load(self, line_edit):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file, _ = QFileDialog.getOpenFileName(None,'Open file',self.conf_load_path,"json files (*.json))")

            #file = str(QFileDialog.getExistingDirectory())
            if file:
                line_edit.setText(file)
        except Exception as e:
            print (str(e))

    def load_display_to_screen(self):
        try:
            #Initialize the result list
            self.result_jbz = None
            self.result_conf_other_1 = None
            self.result_conf_other_2 = None
            self.result_conf_other_3 = None
            self.result_manifest = None
            self.result_emv = None
            self.result_tms = None

            #Hide the panels
            self.show_hide_panel({'jbz': False})
            self.show_hide_panel({'first': False})
            self.show_hide_panel({'second': False})
            self.show_hide_panel({'third': False})
            self.show_hide_panel({'manifest': False})
            self.show_hide_panel({'tms': False})
            self.show_hide_panel({'emv': False})

            filename = self.load_to_screen_ui.load_filename_line_edit.text()
            with open(filename) as results_json:
                data = json.load(results_json)

                #Retrieve content from jbz dictionary and assign to jbz result list
                self.result_jbz, self.result_jbz_ref = self.results_json_to_list(data, 'jbz', ['PACKAGE', 'PKG VER'], False)

                #Retrieve content from conf others 1 dictionary and assign to conf others 1 result list
                self.result_conf_other_1, self.result_conf_other_1_ref = self.results_json_to_list(data, 'conf_other_1', ['PACKAGE', 'PKG VER'], False)

                #Retrieve content from conf others 2 dictionary and assign to conf others 2 result list
                self.result_conf_other_2, self.result_conf_other_2_ref = self.results_json_to_list(data, 'conf_other_2', ['PACKAGE', 'PKG VER'], False)

                #Retrieve content from conf others 3 dictionary and assign to conf others 3 result list
                self.result_conf_other_3, self.result_conf_other_3_ref = self.results_json_to_list(data, 'conf_other_3', ['PACKAGE', 'PKG VER'], False)

                #Retrieve content from manifest dictionary and assign to manifest result list
                self.result_manifest = self.results_json_to_list(data, 'manifest', ['TAG', 'VERSION'], True)

                #Retrieve content from tms dictionary and assign to tms result list
                self.result_tms = self.results_json_to_list(data, 'tms', ['TAG','VALUE'], True)

                #Retrieve content from emv dictionary and assign to emv result list
                self.result_emv = self.results_json_to_list(data, 'emv', ["TAG", "VERSION"], True)

                #Populate the tables from the loaded list
                if self.result_jbz:
                    self.job_bundle_pkg_ver_label.setText("Package Version")
                    #Disconnect any signals attached to table.
                    try:
                        self.jbz_pkg_ver_table.disconnect()
                    except Exception as e:
                        print(str(e))
                    self.populate_generic_table(self.jbz_pkg_ver_table, self.result_jbz, color_code='jbz')
                    self.show_hide_panel({'jbz':True})
                    self.pkg_listview.hide()

                if self.result_conf_other_1:
                    self.first_conf_other_pkg_ver_label.setText("1st Conf and Other Version")
                    #Disconnect any signals attached to table.
                    try:
                        self.first_conf_other_pkg_ver_table.disconnect()
                    except Exception as e:
                        print(str(e))
                    self.populate_generic_table(self.first_conf_other_pkg_ver_table, self.result_conf_other_1, color_code='conf_other_1')
                    self.show_hide_panel({'first':True})
                    self.first_conf_other_pkg_listview.hide()

                if self.result_conf_other_2:
                    self.second_conf_other_pkg_ver_label.setText("2nd Conf and Other Version")
                    #Disconnect any signals attached to table.
                    try:
                        self.second_conf_other_pkg_ver_table.disconnect()
                    except Exception as e:
                        print(str(e))
                    self.populate_generic_table(self.second_conf_other_pkg_ver_table, self.result_conf_other_2, color_code='conf_other_2')
                    self.show_hide_panel({'second':True})
                    self.second_conf_other_pkg_listview.hide()

                if self.result_conf_other_3:
                    self.third_conf_other_pkg_ver_label.setText("3rd Conf and Other Version")
                    #Disconnect any signals attached to table.
                    try:
                        self.third_conf_other_pkg_ver_table.disconnect()
                    except Exception as e:
                        print(str(e))
                    self.populate_generic_table(self.third_conf_other_pkg_ver_table, self.result_conf_other_3, color_code='conf_other_3')
                    self.show_hide_panel({'third':True})
                    self.third_conf_other_pkg_listview.hide()

                if self.result_manifest:
                    self.populate_generic_table(self.manifest_table, self.result_manifest, color_code='manifest')
                    self.show_hide_panel({'manifest': True})

                if self.result_tms:
                    self.populate_generic_table(self.tms_param_table, self.result_tms, color_code='tms')
                    self.show_hide_panel({'tms': True})

                if self.result_emv:
                    self.populate_generic_table(self.emv_kernel_ver_table, self.result_emv, color_code='emv')
                    self.show_hide_panel({'emv': True})

            self.load_to_screen_widget.hide()
        except Exception as e:
            print (str(e))

    def results_json_to_list(self, data, key, header, single_val):
        try:
            # The list that is displayed on the screen.
            temp_result_list = []
            # The list that contains more information, this is used in packages that has version but it is not display, only package name and pkg version (v1/v255) is displayed.
            temp_ref_result_list = []
            temp_result_list.append(header)
            for result in data[key]:
                for k, v in result.items():
                    if single_val:
                        temp_result_list.append([k, v])
                    else:
                        temp_result_list.append([k, v[0]])
                        temp_ref_result_list.append([k, v[0], v[1]])
            if single_val:
                return temp_result_list
            else:
                return temp_result_list, temp_ref_result_list
        except Exception as e:
            print(str(e))

    # ███████╗ █████╗ ██╗   ██╗███████╗
    # ██╔════╝██╔══██╗██║   ██║██╔════╝
    # ███████╗███████║██║   ██║█████╗
    # ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝
    # ███████║██║  ██║ ╚████╔╝ ███████╗
    # ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝

    def init_save_widget(self):
        try:
            self.save_on_screen_widget = QtWidgets.QWidget()
            self.save_on_screen_ui = Ui_save_widget()
            self.save_on_screen_ui.setupUi(self.save_on_screen_widget)
            self.save_on_screen_ui.save_save_button.clicked.connect(self.save_on_screen_to_json)
        except Exception as e:
            print (str(e))

    def open_save_widget(self):

        try:
            self.save_on_screen_ui.save_filename_line_edit.setText('')
            self.save_on_screen_widget.hide()
            self.save_on_screen_widget.show()
        except Exception as e:
            print (str(e))

    #common jsonify pattern
    def common_jsonify_of_result_list(self,result_json_string,source,result_ref):
        try:
            result_json_string = result_json_string +'"'+source+'":['
            for rl in result_ref:
                result_json_string = result_json_string + '{"'+rl[0]+'":"'+rl[1]+'"},'
            result_json_string = result_json_string[:-1]
            result_json_string = result_json_string + '],'
            return result_json_string
        except Exception as e:
            print (str(e))

    def common_jsonify_of_result_list_with_header_info(self,result_json_string,source,result_ref):
        try:
            result_json_string = result_json_string +'"'+source+'":['
            for rl in result_ref:
                result_json_string = result_json_string + '{"'+rl[0]+'":["'+rl[1]+'","'+rl[2]+'"]},'
            result_json_string = result_json_string[:-1]
            result_json_string = result_json_string + '],'
            return result_json_string
        except Exception as e:
            print (str(e))

    #Convert the results to json string
    def results_to_json(self):
        try:
            #Outer bracket
            result_json_string = "{"

            #JBZ
            if self.result_jbz_ref is not None:
                result_json_string = self.common_jsonify_of_result_list_with_header_info(result_json_string, 'jbz', self.result_jbz_ref)

            #CONF OR OTHER 1
            if self.result_conf_other_1_ref is not None:
                result_json_string = self.common_jsonify_of_result_list_with_header_info(result_json_string,'conf_other_1',self.result_conf_other_1_ref)

            #CONF OR OTHER 2
            if self.result_conf_other_2_ref is not None:
                result_json_string = self.common_jsonify_of_result_list_with_header_info(result_json_string, 'conf_other_2', self.result_conf_other_2_ref)

            #CONF OR OTHER 3
            if self.result_conf_other_3_ref is not None:
                result_json_string = self.common_jsonify_of_result_list_with_header_info(result_json_string, 'conf_other_3', self.result_conf_other_3_ref)

            #MANIFEST
            if self.result_manifest is not None:
                result_json_string = self.common_jsonify_of_result_list(result_json_string, 'manifest', self.result_manifest)

            #EMV
            if self.result_emv is not None:
                result_json_string = self.common_jsonify_of_result_list(result_json_string, 'emv', self.result_emv)

            #TMS
            if self.result_tms is not None:
                result_json_string = self.common_jsonify_of_result_list(result_json_string, 'tms', self.result_tms)

            result_json_string = result_json_string[:-1]
            result_json_string = result_json_string+"}"

            return result_json_string
        except Exception as e:
            print (str(e))

    def save_on_screen_to_json(self):
        try:
            filename = self.save_on_screen_ui.save_filename_line_edit.text()
            if filename != '':
                #The path to save is same as the path to load.
                with open(self.conf_load_path+filename+'.json', 'w') as outfile:
                    json.dump(json.loads(self.results_to_json()), outfile)
                    self.dialog('Saved to ' + self.conf_load_path + filename, 'Save')
                    self.save_on_screen_widget.hide()
            else:
                self.dialog('Cannot save without file name.' + filename, 'Save')
        except Exception as e:
            self.dialog('Error saving.', 'Save')
            #Remove the faulty file created
            if os.path.exists(self.conf_load_path+filename+'.json'):
                os.remove(self.conf_load_path+filename+'.json')
            self.save_on_screen_widget.hide()
            print (str(e))

    # ██████╗  █████╗  ██████╗██╗  ██╗ █████╗  ██████╗ ███████╗    ██╗   ██╗███████╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗
    # ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝    ██║   ██║██╔════╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║
    # ██████╔╝███████║██║     █████╔╝ ███████║██║  ███╗█████╗      ██║   ██║█████╗  ██████╔╝███████╗██║██║   ██║██╔██╗ ██║
    # ██╔═══╝ ██╔══██║██║     ██╔═██╗ ██╔══██║██║   ██║██╔══╝      ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║██║   ██║██║╚██╗██║
    # ██║     ██║  ██║╚██████╗██║  ██╗██║  ██║╚██████╔╝███████╗     ╚████╔╝ ███████╗██║  ██║███████║██║╚██████╔╝██║ ╚████║
    # ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝

    def init_pkg_widget(self):
        try:
            self.pkg_widget = QtWidgets.QWidget()
            self.pkg_ui = Ui_pkg_widget()
            self.pkg_ui.setupUi(self.pkg_widget)
            self.pkg_ui.jbz_path_push_button.clicked.connect(self.search_jbz_path)
            self.pkg_ui.extract_push_button.clicked.connect(self.extract_jbz_and_other_pkg)
            self.pkg_ui.conf_other_pkg_1_push_button.clicked.connect(self.search_other_pkg_path_1)
            self.pkg_ui.conf_other_pkg_2_push_button.clicked.connect(self.search_other_pkg_path_2)
            self.pkg_ui.conf_other_pkg_3_push_button.clicked.connect(self.search_other_pkg_path_3)
        except Exception as e:
            print (str(e))

    def open_pkg_widget(self):
        try:
            self.pkg_ui.jbz_path_line_edit.setFocus()
            self.pkg_ui.jbz_path_line_edit.setText('')
            self.pkg_ui.conf_other_pkg_1_line_edit.setText('')
            self.pkg_ui.conf_other_pkg_2_line_edit.setText('')
            self.pkg_ui.conf_other_pkg_3_line_edit.setText('')
            self.pkg_widget.hide()
            self.pkg_widget.show()
        except Exception as e:
            print (str(e))

    def open_file_dialog(self,line_edit):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file, _ = QFileDialog.getOpenFileName(None,caption='Open file',directory=self.conf_default_pkg_folder)

            if file:
                line_edit.setText(file)
        except Exception as e:
            print (str(e))

    def search_jbz_path(self):
        try:
            self.open_file_dialog(self.pkg_ui.jbz_path_line_edit)
        except Exception as e:
            print (str(e))

    def search_other_pkg_path_1(self):
        try:
            self.open_file_dialog(self.pkg_ui.conf_other_pkg_1_line_edit)
        except Exception as e:
            print (str(e))

    def search_other_pkg_path_2(self):
        try:
            self.open_file_dialog(self.pkg_ui.conf_other_pkg_2_line_edit)
        except Exception as e:
            print (str(e))

    def search_other_pkg_path_3(self):
        try:
            self.open_file_dialog(self.pkg_ui.conf_other_pkg_3_line_edit)
        except Exception as e:
            print (str(e))

    def extract_jbz_and_other_pkg(self):
        try:
            self.jbx = JobBundleExtraction()

            #Initialize from configuration
            self.jbx.base_xtrak_path = self.conf_base_xtrak_path
            self.jbx.sevenZ_exe = self.conf_sevenZ_exe
            self.jbx.manifest_file = self.conf_manifest

            # The guide to list holding the information from different sources. (i.e. packages, tms, emv kernel, manifest)
            # PACKAGE LIST
            # *** jbz ***
            # self.result_jbz - the view list for job bundle table
            # self.result_manifest - the view list for manifest table
            # self.result_jbz_ref - the reference list when saving job bundle.
            # *** tgz #1 ***
            # self.result_conf_other_1 - the view list for zipped packages from any tgz (e.g. conf)
            # self.result_conf_other_1_ref - the reference list when saving tgz #1
            # *** tgz #2 ***
            # self.result_conf_other_2 - the view list for zipped packages from any tgz (e.g. others)
            # self.result_conf_other_2_ref - the reference list when saving tgz #2
            # *** tgz #3 ***
            # self.result_conf_other_3 - the view list for zipped packages from any tgz (e.g. factory)
            # self.result_conf_other_3_ref - the reference list when saving tgz #3

            #Do extraction if there is an entry from the line edit field.
            if self.pkg_ui.jbz_path_line_edit.text() != "":
                self.result_jbz,self.result_manifest,self.result_jbz_ref = self.jbx.extract(tag=0,jbz_file=self.pkg_ui.jbz_path_line_edit.text())
                if self.result_jbz:
                    self.show_hide_panel({'jbz':True})
                    self.pkg_listview.hide()
                if self.result_manifest:
                    self.show_hide_panel({'manifest': True})

            if self.pkg_ui.conf_other_pkg_1_line_edit.text() != "":
                self.result_conf_other_1,_,self.result_conf_other_1_ref = self.jbx.extract(tag=1,jbz_file=self.pkg_ui.conf_other_pkg_1_line_edit.text())
                if self.result_conf_other_1:
                    self.show_hide_panel({'first':True})
                    self.first_conf_other_pkg_listview.hide()

            if self.pkg_ui.conf_other_pkg_2_line_edit.text() != "":
                self.result_conf_other_2,_,self.result_conf_other_2_ref = self.jbx.extract(tag=2,jbz_file=self.pkg_ui.conf_other_pkg_2_line_edit.text())
                if self.result_conf_other_2:
                    self.show_hide_panel({'second': True})
                    self.second_conf_other_pkg_listview.hide()

            if self.pkg_ui.conf_other_pkg_3_line_edit.text() != "":
                self.result_conf_other_3,_,self.result_conf_other_3_ref = self.jbx.extract(tag=3,jbz_file=self.pkg_ui.conf_other_pkg_3_line_edit.text())
                if self.result_conf_other_3:
                    self.show_hide_panel({'third': True})
                    self.third_conf_other_pkg_listview.hide()

            self.pkg_widget.hide()

            #Display the result from extraction
            if self.result_jbz:
                self.populate_jb_table(self.result_jbz)
                self.job_bundle_pkg_ver_label.setText("..."+self.pkg_ui.jbz_path_line_edit.text()[-40:])
            if self.result_conf_other_1:
                self.populate_first_conf_table(self.result_conf_other_1)
                self.first_conf_other_pkg_ver_label.setText("..."+self.pkg_ui.conf_other_pkg_1_line_edit.text()[-40:])
            if self.result_conf_other_2:
                self.populate_second_conf_table(self.result_conf_other_2)
                self.second_conf_other_pkg_ver_label.setText("..."+self.pkg_ui.conf_other_pkg_2_line_edit.text()[-40:])
            if self.result_conf_other_3:
                self.populate_third_conf_table(self.result_conf_other_3)
                self.third_conf_other_pkg_ver_label.setText("..."+self.pkg_ui.conf_other_pkg_3_line_edit.text()[-40:])
            if self.result_manifest:
                self.populate_manifest_table(self.result_manifest)
        except Exception as e:
            print (str(e))

    def populate_jb_table(self,result):
        try:
            self.model_jbz_pkg_ver_table = self.populate_generic_table(self.jbz_pkg_ver_table,result,color_code='jbz',hide_col=2)
            self.jbz_pkg_ver_table.clicked.connect(self.jbz_package_info)
        except Exception as e:
            print (str(e))

    def populate_first_conf_table(self,result):
        try:
            self.model_first_conf_ver_table = self.populate_generic_table(self.first_conf_other_pkg_ver_table,result,color_code='conf_other_1',hide_col=2)
            self.first_conf_other_pkg_ver_table.clicked.connect(self.first_conf_package_info)
        except Exception as e:
            print (str(e))

    def populate_second_conf_table(self,result):
        try:
            self.model_second_conf_ver_table = self.populate_generic_table(self.second_conf_other_pkg_ver_table,result,color_code='conf_other_2',hide_col=2)
            self.second_conf_other_pkg_ver_table.clicked.connect(self.second_conf_package_info)
        except Exception as e:
            print (str(e))

    def populate_third_conf_table(self,result):
        try:
            self.model_third_conf_ver_table = self.populate_generic_table(self.third_conf_other_pkg_ver_table,result,color_code='conf_other_3',hide_col=2)
            self.third_conf_other_pkg_ver_table.clicked.connect(self.third_conf_package_info)
        except Exception as e:
            print (str(e))

    def populate_manifest_table(self,result):
        try:
            self.model_manifest_table = self.populate_generic_table(self.manifest_table,result,color_code='manifest')
        except Exception as e:
            print (str(e))

    #This is called by package info functions to display the header information
    def common_package_info_table_setter(self,signal,model,list_model,list_view, folder_index):
        try:
            row = signal.row()
            column = 2 # column 2 has the path to the package.
            index = signal.sibling(row, column)
            index_dict = model.itemData(index)
            pkg_header_string = str(package.header_info(index_dict.get(0)))

            list_model.clear()

            for h in pkg_header_string.splitlines():
                list_model.appendRow(QStandardItem(h))

            # Apply the model to the list view
            list_view.setModel(list_model)
        except Exception as e:
            print (str(e))

    def jbz_package_info(self, signal):
        try:
            self.pkg_listview.show()
            self.common_package_info_table_setter(signal, self.model_jbz_pkg_ver_table, self.pkg_header_list_model, self.pkg_listview, 0)
        except Exception as e:
            print (str(e))

    def first_conf_package_info(self,signal):
        try:
            self.first_conf_other_pkg_listview.show()
            self.common_package_info_table_setter(signal, self.model_first_conf_ver_table, self.first_conf_other_pkg_header_list_model, self.first_conf_other_pkg_listview,1)
        except Exception as e:
            print (str(e))

    def second_conf_package_info(self,signal):
        try:
            self.second_conf_other_pkg_listview.show()
            self.common_package_info_table_setter(signal, self.model_second_conf_ver_table, self.second_conf_other_pkg_header_list_model, self.second_conf_other_pkg_listview,2)
        except Exception as e:
            print (str(e))

    def third_conf_package_info(self,signal):
        try:
            self.third_conf_other_pkg_listview.show()
            self.common_package_info_table_setter(signal, self.model_third_conf_ver_table, self.third_conf_other_pkg_header_list_model, self.third_conf_other_pkg_listview, 3)
        except Exception as e:
            print (str(e))

    # ███████╗███╗   ███╗██╗   ██╗    ██╗  ██╗███████╗██████╗ ███╗   ██╗███████╗██╗         ██╗   ██╗███████╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗
    # ██╔════╝████╗ ████║██║   ██║    ██║ ██╔╝██╔════╝██╔══██╗████╗  ██║██╔════╝██║         ██║   ██║██╔════╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║
    # █████╗  ██╔████╔██║██║   ██║    █████╔╝ █████╗  ██████╔╝██╔██╗ ██║█████╗  ██║         ██║   ██║█████╗  ██████╔╝███████╗██║██║   ██║██╔██╗ ██║
    # ██╔══╝  ██║╚██╔╝██║╚██╗ ██╔╝    ██╔═██╗ ██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝  ██║         ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║██║   ██║██║╚██╗██║
    # ███████╗██║ ╚═╝ ██║ ╚████╔╝     ██║  ██╗███████╗██║  ██║██║ ╚████║███████╗███████╗     ╚████╔╝ ███████╗██║  ██║███████║██║╚██████╔╝██║ ╚████║
    # ╚══════╝╚═╝     ╚═╝  ╚═══╝      ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝

    def init_emv_widget(self):
        try:
            self.emv_widget = QtWidgets.QWidget()
            self.emv_ui = Ui_emv_widget()
            self.emv_ui.setupUi(self.emv_widget)
            self.emv_ui.extractEMVPushButton.clicked.connect(self.extract_emv)
            self.device_customer_list = ["G6-300","G7-100 NCR","G7-100 Canada","G6-200"]
            self.emv_ui.emv_device_comboBox.addItems(self.device_customer_list)
        except Exception as e:
            print (str(e))

    def open_emv_widget(self):
        try:
            emvx = EmvExtraction()
            self.emv_ui.emv_ver_url_lineedit.setText(self.conf_emv_ver_url)
            self.emv_ui.chrome_driver_lineEdit.setText(self.conf_chrome_driver_filepath)
            self.emv_widget.hide()
            self.emv_widget.show()
        except Exception as e:
            print (str(e))

    def extract_emv(self):
        try:
            if self.emv_ui.usernameLineEdit.text() == '' or self.emv_ui.passwordLineEdit.text() == '':
                return

            #login to confluence and get EMV version
            emvx = EmvExtraction()

            emvx.emv_ver_url = self.conf_emv_ver_url
            emvx.chrome_driver_filepath = self.conf_chrome_driver_filepath

            index = self.emv_ui.emv_device_comboBox.currentIndex()
            dc = self.device_customer_list[index].split(' ')
            if len(dc) == 1:
                selected_device = dc[0]
                selected_customer = "ALL"
            else:
                selected_device = dc[0]
                selected_customer = dc[1]
            self.result_emv = emvx.login(self.emv_ui.usernameLineEdit.text(),self.emv_ui.passwordLineEdit.text(),selected_device,selected_customer)
            self.populate_generic_table(self.emv_kernel_ver_table,self.result_emv, color_code='emv')
            self.show_hide_panel({'emv': True})
            self.emv_widget.hide()
        except Exception as e:
            print (str(e))

    # ████████╗███╗   ███╗███████╗██╗     ██╗████████╗███████╗    ██████╗  █████╗ ██████╗  █████╗ ███╗   ███╗███████╗████████╗███████╗██████╗ ███████╗
    # ╚══██╔══╝████╗ ████║██╔════╝██║     ██║╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝
    #    ██║   ██╔████╔██║███████╗██║     ██║   ██║   █████╗      ██████╔╝███████║██████╔╝███████║██╔████╔██║█████╗     ██║   █████╗  ██████╔╝███████╗
    #    ██║   ██║╚██╔╝██║╚════██║██║     ██║   ██║   ██╔══╝      ██╔═══╝ ██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝     ██║   ██╔══╝  ██╔══██╗╚════██║
    #    ██║   ██║ ╚═╝ ██║███████║███████╗██║   ██║   ███████╗    ██║     ██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║███████╗   ██║   ███████╗██║  ██║███████║
    #    ╚═╝   ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝

    def init_tms_widget(self):
        try:
            self.tms_widget = QtWidgets.QWidget()
            self.tms_ui = Ui_tms_widget()
            self.tms_ui.setupUi(self.tms_widget)
            self.tms_ui.tms_param_search_push_button.clicked.connect(self.search_tms_params_csv)
            self.tms_ui.tms_param_load_push_button.clicked.connect(self.load_tms)
        except Exception as e:
            print (str(e))

    def open_tms_widget(self):
        try:
            self.tms_widget.hide()
            self.tms_widget.show()
        except Exception as e:
            print (str(e))

    def load_tms(self):
        try:
            tmsx = TmsExtraction()
            self.result_tms = tmsx.load_tms_parameters(self.tms_ui.tmslite_param_line_edit.text())
            self.tms_widget.hide()
            self.populate_generic_table(self.tms_param_table,self.result_tms, color_code='tms')
            self.show_hide_panel({'tms': True})
        except Exception as e:
            print (str(e))

    def search_tms_params_csv(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file, _ = QFileDialog.getOpenFileName(None,'Open file',self.conf_tms_path,"csv files (*.csv))")

            #file = str(QFileDialog.getExistingDirectory())
            if file:
                self.tms_ui.tmslite_param_line_edit.setText(file)
        except Exception as e:
            print (str(e))

     #       ██╗███████╗██████╗  ██████╗  ██████╗      █████╗ ██████╗ ████████╗██╗███████╗ █████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
     #       ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝     ██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
     #       ██║█████╗  ██████╔╝██║   ██║██║  ███╗    ███████║██████╔╝   ██║   ██║█████╗  ███████║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝
     #  ██   ██║██╔══╝  ██╔══██╗██║   ██║██║   ██║    ██╔══██║██╔══██╗   ██║   ██║██╔══╝  ██╔══██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝
     #  ╚█████╔╝██║     ██║  ██║╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║   ██║   ██║██║     ██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║
     #   ╚════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝

    def init_jfrog_widget(self):
        try:
            self.jfrog_widget = QtWidgets.QWidget()
            self.jfrog_ui = Ui_jfrog_widget()
            self.jfrog_ui.setupUi(self.jfrog_widget)
            #Jfrog Artifactory Signals
            self.jfrog_ui.jfrog_main_push_button.clicked.connect(self.copy_selected_build_to_main)
            self.jfrog_ui.jfrog_version_combo_box.activated.connect(self.filter_jfrog_result)
            self.jfrog_ui.jfrog_filter_push_button.clicked.connect(self.filter_jfrog_result)
        except Exception as e:
            print (str(e))

    def open_jfrog_widget(self):
        try:
            self.jfrog_art_object = JfrogArtifactory(self.conf_jfrog_path)
            self.jfrog_ui.jfrog_version_combo_box.clear()
            ubn = self.jfrog_art_object.unique_build_number()
            if ubn:
                ubn.sort()
                self.jfrog_ui.jfrog_version_combo_box.addItems(ubn)
                self.jfrog_widget.hide()
                self.jfrog_widget.show()
            else:
                self.dialog("Unable to retrieve list of build versions!", "Build Number")
        except Exception as e:
            print (str(e))

    def jfrog_check_box_state_of_column(self):
        return {'type': not self.jfrog_ui.jfrog_type_check_box.isChecked(),
                'size': not self.jfrog_ui.jfrog_size_check_box.isChecked(),
                'created': not self.jfrog_ui.jfrog_created_check_box.isChecked(),
                'modified': not self.jfrog_ui.jfrog_modified_check_box.isChecked(),
                'sha1': not self.jfrog_ui.jfrog_sha1_check_box.isChecked(),
                'md5': not self.jfrog_ui.jfrog_md5_check_box.isChecked(),
                'props': not self.jfrog_ui.jfrog_props_check_box.isChecked()}

    def copy_selected_build_to_main(self):
        try:
            if self.result_of_jfrog_list:
                self.populate_jfrog_table(self.jfrog_table,self.result_of_jfrog_list,self.jfrog_check_box_state_of_column())
                self.jfrog_widget.hide()
                self.show_hide_panel({'jfrog': True})
        except Exception as e:
            print (str(e))

    def filter_jfrog_result(self):
        try:
            self.result_of_jfrog_list = self.jfrog_art_object.filter_artifact(self.jfrog_ui.jfrog_version_combo_box.currentText())
            self.populate_jfrog_table(self.jfrog_ui.jfrog_all_tableview,self.result_of_jfrog_list,self.jfrog_check_box_state_of_column())
        except Exception as e:
            print (str(e))

    def populate_jfrog_table(self, table, result_orig, col_vis):
        try:
            result = result_orig.copy()
            header = result.pop(0)
            rn = [str(c+1) for c in range(0,len(result))]
            data = pd.DataFrame(result, columns=header,index=rn)
            model = TableModel(data)
            table.setModel(model)
            table.setSelectionBehavior(QAbstractItemView.SelectRows)
            table.resizeColumnsToContents()
            #Hide or unhide column
            for key, value in col_vis.items():
                if key == 'type':
                    table.setColumnHidden(1, value)
                if key == 'size':
                    table.setColumnHidden(2, value)
                if key == 'created':
                    table.setColumnHidden(3, value)
                if key == 'modified':
                    table.setColumnHidden(4, value)
                if key == 'sha1':
                    table.setColumnHidden(5, value)
                if key == 'md5':
                    table.setColumnHidden(6, value)
                if key == 'props':
                    table.setColumnHidden(7, value)
        except Exception as e:
            print (str(e))

    # ███████╗██╗  ██╗ █████╗ ██████╗ ███████╗██████╗     ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
    # ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
    # ███████╗███████║███████║██████╔╝█████╗  ██║  ██║    █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
    # ╚════██║██╔══██║██╔══██║██╔══██╗██╔══╝  ██║  ██║    ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║
    # ███████║██║  ██║██║  ██║██║  ██║███████╗██████╔╝    ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
    # ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

    def dialog(self, message, title):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText(message)
        infoBox.setWindowTitle(title)
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()

    #Hide panel
    def show_hide_panel(self, hs_dict):
        try:
            splash_flag = False
            for key, value in hs_dict.items():
                if key == 'jfrog':
                    if value:
                        #show jfrog
                        self.jfrog_buttom_button_frame.show()
                        self.jfrog_table.show()
                        self.jfrog_label.show()
                        splash_flag = True
                    else:
                        #hide jfrog
                        self.jfrog_buttom_button_frame.hide()
                        self.jfrog_table.hide()
                        self.jfrog_label.hide()
                if key == 'jbz':
                     if value:
                         #show jbz
                         self.jbz_pkg_ver_buttom_button_frame.show()
                         self.jbz_pkg_ver_table.show()
                         self.job_bundle_pkg_ver_label.show()
                         self.pkg_listview.show()
                         splash_flag = True
                     else:
                         #hide jbz
                         self.jbz_pkg_ver_buttom_button_frame.hide()
                         self.jbz_pkg_ver_table.hide()
                         self.job_bundle_pkg_ver_label.hide()
                         self.pkg_listview.hide()

                if key == 'first':
                     if value:
                         #show first conf and other
                         self.first_conf_other_pkg_ver_buttom_button_frame.show()
                         self.first_conf_other_pkg_ver_table.show()
                         self.first_conf_other_pkg_ver_label.show()
                         self.first_conf_other_pkg_listview.show()
                         splash_flag = True
                     else:
                         #hide first conf and other
                         self.first_conf_other_pkg_ver_buttom_button_frame.hide()
                         self.first_conf_other_pkg_ver_table.hide()
                         self.first_conf_other_pkg_ver_label.hide()
                         self.first_conf_other_pkg_listview.hide()

                if key == 'second':
                     if value:
                         #show second conf and other
                         self.second_conf_other_pkg_ver_buttom_button_frame.show()
                         self.second_conf_other_pkg_ver_table.show()
                         self.second_conf_other_pkg_ver_label.show()
                         self.second_conf_other_pkg_listview.show()
                         splash_flag = True
                     else:
                         #hide second conf and other
                         self.second_conf_other_pkg_ver_buttom_button_frame.hide()
                         self.second_conf_other_pkg_ver_table.hide()
                         self.second_conf_other_pkg_ver_label.hide()
                         self.second_conf_other_pkg_listview.hide()

                if key == 'third':
                     if value:
                         #show third conf and other
                         self.third_conf_other_pkg_ver_buttom_button_frame.show()
                         self.third_conf_other_pkg_ver_table.show()
                         self.third_conf_other_pkg_ver_label.show()
                         self.third_conf_other_pkg_listview.show()
                         splash_flag = True
                     else:
                         #hide third conf and other
                         self.third_conf_other_pkg_ver_buttom_button_frame.hide()
                         self.third_conf_other_pkg_ver_table.hide()
                         self.third_conf_other_pkg_ver_label.hide()
                         self.third_conf_other_pkg_listview.hide()

                if key == 'manifest':
                    if value:
                        # show manifest
                        self.manifest_buttom_button_frame.show()
                        self.manifest_table.show()
                        self.manifest_file_label.show()
                        splash_flag = True
                    else:
                        # hide manifest
                        self.manifest_buttom_button_frame.hide()
                        self.manifest_table.hide()
                        self.manifest_file_label.hide()

                if key == 'tms':
                     if value:
                         #show tms
                         self.tms_param_buttom_button_frame.show()
                         self.tms_param_table.show()
                         self.tms_param_label.show()
                         splash_flag = True
                     else:
                         #hide tms
                         self.tms_param_buttom_button_frame.hide()
                         self.tms_param_table.hide()
                         self.tms_param_label.hide()

                if key == 'emv':
                    if value:
                        # show emv
                        self.emv_kernel_ver_buttom_button_frame.show()
                        self.emv_kernel_ver_table.show()
                        self.emv_kernel_version_label.show()
                        splash_flag = True
                    else:
                        # hide emv
                        self.emv_kernel_ver_buttom_button_frame.hide()
                        self.emv_kernel_ver_table.hide()
                        self.emv_kernel_version_label.hide()
            #Hide the splash screen if screen is occupied, shown only in start-up.
            if splash_flag:
                self.splash_label.setVisible(False)

        except Exception as e:
            print (str(e))

# ████████╗ █████╗ ██████╗ ██╗     ███████╗    ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗
# ╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║
#    ██║   ███████║██████╔╝██║     █████╗      ██╔████╔██║██║   ██║██║  ██║█████╗  ██║
#    ██║   ██╔══██║██╔══██╗██║     ██╔══╝      ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ██║
#    ██║   ██║  ██║██████╔╝███████╗███████╗    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗
#    ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝

    #Common table renderer using basic table model
    def populate_generic_table(self,table,result,color_code=None,hide_col=None):
        try:
            header = result.pop(0)
            rn = [str(c+1) for c in range(0,len(result))]
            data = pd.DataFrame(result, columns=header,index=rn)
            model = TableModel(data,color_code)
            table.setSelectionBehavior(QAbstractItemView.SelectRows)
            table.setModel(model)
            table.resizeColumnsToContents()
            if hide_col is not None:
                table.setColumnHidden(hide_col, True)
            return model
        except Exception as e:
            print (str(e))

    #change background color as per pkg group
    def populate_map_pkg_table(self,table,result):
        try:
            header = result.pop(0)
            rn = [str(c + 1) for c in range(0, len(result))]
            data = pd.DataFrame(result, columns=header, index=rn)
            model = MapPkgTableModel(data)
            table.setSelectionBehavior(QAbstractItemView.SelectRows)
            table.setModel(model)
            table.resizeColumnsToContents()
            #Hide the number column
            table.setColumnHidden(0, True)
            return model
        except Exception as e:
            print (str(e))

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, color_code = None):
        super(TableModel, self).__init__()
        self._data = data
        self._color_code = color_code

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        elif role == Qt.BackgroundRole:
            if self._color_code is None:
                return
            if self._color_code == 'jbz':
                return QColor(230, 230, 255) if index.row() % 2 == 0 else QColor(204, 204, 255)
            elif self._color_code == 'conf_other_1':
                #light red for conf 1 if even row else lighter red
                return QColor(255, 235, 230) if index.row() % 2 == 0 else QColor(255,214,204)
            elif self._color_code == 'conf_other_2':
                #lighter yellow for conf 2 if even row else light yellow
                return QColor(255, 255, 230) if index.row() % 2 == 0 else QColor(255, 255, 204)
            elif self._color_code == 'conf_other_3':
                #lighter green for conf 3 if even row else light green
                return QColor(230,255,230) if index.row() % 2 == 0 else QColor(204, 255, 204)
            elif self._color_code == 'manifest':
                #lighter blue for manifest if even row else light blue
                return QColor(230,240,255) if index.row() % 2 == 0 else QColor(204, 224, 255)
            elif self._color_code == 'tms':
                #lighter cream for tms if even row else light cream
                return QColor(255,242,230) if index.row() % 2 == 0 else QColor(255, 229, 204)
            elif self._color_code == 'emv':
                #lighter pink for emv if even row else light pink
                return QColor(255,230,255) if index.row() % 2 == 0 else QColor(255, 204, 255)

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

class MapPkgTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(MapPkgTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        elif role == Qt.BackgroundRole:
            value = self._data.iloc[index.row(), 0]
            if index.column() == 1 and int(value) == 0:
                #lighter blue for jbz if even row else light blue
                return QColor(230,230,255) if index.row() % 2 == 0 else QColor(204,204,255)
            elif index.column() == 1 and int(value) == 1:
                #light red for conf 1 if even row else lighter red
                return QColor(255, 235, 230) if index.row() % 2 == 0 else QColor(255,214,204)
            elif index.column() == 1 and int(value) == 2:
                #lighter yellow for conf 2 if even row else light yellow
                return QColor(255, 255, 230) if index.row() % 2 == 0 else QColor(255, 255, 204)
            elif index.column() == 1 and int(value) == 3:
                #lighter green for conf 3 if even row else light green
                return QColor(230,255,230) if index.row() % 2 == 0 else QColor(204, 255, 204)

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

# ███╗   ███╗ █████╗ ██╗███╗   ██╗
# ████╗ ████║██╔══██╗██║████╗  ██║
# ██╔████╔██║███████║██║██╔██╗ ██║
# ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
# ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    #Override closeEvent so all other widgets will close if Main Window is exited.
    class CustomMainWindow(QtWidgets.QMainWindow):
        def closeEvent(self, *args, **kwargs):
            sys.exit(app.exec_())

    version_checker_mainwindow = CustomMainWindow()
    ui = Launcher()
    ui.setupUi(version_checker_mainwindow)
    ui.extendUI(version_checker_mainwindow)
    sys.exit(app.exec_())

# To convert ui to py
# pyuic5 main.ui -o main.py
# pyuic5 emv.ui -o emv.py
# pyuic5 tms_param.ui -o tms_param.py
# pyuic5 jbz_pkg.ui -o jbz_pkg.py
# pyuic5 jfrog.ui -o jfrog.py
# pyuic5 save_on_screen_data.ui -o save_on_screen_data.py
# pyuic5 load_to_screen.ui -o load_to_screen.py
# pyuic5 map.ui -o map.py
# pyuic5 compare.ui -o compare.py
# pyuic5 settings.ui -o settings.py

# To make .exe
# pyinstaller --noconsole --onefile --windowed --icon=../vc.ico launcher.py

# does not work
# pyinstaller --noconsole --onefile --windowed --icon=vc.ico gui/launcher.py

# https://manytools.org/hacker-tools/ascii-banner/