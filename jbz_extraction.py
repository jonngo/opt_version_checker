import os
import re
import shutil

from texttable import Texttable
from subprocess import Popen,PIPE

class JobBundleExtraction:
    def __init__(self):
        self.base_xtrak_path = "D:/JonNgoStorage/version_checker/"
        self.sevenZ_exe = "C:/Program Files/7-Zip/7z.exe"
        self.xtrak_path1 = self.base_xtrak_path + "xtrak_level_1/"
        self.xtrak_path2 = self.base_xtrak_path + "xtrak_level_2/"
        self.xtrak_path3 = self.base_xtrak_path + "xtrak_level_3/"
        self.manifest_file = "manifest.mnf"
        self.regexp_string = r"\d{2}.\d{2}.\d{4}"
        try:
            shutil.rmtree(self.xtrak_path1)
            shutil.rmtree(self.xtrak_path2)
            shutil.rmtree(self.xtrak_path3)
        except:
            print('Error while deleting directory')

    def filenameOnly(self,f):
        print ('filenameonly')
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

    def extract(self, jbz_file):
        # Level 1 extraction
        process = Popen([self.sevenZ_exe, "x", jbz_file, "-o" + self.xtrak_path1, "*"], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        s = stdout.decode("utf-8")
        print(s)
        #filter all pkg
        # pkg_list = [os.path.join(root,name) for root, dirs, files in os.walk(self.xtrak_path1) for name in files if os.path.join(root, name).endswith(".pkg")]
        pkg_list = [os.path.join(root,name) for root, dirs, files in os.walk(self.xtrak_path1) for name in files]

        #Level 2 extraction
        for p in pkg_list:
            print (p)

            process = Popen([self.sevenZ_exe,"x",p,"-o"+self.xtrak_path2+self.filenameOnly(p)+"/","*"], stdout=PIPE, stderr=PIPE)
            #process = Popen([self.sevenZ_exe, "x", p, "-o" + self.xtrak_path2 + (os.path.splitext(p.split('/')[-1])[0]) + "/", "*"], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()

            s = stdout.decode("utf-8")
            print(s)
            print("-"*150)

        #filter all tar and cpio
        # pkg_list = [os.path.join(root,name) for root, dirs, files in os.walk(self.xtrak_path2) for name in files if os.path.join(root,name).endswith(".tar") or os.path.join(root,name).endswith(".cpio")]
        pkg_list = [os.path.join(root,name) for root, dirs, files in os.walk(self.xtrak_path2) for name in files]

        #Level 3 extraction
        for p in pkg_list:
            print (p)

            process = Popen([self.sevenZ_exe,"x",p,"-o"+self.xtrak_path3+self.filenameOnly(p)+"/","*"], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()

            s = stdout.decode("utf-8")
            print(s)
            print("-"*150)

        master_pkg_list = []
        master_pkg_list.append(['Package','Version'])

        all_xtrak = [self.xtrak_path3,self.xtrak_path2,self.xtrak_path1]

        for x in all_xtrak:
            print(x)
            for root, dirs, files in os.walk(x):
                for name in files:
                    v = self.getVersion(name)
                    print(v)
                    if v is not None:
                        # master_pkg_list.append(["".join(os.path.join(root, name).split('/')[4:]),v])
                        master_pkg_list.append([name, v])

        #Find manifest file

        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_cols_dtype(['t', 't'])  # text
        table.set_cols_width([180, 20])

        table.set_cols_align(["l", "l"])
        table.add_rows(master_pkg_list)
        print(table.draw())

        for x in all_xtrak:
            for root, dirs, files in os.walk(x):
                for name in files:
                    if self.manifest_file in name:
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

        return master_pkg_list, manifest

