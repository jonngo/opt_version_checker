import os
import re
import shutil

from texttable import Texttable
from subprocess import Popen,PIPE
import package

class JobBundleExtraction:
    def __init__(self):
        self.base_xtrak_path = "D:/JonNgoStorage/my_hack_project/opt_version_checker/"
        self.sevenZ_exe = "C:/Program Files/7-Zip/7z.exe"
        self.extract_folder = "xtrak_level_"
        self.extract_file_starting_index = 1
        self.extract_file_ending_index = 5
        self.manifest_file = "manifest.mnf"

    def filenameOnly(self,f):
        return os.path.splitext(f.split('/')[-1])[0]

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

    def packman_version(self,file):
        package.header_info()

    def clear_xtrak_folders(self, tag):
        for x in range(self.extract_file_starting_index,self.extract_file_ending_index+1):
            if os.path.exists(self.base_xtrak_path+tag+'/'+self.extract_folder+str(x)):
                try:
                    shutil.rmtree(self.base_xtrak_path+tag+'/'+self.extract_folder+str(x))
                except:
                    print('Error while deleting directory ... {}'.format(self.base_xtrak_path+tag+'/' + self.extract_folder + str(x)))

    #The return version string of Packman code is inconsistent, this will detect the type and convert to string.
    def string_version(self, v):
        if type(v) is str:
            return v
        elif type(v) is bytes:
            return v.decode()
        else:
            print('Neither str or bytes type: '+v)
            return v

    #returns the package name only
    def parse_package_name(self, p):
        return "_".join(p.split('_')[:-2])

    #returns the KVC from the package name string
    def parse_package_kvc(self, p):
        return p.split('_')[-1].split('.')[-2]

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

        master_pkg_list = []
        master_pkg_list.append(['PACKAGE', 'PKG VER', 'Path'])

        #This list is used when saving packages, include in this other header information if needed.
        ref_pkg_list = []

        for x in range(self.extract_file_starting_index,self.extract_file_ending_index+1):
            if os.path.exists(self.base_xtrak_path+str(tag)+'/' + self.extract_folder + str(x)):
                print('processing ... {}'.format(x))
                for root, dirs, files in os.walk(self.base_xtrak_path+str(tag)+'/'+self.extract_folder+str(x)):
                    for name in files:
                        if name.endswith('.pkg'):
                            v = self.package_version_type(os.path.join(root, name))
                            # pmv - version from packman
                            pmv = self.string_version(package.version_num(os.path.join(root, name)))
                            if v is not None:
                                master_pkg_list.append([name, v, os.path.join(root, name)])
                                ref_pkg_list.append([name, v, pmv])
                                # master_pkg_list.append([self.parse_package_name(name),pmv,self.parse_package_kvc(name), v])

        # self.display_table(master_pkg_list)

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

        # if manifest is not None:
        #     self.display_table(manifest)

        return master_pkg_list, manifest, ref_pkg_list

    # def display_table(self, content):
    #     table = Texttable()
    #     table.set_deco(Texttable.HEADER)
    #     table.set_cols_dtype(['t', 't'])  # text
    #     table.set_cols_width([180, 20])
    #
    #     table.set_cols_align(["l", "l"])
    #     table.add_rows(content)
    #     print(table.draw())

# Uncomment to perform module test.
# if __name__ == "__main__":
#     file_to_extract = 'D:/JonNgoStorage/sequioa/R3.2.1/02.02.0050/R3.2.1_seq_platform_dev_su_with_bm_qatest_02.02.0050.jbz'
#     #file_to_extract = 'D:/JonNgoStorage/sequioa/R3.2.1/02.02.0050/R3.2.1_seq_factory_dev_02.02.0050.tgz'
#     jbx = JobBundleExtraction()
#     result_jbz, result_manifest = jbx.extract(file_to_extract)
#     if result_manifest is None:
#         print('No manifest file found')
