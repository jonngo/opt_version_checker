# import os
#
# a="D:/JonNgoStorage/version_checker/xtrak_temp/data/upc_applications_ifm_one_pcd_one_02.02.0023_37545C.pkg".split('/')[-1]
#
# print(os.path.splitext(a)[0])

# b = a.split('/')
#
# print (b[-1])
# # for c in b:
# #     print(c)


# a = 'D:/JonNgoStorage/version_checker/xtrak_level_3/data\apc-pkg-install-dev-su_02.02.0056_9FE3C4\04-firmware.auto\apc_invenco_service_02.02.0023-r0.rpm'
#
# b = a.split('/')
#
# print ("".join(a.split('/')[3:]))
# from jbz_extraction import JobBundleExtraction
# import os
#
# jbx = JobBundleExtraction()
# result = jbx.extract('D:/JonNgoStorage/sequioa/R3.2.1/02.02.0050/R3.2.1_seq_platform_dev_su_02.02.0050.jbz')
# print(result)

# def filenameOnly(f):
#     return os.path.splitext(f.split('/')[-1])[0]

# a = filenameOnly('D:/JonNgoStorage/version_checker/xtrak_level_1/data\\apc-pkg-install-dev-su_02.02.0040_9FE3C4.pkg')
# print (a)


# a = []
# a.append(['a','b'])
# a.append(['1','2'])
#
# a.pop(0)
#
# print(a[0])
# print(a[1])
import re

# a= r"\d{2}.\d{2}.\d{4}"
#
# print (type(a))

