import os
import re
import shutil

from texttable import Texttable
from subprocess import Popen,PIPE

class JobBundleExtraction:
    def __init__(self):
        self.base_xtrak_path = "D:/JonNgoStorage/my_hack_project/opt_version_checker/"
        self.sevenZ_exe = "C:/Program Files/7-Zip/7z.exe"
        self.extract_folder = "xtrak_level_"
        self.extract_file_starting_index = 1
        self.extract_file_ending_index = 5
        self.manifest_file = "manifest.mnf"
        self.regexp_string = r"\d{2}.\d{2}.\d{4}"
        self.use_full_path = False

    def filenameOnly(self,f):
        return os.path.splitext(f.split('/')[-1])[0]

    def set_regex_to_find_version(self,regex_in):
        self.regexp_string = re.compile(regex_in)

    def getVersion(self,v):
        match_ver = re.findall(self.regexp_string, v)
        ret_ver = None
        try:
            ret_ver = match_ver[-1]
        except IndexError:
            print("Invalid match - "+v)
        return ret_ver

    def remove_path(self,pkg_name1):
        index_to = pkg_name1.rfind('\\')
        if index_to != -1:
            return pkg_name1[index_to:]
        else:
            return pkg_name1

    #Determine whether pkg is v1 or v255
    def package_version_type(self,file):
        with open(file, 'rb') as fin:
            header = fin.read(1)
            return str(int.from_bytes(header, byteorder='little'))

    def clear_xtrak_folders(self, tag):
        for x in range(self.extract_file_starting_index,self.extract_file_ending_index+1):
            if os.path.exists(self.base_xtrak_path+tag+'/'+self.extract_folder+str(x)):
                try:
                    shutil.rmtree(self.base_xtrak_path+tag+'/'+self.extract_folder+str(x))
                except:
                    print('Error while deleting directory ... {}'.format(self.base_xtrak_path+tag+'/' + self.extract_folder + str(x)))

    def extract(self, tag=0,jbz_file=None):
        #Remove existing extract folder
        self.clear_xtrak_folders(str(tag))

        pkg_list = [jbz_file, ]

        for x in range(self.extract_file_starting_index,self.extract_file_ending_index+1):
            for p in pkg_list:
                print (p)
                process = Popen([self.sevenZ_exe,"x",p,"-o"+self.base_xtrak_path+str(tag)+'/'+self.extract_folder+str(x)+'/'+self.filenameOnly(p)+"/","*"], stdout=PIPE, stderr=PIPE)
                stdout, stderr = process.communicate()
                s = stdout.decode("utf-8")
                print(s)

            #If the extract folder is not created then break from the loop
            if not os.path.exists(self.base_xtrak_path+str(tag)+'/'+self.extract_folder+str(x)):
                break;
            #Display only .pkg
            # pkg_list = [os.path.join(root, name) for root, dirs, files in
            #             os.walk(self.base_xtrak_path+str(tag)+'/' + self.extract_folder + str(x) + '/') for name in files if os.path.join(root, name).endswith(".pkg")]

            pkg_list = [os.path.join(root, name) for root, dirs, files in os.walk(self.base_xtrak_path+str(tag)+'/' + self.extract_folder + str(x) + '/') for name in files]

            # for i in pkg_list:
            #     print('... {}'.format(i))

        master_pkg_list = []
        master_pkg_list.append(['Package','Pkg Ver'])

        for x in range(self.extract_file_starting_index,self.extract_file_ending_index+1):
            if os.path.exists(self.base_xtrak_path+str(tag)+'/' + self.extract_folder + str(x)):
                print('processing ... {}'.format(x))
                for root, dirs, files in os.walk(self.base_xtrak_path+str(tag)+'/'+self.extract_folder+str(x)):
                    for name in files:
                        if name.endswith('.pkg'):
                            v = self.package_version_type(os.path.join(root, name))
                            if v is not None:
                                if self.use_full_path:
                                    master_pkg_list.append(["".join(os.path.join(root, name).split('/')[4:]),v])
                                else:
                                    master_pkg_list.append([name, v])

        self.display_table(master_pkg_list)

        #Find manifest file

        manifest = None

        for x in range(self.extract_file_starting_index, self.extract_file_ending_index + 1):
            for root, dirs, files in os.walk(self.base_xtrak_path+str(tag)+'/' + self.extract_folder + str(x)):
                for name in files:
                    if self.manifest_file == name:
                        manifest_file = "".join(os.path.join(root, name))

                        try:
                            with open(manifest_file, 'r') as f:
                                raw_manifest = f.readlines()
                        except(IOError):
                            print('IOError')
                        except(ValueError):
                            print('ValueError')

                        #This part may be improved using Pandas

                        mlist = [i.strip() for i in raw_manifest if 'version' in i or 'name' in i]

                        v = []
                        n = []

                        for kv in mlist:
                            if kv.startswith('version'):
                                v.append(kv)
                            if kv.startswith('name'):
                                n.append(kv)
                        #get rid of the first version
                        v.pop(0)

                        manifest = [[n[c].split('"')[1], v[c].split('"')[1]] for c in range(0, len(v))]
                        manifest.insert(0,['TAG','VERSION'])

        if manifest is not None:
            self.display_table(manifest)

        return master_pkg_list, manifest

    def display_table(self, content):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_cols_dtype(['t', 't'])  # text
        table.set_cols_width([180, 20])

        table.set_cols_align(["l", "l"])
        table.add_rows(content)
        print(table.draw())

# Uncomment to perform module test.
# if __name__ == "__main__":
#     file_to_extract = 'D:/JonNgoStorage/sequioa/R3.2.1/02.02.0050/R3.2.1_seq_platform_dev_su_with_bm_qatest_02.02.0050.jbz'
#     #file_to_extract = 'D:/JonNgoStorage/sequioa/R3.2.1/02.02.0050/R3.2.1_seq_factory_dev_02.02.0050.tgz'
#     jbx = JobBundleExtraction()
#     result_jbz, result_manifest = jbx.extract(file_to_extract)
#     if result_manifest is None:
#         print('No manifest file found')

# header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)