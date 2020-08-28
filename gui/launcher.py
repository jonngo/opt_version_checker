import os

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView

import package
from gui import Ui_MainWindow
from gui import Ui_pkg_widget
from gui import Ui_emv_widget
from gui import Ui_tms_widget
from gui import Ui_jfrog_widget
from gui import Ui_save_widget
from gui import Ui_load_widget
from gui import Ui_map_widget
from PyQt5 import QtCore, QtWidgets, QtGui
from jbz_extraction import JobBundleExtraction
from emv_version import EmvExtraction
from tms_parameters import TmsExtraction
from jfrog_artifactory import JfrogArtifactory
import sys
from PyQt5.QtCore import Qt
import pandas as pd
import json

class Launcher(Ui_MainWindow, Ui_pkg_widget, Ui_emv_widget, Ui_tms_widget, Ui_jfrog_widget, Ui_save_widget, Ui_load_widget, Ui_map_widget):
    def __init__(self):
        with open("config.json") as json_data_file:
            data = json.load(json_data_file)
            for conf in data['pkg_version_cfg']:

                """
                    Configuration variables of package version
                        - conf_base_xtrak_path
                        - conf_sevenZ_exe
                        - conf_manifest
                        - conf_regexp_string
                """

                if 'base_xtrak_path' in conf:
                    self.conf_base_xtrak_path = conf['base_xtrak_path']
                elif 'sevenZ_exe' in conf:
                    self.conf_sevenZ_exe = conf['sevenZ_exe']
                elif 'manifest_file' in conf:
                    self.conf_manifest = conf['manifest_file']
                elif 'regexp_string' in conf:
                    self.conf_regexp_string = conf['regexp_string']

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

            #TODO include in the config the default directory to open, this is for all file dialog

            #TODO config of destination folder for saving

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


    #MAIN
    def extendUI(self,version_checker_mainwindow):
        #Initialize Widgets
        self.init_jfrog_widget()
        self.init_pkg_widget()
        self.init_emv_widget()
        self.init_tms_widget()
        self.init_save_widget()
        self.init_load_widget()
        self.init_map_widget()

        #Source Menu
        self.jbz_pkg_menu_item.triggered.connect(self.open_pkg_widget)
        self.emv_menu_item.triggered.connect(self.open_emv_widget)
        self.tmsLite_menu_item.triggered.connect(self.open_tms_widget)
        self.jfrog_menu_item.triggered.connect(self.open_jfrog_widget)
        self.save_menu_item.triggered.connect(self.open_save_widget)
        self.load_menu_item.triggered.connect(self.open_load_widget)
        self.map_menu_item.triggered.connect(self.open_map_widget)

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

        #toggle package header button
        self.pkg_header_pushbutton.clicked.connect(self.jbz_toggle_header_listview)
        self.first_conf_other_pkg_header_pushbutton.clicked.connect(self.first_conf_other_toggle_header_listview)
        self.second_conf_other_pkg_header_pushbutton.clicked.connect(self.second_conf_other_toggle_header_listview)
        self.third_conf_other_pkg_header_pushbutton.clicked.connect(self.third_conf_other_toggle_header_listview)


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

    #MAP (This is to map the key name from different sources which will be used for the filter rules)
    def init_map_widget(self):
        self.map_widget = QtWidgets.QWidget()
        self.map_ui = Ui_map_widget()
        self.map_ui.setupUi(self.map_widget)

        self.map_ui.map_pkg_filter_Line_edit.textChanged['QString'].connect(self.map_filter_pkg_field)
        self.map_ui.map_manifest_filter_line_edit.textChanged['QString'].connect(self.map_filter_manifest_field)
        self.map_ui.map_emv_filter_line_edit.textChanged['QString'].connect(self.map_filter_emv_field)
        self.map_ui.map_tms_filter_line_edit.textChanged['QString'].connect(self.map_filter_tms_field)

        self.map_ui.map_add_push_button.clicked.connect(self.add_to_rule_table)

    def open_map_widget(self):
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
            self.model_map_manifest_table = self.populate_generic_table(self.map_ui.map_manifest_table, self.map_manifest_result_list)
            self.map_ui.map_manifest_table.doubleClicked.connect(self.map_stage_manifest)

        if self.result_tms:
            self.map_tms_result_list = self.result_tms.copy()
            self.map_tms_result_list.insert(0, ['TAG', 'VALUE'])
            self.model_map_tms_table = self.populate_generic_table(self.map_ui.map_tms_table, self.map_tms_result_list)
            self.map_ui.map_tms_table.doubleClicked.connect(self.map_stage_tms)

        if self.result_emv:
            self.map_emv_result_list = self.result_emv.copy()
            self.map_emv_result_list.insert(0,["TAG", "VERSION"])
            self.model_map_emv_table = self.populate_generic_table(self.map_ui.map_emv_table, self.map_emv_result_list)
            self.map_ui.map_emv_table.doubleClicked.connect(self.map_stage_emv)

        self.map_widget.show()

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
            print('function: add_to_rule_table')
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
            print('function: common map filter field')
            print (str(e))

    def map_filter_pkg_field(self):
        self.map_merged_pkg_result, self.model_map_pkg_table = self.common_map_filter_field(True, self.map_merged_pkg_result_orig, self.map_ui.map_pkg_filter_Line_edit, ['#', 'Pkg'], self.map_ui.map_pkg_table)

    def map_filter_manifest_field(self):
        self.map_manifest_result_list, self.model_map_manifest_table = self.common_map_filter_field(False, self.result_manifest, self.map_ui.map_manifest_filter_line_edit, ['TAG', 'VERSION'], self.map_ui.map_manifest_table)

    def map_filter_emv_field(self):
        self.map_emv_result_list, self.model_map_emv_table = self.common_map_filter_field(False, self.result_emv, self.map_ui.map_emv_filter_line_edit, ["TAG", "VERSION"], self.map_ui.map_emv_table)

    def map_filter_tms_field(self):
        self.map_tms_result_list, self.model_map_tms_table = self.common_map_filter_field(False, self.result_tms, self.map_ui.map_tms_filter_line_edit, ['TAG', 'VALUE'], self.map_ui.map_tms_table)

    #return the package name only from the package file name + version + KVC.
    def parse_package_name(self, p):
        return "_".join(p.split('_')[:-2])

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
            print('function: common_map_stage')
            print (str(e))

    #Double clicking the table will put it in the staging field, ready to commit to the table below.
    def map_stage_the_pkg_name(self, signal):
        self.common_map_stage(signal,1,self.model_map_pkg_table,self.map_ui.map_pkg_ver_line_edit,True)

    def map_stage_manifest(self, signal):
        self.common_map_stage(signal,0,self.model_map_manifest_table,self.map_ui.map_manifest_line_edit,False)

    def map_stage_tms(self, signal):
        self.common_map_stage(signal,0,self.model_map_tms_table,self.map_ui.map_tms_line_edit,False)

    def map_stage_emv(self, signal):
        self.common_map_stage(signal,0,self.model_map_emv_table,self.map_ui.map_emv_line_edit,False)

    #LOAD TO SCREEN
    def init_load_widget(self):
        self.load_to_screen_widget = QtWidgets.QWidget()
        self.load_to_screen_ui = Ui_load_widget()
        self.load_to_screen_ui.setupUi(self.load_to_screen_widget)
        self.load_to_screen_ui.load_browse_filename_push_button.clicked.connect(self.browse_filename_to_load)
        self.load_to_screen_ui.load_load_push_button.clicked.connect(self.load_display_to_screen)

    def open_load_widget(self):
        self.load_to_screen_widget.hide()
        self.load_to_screen_widget.show()

    def browse_filename_to_load(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(None,'Open file','C:\\Users\\jonathann\\invenco',"json files (*.json))")

        #file = str(QFileDialog.getExistingDirectory())
        if file:
            self.load_to_screen_ui.load_filename_line_edit.setText(file)

    def load_display_to_screen(self):
        #TODO refactor the load function, too many duplicate code
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
            try:
                temp_result_list = []
                temp_ref_result_list = []
                temp_result_list.append(['Package', 'Pkg Ver'])
                for result in data['jbz']:
                    for k, v in result.items():
                        temp_result_list.append([k,v[0]])
                        temp_ref_result_list.append([k,v[0],v[1]])
                self.result_jbz = temp_result_list
                self.result_jbz_ref = temp_ref_result_list
            except Exception as e:
                print (str(e)+' does not exist')

            #Retrieve content from conf others 1 dictionary and assign to conf others 1 result list
            try:
                temp_result_list = []
                temp_ref_result_list = []
                temp_result_list.append(['Package', 'Pkg Ver'])
                for result in data['conf_other_1']:
                    for k, v in result.items():
                        temp_result_list.append([k,v[0]])
                        temp_ref_result_list.append([k,v[0],v[1]])
                self.result_conf_other_1 = temp_result_list
                self.result_conf_other_1_ref = temp_ref_result_list
            except Exception as e:
                print (str(e)+' does not exist')

            #Retrieve content from conf others 2 dictionary and assign to conf others 2 result list
            try:
                temp_result_list = []
                temp_ref_result_list = []
                temp_result_list.append(['Package', 'Pkg Ver'])
                for result in data['conf_other_2']:
                    for k, v in result.items():
                        temp_result_list.append([k,v[0]])
                        temp_ref_result_list.append([k,v[0],v[1]])
                self.result_conf_other_2 = temp_result_list
                self.result_conf_other_2_ref = temp_ref_result_list
            except Exception as e:
                print (str(e)+' does not exist')

            #Retrieve content from conf others 3 dictionary and assign to conf others 3 result list
            try:
                temp_result_list = []
                temp_ref_result_list = []
                temp_result_list.append(['Package', 'Pkg Ver'])
                for result in data['conf_other_3']:
                    for k, v in result.items():
                        temp_result_list.append([k,v[0]])
                        temp_ref_result_list.append([k,v[0],v[1]])
                self.result_conf_other_3 = temp_result_list
                self.result_conf_other_3_ref = temp_ref_result_list
            except Exception as e:
                print (str(e)+' does not exist')

            #Retrieve content from manifest dictionary and assign to manifest result list
            try:
                temp_result_list = []
                temp_result_list.append(['Package', 'Pkg Ver'])
                for result in data['manifest']:
                    for k, v in result.items():
                        temp_result_list.append([k,v])
                self.result_manifest = temp_result_list
            except Exception as e:
                print (str(e)+' does not exist')

            #Retrieve content from tms dictionary and assign to tms result list
            try:
                temp_result_list = []
                temp_result_list.append(['Package', 'Pkg Ver'])
                for result in data['tms']:
                    for k, v in result.items():
                        temp_result_list.append([k,v])
                self.result_tms = temp_result_list
            except Exception as e:
                print (str(e)+' does not exist')

            #Retrieve content from emv dictionary and assign to emv result list
            try:
                temp_result_list = []
                temp_result_list.append(['Package', 'Pkg Ver'])
                for result in data['emv']:
                    for k, v in result.items():
                        temp_result_list.append([k,v])
                self.result_emv = temp_result_list
            except Exception as e:
                print (str(e)+' does not exist')

            #Populate the tables from the loaded list

            if self.result_jbz:
                self.populate_generic_table(self.jbz_pkg_ver_table, self.result_jbz, color_code='jbz')
                self.show_hide_panel({'jbz':True})
                self.pkg_listview.hide()

            if self.result_conf_other_1:
                self.populate_generic_table(self.first_conf_other_pkg_ver_table, self.result_conf_other_1, color_code='conf_other_1')
                self.show_hide_panel({'first':True})
                self.first_conf_other_pkg_listview.hide()

            if self.result_conf_other_2:
                self.populate_generic_table(self.second_conf_other_pkg_ver_table, self.result_conf_other_2, color_code='conf_other_2')
                self.show_hide_panel({'second':True})
                self.second_conf_other_pkg_listview.hide()

            if self.result_conf_other_3:
                self.populate_generic_table(self.third_conf_other_pkg_ver_table, self.result_conf_other_3, color_code='conf_other_3')
                self.show_hide_panel({'third':True})
                self.third_conf_other_pkg_listview.hide()

            if self.result_manifest:
                self.populate_generic_table(self.manifest_table, self.result_manifest)
                self.show_hide_panel({'manifest': True})

            if self.result_tms:
                self.populate_generic_table(self.tms_param_table, self.result_tms)
                self.show_hide_panel({'tms': True})

            if self.result_emv:
                self.populate_generic_table(self.emv_kernel_ver_table, self.result_emv)
                self.show_hide_panel({'emv': True})

        self.load_to_screen_widget.hide()

    #SAVE ON SCREEN DATA
    def init_save_widget(self):
        self.save_on_screen_widget = QtWidgets.QWidget()
        self.save_on_screen_ui = Ui_save_widget()
        self.save_on_screen_ui.setupUi(self.save_on_screen_widget)
        self.save_on_screen_ui.save_save_button.clicked.connect(self.save_on_screen_to_json)

    def open_save_widget(self):
        self.save_on_screen_ui.save_filename_line_edit.setText('')
        self.save_on_screen_widget.hide()
        self.save_on_screen_widget.show()

    #common jsonify pattern
    def common_jsonify_of_result_list(self,result_json_string,source,result_ref):
        result_json_string = result_json_string +'"'+source+'":['
        for rl in result_ref:
            result_json_string = result_json_string + '{"'+rl[0]+'":"'+rl[1]+'"},'
        result_json_string = result_json_string[:-1]
        result_json_string = result_json_string + '],'
        return result_json_string

    def common_jsonify_of_result_list_with_header_info(self,result_json_string,source,result_ref):
        result_json_string = result_json_string +'"'+source+'":['
        for rl in result_ref:
            result_json_string = result_json_string + '{"'+rl[0]+'":["'+rl[1]+'","'+rl[2]+'"]},'
        result_json_string = result_json_string[:-1]
        result_json_string = result_json_string + '],'
        return result_json_string

    #Convert the results to json string
    def results_to_json(self):
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

    def save_on_screen_to_json(self):
        filename = self.save_on_screen_ui.save_filename_line_edit.text()
        print(filename)
        if filename != '':
            with open(filename+'.json', 'w') as outfile:
                json.dump(json.loads(self.results_to_json()), outfile)

        self.save_on_screen_widget.hide()

    #JBZ PACKAGE VERSION
    def init_pkg_widget(self):
        self.pkg_widget = QtWidgets.QWidget()
        self.pkg_ui = Ui_pkg_widget()
        self.pkg_ui.setupUi(self.pkg_widget)
        self.pkg_ui.jbzPathPushButton.clicked.connect(self.search_jbz_path)
        self.pkg_ui.extractPushButton.clicked.connect(self.extract_jbz_and_other_pkg)
        self.pkg_ui.conf_other_pkg_1_push_button.clicked.connect(self.search_other_pkg_path_1)
        self.pkg_ui.conf_other_pkg_2_push_button.clicked.connect(self.search_other_pkg_path_2)
        self.pkg_ui.conf_other_pkg_3_push_button.clicked.connect(self.search_other_pkg_path_3)

    def open_pkg_widget(self):
        self.pkg_ui.extractionPathLineEdit.setText(self.conf_base_xtrak_path)
        self.pkg_ui.sevenZlineEdit.setText(self.conf_sevenZ_exe)
        self.pkg_ui.jbz_manifest_line_edit.setText(self.conf_manifest)
        self.pkg_ui.jbz_regex_match_ver_line_edit.setText(self.conf_regexp_string)
        self.pkg_widget.hide()
        self.pkg_widget.show()

    def open_file_dialog(self,line_edit):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName()

        if file:
            line_edit.setText(file)

    def search_jbz_path(self):
        self.open_file_dialog(self.pkg_ui.jbzPathLineEdit)

    def search_other_pkg_path_1(self):
        self.open_file_dialog(self.pkg_ui.conf_other_pkg_1_line_edit)

    def search_other_pkg_path_2(self):
        self.open_file_dialog(self.pkg_ui.conf_other_pkg_2_line_edit)

    def search_other_pkg_path_3(self):
        self.open_file_dialog(self.pkg_ui.conf_other_pkg_3_line_edit)

    def extract_jbz_and_other_pkg(self):
        self.jbx = JobBundleExtraction()

        #Initialize from configuration
        self.jbx.base_xtrak_path = self.conf_base_xtrak_path
        self.jbx.sevenZ_exe = self.conf_sevenZ_exe
        self.jbx.manifest_file = self.conf_manifest
        self.jbx.regexp_string = self.conf_regexp_string

        #Do extraction if there is an entry from the line edit field.
        if self.pkg_ui.jbzPathLineEdit.text() != "":
            self.result_jbz,self.result_manifest,self.result_jbz_ref = self.jbx.extract(tag=0,jbz_file=self.pkg_ui.jbzPathLineEdit.text())
            if self.result_jbz:
                self.show_hide_panel({'jbz':True})
            if self.result_manifest:
                self.show_hide_panel({'manifest': True})

        if self.pkg_ui.conf_other_pkg_1_line_edit.text() != "":
            self.result_conf_other_1,_,self.result_conf_other_1_ref = self.jbx.extract(tag=1,jbz_file=self.pkg_ui.conf_other_pkg_1_line_edit.text())
            if self.result_conf_other_1:
                self.show_hide_panel({'first':True})

        if self.pkg_ui.conf_other_pkg_2_line_edit.text() != "":
            self.result_conf_other_2,_,self.result_conf_other_2_ref = self.jbx.extract(tag=2,jbz_file=self.pkg_ui.conf_other_pkg_2_line_edit.text())
            if self.result_conf_other_2:
                self.show_hide_panel({'second': True})

        if self.pkg_ui.conf_other_pkg_3_line_edit.text() != "":
            self.result_conf_other_3,_,self.result_conf_other_3_ref = self.jbx.extract(tag=3,jbz_file=self.pkg_ui.conf_other_pkg_3_line_edit.text())
            if self.result_conf_other_3:
                self.show_hide_panel({'third': True})

        self.pkg_widget.hide()

        #Display the result from extraction
        if self.result_jbz:
            self.populate_jb_table(self.result_jbz)
            self.job_bundle_pkg_ver_label.setText("..."+self.pkg_ui.jbzPathLineEdit.text()[-40:])
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

    def populate_jb_table(self,result):
        self.model_jbz_pkg_ver_table = self.populate_generic_table(self.jbz_pkg_ver_table,result,color_code='jbz')
        self.jbz_pkg_ver_table.clicked.connect(self.jbz_package_info)


    def populate_first_conf_table(self,result):
        self.model_first_conf_ver_table = self.populate_generic_table(self.first_conf_other_pkg_ver_table,result,color_code='conf_other_1')
        self.first_conf_other_pkg_ver_table.clicked.connect(self.first_conf_package_info)

    def populate_second_conf_table(self,result):
        self.model_second_conf_ver_table = self.populate_generic_table(self.second_conf_other_pkg_ver_table,result,color_code='conf_other_2')
        self.second_conf_other_pkg_ver_table.clicked.connect(self.second_conf_package_info)

    def populate_third_conf_table(self,result):
        self.model_third_conf_ver_table = self.populate_generic_table(self.third_conf_other_pkg_ver_table,result,color_code='conf_other_3')
        self.third_conf_other_pkg_ver_table.clicked.connect(self.third_conf_package_info)

    def populate_manifest_table(self,result):
        self.model_manifest_table = self.populate_generic_table(self.manifest_table,result)

    #This is called by package info functions to display the header information
    def common_package_info_table_setter(self,signal,model,list_model,list_view, folder_index):
        row = signal.row()
        index = signal.sibling(row, 0)
        index_dict = model.itemData(index)
        index_value = index_dict.get(0)

        pkg_header_string = str(package.header_info(self.get_pkg_full_path(index_value,folder_index)))

        list_model.clear()

        for h in pkg_header_string.splitlines():
            list_model.appendRow(QStandardItem(h))

        # Apply the model to the list view
        list_view.setModel(list_model)

    def jbz_package_info(self,signal):
        self.common_package_info_table_setter(signal, self.model_jbz_pkg_ver_table, self.pkg_header_list_model, self.pkg_listview, 0)

    def first_conf_package_info(self,signal):
        self.common_package_info_table_setter(signal, self.model_first_conf_ver_table, self.first_conf_other_pkg_header_list_model, self.first_conf_other_pkg_listview,1)

    def second_conf_package_info(self,signal):
        self.common_package_info_table_setter(signal, self.model_second_conf_ver_table, self.second_conf_other_pkg_header_list_model, self.second_conf_other_pkg_listview,2)

    def third_conf_package_info(self,signal):
        self.common_package_info_table_setter(signal, self.model_third_conf_ver_table, self.third_conf_other_pkg_header_list_model, self.third_conf_other_pkg_listview, 3)

    def get_pkg_full_path(self,pkg_name,tag):
        for x in range(self.jbx.extract_file_starting_index,self.jbx.extract_file_ending_index+1):
            if os.path.exists(self.jbx.base_xtrak_path+str(tag)+'/' + self.jbx.extract_folder + str(x)):
                print('processing ... {}'.format(x))
                for root, dirs, files in os.walk(self.jbx.base_xtrak_path+str(tag)+'/'+self.jbx.extract_folder+str(x)):
                    for name in files:
                        if name == pkg_name:
                            return os.path.join(root,name)

    #EMV KERNEL VERSION
    def init_emv_widget(self):
        self.emv_widget = QtWidgets.QWidget()
        self.emv_ui = Ui_emv_widget()
        self.emv_ui.setupUi(self.emv_widget)
        self.emv_ui.extractEMVPushButton.clicked.connect(self.extract_emv)
        self.device_customer_list = ["G6-300","G7-100 NCR","G7-100 Canada","G6-200"]
        self.emv_ui.emv_device_comboBox.addItems(self.device_customer_list)

    def open_emv_widget(self):
        emvx = EmvExtraction()
        self.emv_ui.emv_ver_url_lineedit.setText(self.conf_emv_ver_url)
        self.emv_ui.chrome_driver_lineEdit.setText(self.conf_chrome_driver_filepath)
        self.emv_widget.hide()
        self.emv_widget.show()

    def extract_emv(self):
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
        self.populate_generic_table(self.emv_kernel_ver_table,self.result_emv)
        self.show_hide_panel({'emv': True})
        self.emv_widget.hide()

    #TMSLITE PARAMETERS
    def init_tms_widget(self):
        self.tms_widget = QtWidgets.QWidget()
        self.tms_ui = Ui_tms_widget()
        self.tms_ui.setupUi(self.tms_widget)
        self.tms_ui.tms_param_search_push_button.clicked.connect(self.search_tms_params_csv)
        self.tms_ui.tms_param_load_push_button.clicked.connect(self.load_tms)

    def open_tms_widget(self):
        self.tms_widget.hide()
        self.tms_widget.show()


    def load_tms(self):
        tmsx = TmsExtraction()
        self.result_tms = tmsx.load_tms_parameters(self.tms_ui.tmslite_param_line_edit.text())
        self.tms_widget.hide()
        self.populate_generic_table(self.tms_param_table,self.result_tms)
        self.show_hide_panel({'tms': True})

    def search_tms_params_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(None,'Open file','D:\\JonNgoStorage',"csv files (*.csv))")

        #file = str(QFileDialog.getExistingDirectory())
        if file:
            self.tms_ui.tmslite_param_line_edit.setText(file)

    #JFROG ARTIFACTORY
    def init_jfrog_widget(self):
        self.jfrog_widget = QtWidgets.QWidget()
        self.jfrog_ui = Ui_jfrog_widget()
        self.jfrog_ui.setupUi(self.jfrog_widget)
        #Jfrog Artifactory Signals
        self.jfrog_ui.jfrog_load_push_button.clicked.connect(self.load_selected_sku_bundle)
        self.jfrog_ui.jfrog_build_ver_line_edit.returnPressed.connect(self.load_build_list)

    def open_jfrog_widget(self):
        self.jfrog_widget.hide()
        self.jfrog_widget.show()

    #Jfrog Artifactory slot when Load button is clicked
    def load_build_list(self):
        jfrog_art = JfrogArtifactory()
        self.result_of_jfrog_list = jfrog_art.load_artifact(self.jfrog_ui.jfrog_build_ver_line_edit.text())
        self.populate_jfrog_sku_bundle_table(self.result_of_jfrog_list)

    def load_selected_sku_bundle(self):
        if self.result_of_jfrog_list:
            self.populate_jfrog_table(self.result_of_jfrog_list)
            self.jfrog_widget.hide()
            self.show_hide_panel({'jfrog': True})

    def populate_jfrog_sku_bundle_table(self,result_orig):
        result = result_orig.copy()
        header = result.pop(0)
        rn = [str(c+1) for c in range(0,len(result))]
        data = pd.DataFrame(result, columns=header,index=rn)
        self.model = TableModel(data)
        self.jfrog_ui.jfrog_all_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.jfrog_ui.jfrog_all_tableview.setModel(self.model)
        self.jfrog_ui.jfrog_all_tableview.resizeColumnsToContents()

    def populate_jfrog_table(self,result):
        header = result.pop(0)
        rn = [str(c+1) for c in range(0,len(result))]
        data = pd.DataFrame(result, columns=header,index=rn)
        self.model = TableModel(data)
        self.jfrog_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.jfrog_table.setModel(self.model)
        self.jfrog_table.resizeColumnsToContents()

    #Common table renderer using basic table model
    def populate_generic_table(self,table,result,color_code=None):
        header = result.pop(0)
        rn = [str(c+1) for c in range(0,len(result))]
        data = pd.DataFrame(result, columns=header,index=rn)
        model = TableModel(data,color_code)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setModel(model)
        table.resizeColumnsToContents()
        return model

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


    #Toggle the package header list view
    def toggle_header_listview(self,listview):
        if listview.isVisible():
            listview.hide()
        else:
            listview.show()

    def jbz_toggle_header_listview(self):
        self.toggle_header_listview(self.pkg_listview)

    def first_conf_other_toggle_header_listview(self):
        self.toggle_header_listview(self.first_conf_other_pkg_listview)

    def second_conf_other_toggle_header_listview(self):
        self.toggle_header_listview(self.second_conf_other_pkg_listview)

    def third_conf_other_toggle_header_listview(self):
        self.toggle_header_listview(self.third_conf_other_pkg_listview)

    #Hide panel
    def show_hide_panel(self, hs_dict):
        for key, value in hs_dict.items():
            if key == 'jfrog':
                if value:
                    #show jfrog
                    self.jfrog_buttom_button_frame.show()
                    self.jfrog_table.show()
                    self.jfrog_label.show()
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
                else:
                    # hide emv
                    self.emv_kernel_ver_buttom_button_frame.hide()
                    self.emv_kernel_ver_table.hide()
                    self.emv_kernel_version_label.hide()

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

# To make .exe
# pyinstaller --noconsole --onefile --windowed --icon=../vc.ico launcher.py

# does not work
# pyinstaller --noconsole --onefile --windowed --icon=vc.ico gui/launcher.py