# def getVersion(v):
#     match_ver = re.findall(r"\d{2}.\d{2}.\d{4}", v)
#     ret_ver = None
#     try:
#         ret_ver = match_ver[-1]
#         if '.' not in ret_ver:
#             return None
#     except IndexError:
#         print("Invalid match - " + v)
#     return ret_ver
#
# a = [['Package', 'Version'], ['data\\ifm_0_pcd_0_config_00.00.00.0094_23EE23.pkg', '00.00.0094'], ['data\\sdc-kernel-safe_02.02.0032_52AA93.pkg', '02.02.0032'], ['data\\sdc-kernel_02.02.0032_52AA93.pkg', '02.02.0032'], ['data\\sdc_bm_qatest_00.60402.02.0019_52AA93.pkg', '02.02.0019'], ['data\\sdc_rfs_dev_02.02.0023_52AA93.pkg', '02.02.0023'], ['data\\sdc_safe_rfs_dev_02.02.0023_52AA93.pkg', '02.02.0023'], ['data\\sdc_systemassets_00.01.00.0044_294DCD.pkg', '01.00.0044'], ['data\\sdc_tamper_00.02.02.0012_52AA93.pkg', '02.02.0012'], ['data\\upc-kernel-safe_02.02.0032_52AA93.pkg', '02.02.0032'], ['data\\upc-kernel_02.02.0032_52AA93.pkg', '02.02.0032'], ['data\\upc_applications_ifm_one_pcd_zero_02.02.0023_37545C.pkg', '02.02.0023'], ['data\\upc_bm_qatest_00.60402.02.0019_52AA93.pkg', '02.02.0019'], ['data\\upc_generic_plugin_02.02.0023_37545C.pkg', '02.02.0023'], ['data\\upc_rfs_dev_02.02.0023_52AA93.pkg', '02.02.0023'], ['data\\upc_safe_rfs_dev_02.02.0023_52AA93.pkg', '02.02.0023'], ['data\\upc_tamper_00.02.02.0012_52AA93.pkg', '02.02.0012']]
#
# a = [['Package', 'Version'], ['data\\apc-pkg-install-dev-su_02.02.0030_9FE3C4\\04-firmware.auto\\apc_invenco_service_02.02.0014-r0.rpm', '02.02.0014'], ['data\\apc-pkg-install-dev-su_02.02.0030_9FE3C4\\05-middleware.auto\\apc_ics_01.12.0022-r0.rpm', '01.12.0022'], ['data\\apc-pkg-install-dev-su_02.02.0030_9FE3C4\\06-safe-fitimage-dev-02.02.0004.auto\\kernel-fitimage-safe-02.02.0004-r0.invenco_apc.rpm', '02.02.0004'], ['data\\apc-pkg-install-dev-su_02.02.0030_9FE3C4\\07-u-boot-02.02.0004.auto\\u-boot-invenco-apc-02.02.0004-r0.invenco_apc.rpm', '02.02.0004'], ['data\\apc-pkg-install-dev-su_02.02.0030_9FE3C4\\01-install-rootfs-dev-02.02.0004.auto.tar', '02.02.0004'], ['data\\apc-pkg-install-dev-su_02.02.0030_9FE3C4\\06-safe-fitimage-dev-02.02.0004.auto.tar', '02.02.0004'], ['data\\apc-pkg-install-dev-su_02.02.0030_9FE3C4\\07-u-boot-02.02.0004.auto.tar', '02.02.0004'], ['data\\apc_vendor_certs_dev_00.01.01.0018_9FE3C4\\apc-vendor-certificates-01.01.0018-r0.invenco_apc.cpio', '01.01.0018'], ['data\\manifest_00.02.02.0025_9FE3C4\\manifest-02.02.0025-r0.invenco_apc.cpio', '02.02.0025'], ['data\\apc-pkg-install-dev-su_02.02.0030_9FE3C4.pkg', '02.02.0030'], ['data\\apc_vendor_certs_dev_00.01.01.0018_9FE3C4.pkg', '01.01.0018'], ['data\\manifest_00.02.02.0025_9FE3C4.pkg', '02.02.0025'], ['data\\sdc-kernel-safe_02.02.0004_52AA93.pkg', '02.02.0004'], ['data\\sdc-kernel_02.02.0004_52AA93.pkg', '02.02.0004'], ['data\\sdc_bm_dev_02.02.0003_52AA93.pkg', '02.02.0003'], ['data\\sdc_rfs_dev_02.02.0014_52AA93.pkg', '02.02.0014'], ['data\\sdc_safe_rfs_dev_02.02.0014_52AA93.pkg', '02.02.0014'], ['data\\sdc_systemassets_01.00.0026_294DCD.pkg', '01.00.0026'], ['data\\sdc_tamper_02.02.0001_52AA93.pkg', '02.02.0001'], ['data\\upc-kernel-safe_02.02.0004_52AA93.pkg', '02.02.0004'], ['data\\upc-kernel_02.02.0004_52AA93.pkg', '02.02.0004'], ['data\\upc_applications_00.02.02.0014_37545C.pkg', '02.02.0014'], ['data\\upc_applications_g6300_00.02.02.0014_37545C.pkg', '02.02.0014'], ['data\\upc_applications_legacy_00.02.02.0014_37545C.pkg', '02.02.0014'], ['data\\upc_bm_dev_02.02.0003_52AA93.pkg', '02.02.0003'], ['data\\upc_generic_plugin_00.02.02.0014_37545C.pkg', '02.02.0014'], ['data\\upc_rfs_dev_02.02.0014_52AA93.pkg', '02.02.0014'], ['data\\upc_safe_rfs_dev_02.02.0014_52AA93.pkg', '02.02.0014'], ['data\\upc_tamper_02.02.0001_52AA93.pkg', '02.02.0001']]
#
# #get version
#
# for i in a:
#     pkg_name1 = i[0]
#     index_to = pkg_name1.rfind('\\')
#     if index_to != -1:
#         pkg_name2 = pkg_name1[index_to:]
#         print(pkg_name2)
#         # index_from = pkg_name2.rfind('_')
#         # if index_from != -1:
#         #     pkg_name3 = pkg_name2[(index_from+1):]
#
#
# a = 'name = "opt.platform.ver";'
# b = a.split('"')
# print (b[1])

import pandas as pd

a= 'D:/JonNgoStorage/version_checker/xtrak_level_3/data\manifest_02.02.0050_9FE3C4\manifest-02.02.0050-r0.invenco_apc\cfg\secure\manifests\platform\manifest.mnf'

pd.read_json(a)



# try:
#     with open(a, 'r') as f:
#         x = f.readlines()
# except(IOError):
#     print('IOError')
# except(ValueError):
#     print('ValueError')

# m = []
#
# for i in x:
#     if 'version' in i or 'name' in i:
#         m.append(i.strip())

# print(x)

# m = [i.strip() for i in x if 'version' in i or 'name' in i]
#
# v = []
# n = []
#
# for t in m:
#     if t.startswith('version'):
#         v.append(t)
#     if t.startswith('name'):
#         n.append(t)
#
# v.pop(0)
#
# manifest = []
#
# for c in range(0,len(v)):
#     manifest.append([n[c].split('"')[1],v[c].split('"')[1]])
# print(manifest)