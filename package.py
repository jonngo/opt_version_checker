#!/usr/bin/env python
""" sign a binary, rpm, or package for delivery to the G7

 If Packman fails to sign the package with the error like
 "java.security.InvalidKeyException: Illegal key size" it is most likely
 caused because the default 128-bit encryption for java is currently
 installed on the host. To overcome this error, install the
 "Java Cryptography Extension (JCE) Unlimited Strength" files. They are downloaded
 in zip format and need to be unzipped/copied to ${java.home}/jre/lib/security/
 Java 6: http://www.oracle.com/technetwork/java/javase/downloads/jce-6-download-429243.html
 Java 7: http://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html
 Java 8: http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html
"""

import os
import re
import subprocess
import sys
import json
import struct
import argparse
from ctypes import *

# record path to this directory and the signature profiles and packages contained within
workspace = os.path.dirname(os.path.abspath(__file__))

assets_unused_v255 = (
    "upcbootenv",
    "sdcbootenv",
    "upcsystemassets",
    "apcasset",
    "sdcapplications",
    "apcapplications",
    "apcremoverpm",
    "sdcsecureconfig",
    "upcsecureconfig"
)

def print_error(message):
    sys.stderr.write("error: " + message + "\n")

def print_info(message):
    sys.stdout.write(message + "\n")

def run_cmdline(cmdline):
    process = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = process.communicate()
    stdout = stdoutdata.decode("utf-8")
    stderr = stderrdata.decode("utf-8")
    return (process.returncode, stdout, stderr)

def load_json(path):
    if not os.path.exists(path):
        print_error(path + " not found!")
        return None

    data = None
    try:
        with open(path) as data_file:
            data = json.load(data_file)
    except Exception as exception:
        print_error("unable to load '" + path + "' " + str(exception).strip())
        return None
    return data


def read_pkg_name_from_rpm(rpm):
    (ret, stdout, stderr) = run_cmdline(["rpm", "--queryformat=%{NAME}", "-qp", rpm])
    if ret == 0:
        return stdout
    else:
        print_error("\n" + stderr)
        return None


def get_profile_fingerprint_from_key_index(key_index, key_name):
    for profile in key_index["profiles"]:
        if profile["name"] == key_name:
            return profile["key"]["fingerprint"]
    return None


def is_valid_pci_version(pci_version):
    pattern = re.compile(r"^\d{2}.\d{2}.\d{4}$")
    return bool(pattern.match(pci_version))


def pci_version_using_version_build_number(pci_version, version):
    """
    Return the PCI version, but using the build number extracted from the version string
    """
    build_number = version.split(".")[-1]
    return pci_version + "." + build_number


class AssetInfo:
    """
    Class for holding all important asset info information

    pci_version and common_name can be None
    """
    def __init__(self, sign_type, key_name, pkg_name, security_version, pci_version, common_name):
        # Mandatory for v255 and v1 packages
        self.sign_type = sign_type
        self.key_name = key_name

        # Mandatory for v255 packages
        self.pkg_name = pkg_name
        self.security_version = security_version

        # Optional
        self.pci_version = pci_version
        self.common_name = common_name


def parse_asset_infos(asset_infos, pkg_header_version, infile, stype):
    customisation_index = None
    if "-" in stype:
        sign_type, customisation_index = stype.split("-")
    else:
        sign_type = stype

    if pkg_header_version == "v255" and stype in assets_unused_v255:
        print_error(sign_type + " is not supported in v255")
        return None

    if sign_type not in asset_infos:
        print_error("can not find asset info for " + sign_type)
        return None
    info = asset_infos[sign_type]

    pkg_name = None
    if pkg_header_version == "v255" and "pkg_name" not in info:
        print_error("pkg_name is mandantory for v255")
        return None
    if "pkg_name" in info:
        pkg_name = info["pkg_name"]

    security_version = None
    if pkg_header_version == "v255" and "security_version" not in info:
        print_error("security version is mandantory for v255")
        return None
    if "security_version" in info:
        security_version = info["security_version"]

    if "key_name" not in info:
        print_error("key_name is mandantory")
        return None
    key_name = info["key_name"]

    if customisation_index:
        if "customisation" not in info or customisation_index not in info["customisation"]:
            print_error("need customisation info for " + sign_type + " " + customisation_index)
            return None
        pkg_name = pkg_name + "." + info["customisation"][customisation_index]
    elif "customisation" in info and info["customisation"] == "read_from_rpm":
        rpm_name = read_pkg_name_from_rpm(infile)
        if not rpm_name:
            print_error("fetch RPM name failed for " + sign_type)
            return None
        pkg_name += "." + rpm_name

    pci_version = None
    if "pci_version" in info:
        if not is_valid_pci_version(info["pci_version"]):
            print_error("pci_version must have the form 'major.minor.build_num'")
            return None
        pci_version = info["pci_version"]

    common_name = None
    if "common_name" in info:
        common_name = info["common_name"]

    return AssetInfo(sign_type, key_name, pkg_name, security_version, pci_version, common_name)


def generate_cmdline_v255_pkg(asset_infos, header, stype, infile, outpath, outfile, version):
    asset_info = parse_asset_infos(asset_infos, "v255", infile, stype)
    if asset_info is None:
        return None

    filename_version = version
    if asset_info.pci_version is not None:
        filename_version = pci_version_using_version_build_number(asset_info.pci_version, version)
        version = asset_info.pci_version

    version = asset_info.security_version + "." + version

    key_index = load_json(os.path.join(".", "conf", "index.json"))
    fingerprint = get_profile_fingerprint_from_key_index(key_index, asset_info.key_name)
    if not fingerprint:
        print_error("fingerprint could not be found")
        return None

    outfile = outfile + "_" + filename_version + "_" + fingerprint + ".pkg"

    cmdline = ["java", "-jar", "Packman.jar",
               "-h", header,
               "-t", asset_info.sign_type,
               "-pkg", asset_info.pkg_name,
               "-v", version,
               "-kn", asset_info.key_name,
               "-i", infile,
               "-o", os.path.join(outpath, outfile),
               "-s", "./conf/index.json",
               "-m", "999M",
               "-b", "./base",
               "-l", "./packman.log"]

    if asset_info.common_name is not None:
        cmdline += ["-cn", asset_info.common_name]

    return cmdline

def generate_cmdline_v1_pkg(asset_infos, header, stype, infile, outpath, outfile, extension, version):
    version = correct_debug_variant_version_for_v1(version)

    asset_info = parse_asset_infos(asset_infos, "v1", infile, stype)
    if asset_info is None:
        return None

    filename_version = version
    if asset_info.pci_version is not None:
        filename_version = pci_version_using_version_build_number(asset_info.pci_version, version)
        version = asset_info.pci_version

    key_index = load_json(os.path.join(".", "conf", "index.json"))
    fingerprint = get_profile_fingerprint_from_key_index(key_index, asset_info.key_name)
    if not fingerprint:
        print_error("fingerprint could not be found")
        return None

    outfile = outfile + "_" + filename_version + "_" + fingerprint + ".pkg"

    cmdline = ["java", "-jar", "Packman.jar",
               "-h", header,
               "-t", stype,
               "-i", infile,
               "-o", os.path.join(outpath, outfile),
               "-s", "./conf/index.json",
               "-b", "./base",
               "-l", "./packman.log",
               "-pkg", "pkg_name_v1",
               "-v", version]

    if stype == "p2perootcertificate":
        cmdline += ["-kn", "G7-INV-FW-SEC-AST"]
    if stype == "printerfirmware":
        cmdline += ["-kn", "G7-INV_APC-FW"]
    if stype == "apcconfig":
        cmdline += ["-kn", "G7_FW"]
    if stype == "apcplatformasset":
        cmdline += ["-m", "999M"]

    return cmdline


def correct_debug_variant_version_for_v1(version_string):
    # version_numbers = major.minor.build | XX.YY.ZZZZ
    version_numbers = version_string.split(".")
    major_version = int(version_numbers[0], 10)
    if major_version > 60000:
        major_version %= 100
        version_string = "{:02}.{}.{}".format(major_version, version_numbers[1], version_numbers[2])
    return version_string


def generate_cmdline_v1_generic(header, stype, infile, outpath, outfile, extension, version):
    version = correct_debug_variant_version_for_v1(version)

    cmdline = ["java", "-jar", "Packman.jar",
               "-h", header,
               "-t", stype,
               "-i", infile,
               "-o", outpath,
               "-g",
               "-p", outfile,
               "-s", "./conf/index.json",
               "-b", "./base",
               "-l", "./packman.log",
               "-pkg", "pkg_name_v1",
               "-v", version,
               "-e", extension]

    if stype == "p2perootcertificate":
        cmdline += ["-kn", "G7-INV-FW-SEC-AST"]
    if stype == "printerfirmware":
        cmdline += ["-kn", "G7-INV_APC-FW"]
    if stype == "apcconfig":
        cmdline += ["-kn", "G7_FW"]
    if stype == "apcplatformasset":
        cmdline += ["-m", "999M"]

    return cmdline


def generate_cmdline(asset_info_path, header, stype, infile, outpath, outfile, extension, version):
    if extension == "jbz" or extension == "bin":
        return generate_cmdline_v1_generic(header, stype, infile, outpath, outfile, extension, version)

    asset_infos = load_json(asset_info_path)

    if header == "6300":
        if asset_infos is None:
            return None
        else:
            return generate_cmdline_v255_pkg(asset_infos, header, stype, infile, outpath, outfile, version)
    else:
        # For a V1 package, it is okay to not have asset info. For backwards compatibility, we fall back
        # to the old way of generating the command line for v1 packages. If there is no pci_version in the asset_info,
        # We can also fall back to the old way.
        if asset_infos is None or stype not in asset_infos:
            return generate_cmdline_v1_generic(header, stype, infile, outpath, outfile, extension, version)
        else:
            return generate_cmdline_v1_pkg(asset_infos, header, stype, infile, outpath, outfile, extension, version)



def sign_asset(header, infile, output, stype, version, job=None, asset_info_path=None):
    """ sign a specific asset """
    if not os.path.exists(infile):
        print_error("input file does not exist")
        return 1
    # to make Packman work, need to change to it"s current directory.
    # this means if the input or output paths are relative, then need to be absolute otherwise
    # they won't be found. Also if operating within cygwin, change the path to windows format
    # so the windows and cygwin Java installations are supported.
    infile = re.sub(r"^/cygdrive/(\w)/", r"\g<1>:/", os.path.abspath(infile))
    extension = "jbz" if "jobbundle" in stype.lower() else "bin" if header == "6" else "pkg"
    if output == "":
        # output filename was not supplied, therefore use output name based on input and change suffix to .bin
        outpath = re.sub(r"^/cygdrive/(\w)/", r"\1:/", os.path.dirname(os.path.abspath(infile)))
        # if input file already has a .bin filename suffix, so remove it and version
        # as packman will add both
        outfile = re.sub(r"(-+|_+|-+r\d+|_+r\d+)$", "", re.sub(r"\d+(-|_|\.)\d+(-|_|\.)[\d\-_\.]+",
                         "", re.sub(r"\.(bin|pkg|rpm|sbin|tar|uboot)$", "", os.path.basename(infile))))
    elif os.path.isdir(output):
        # output is a directory name, therefore add the output filename
        outfile = re.sub(r"(-+|_+|-+r\d+|_+r\d+)$", "", re.sub(r"\d+(-|_|\.)\d+(-|_|\.)[\d\-_\.]+",
                         "", re.sub(r"\.(bin|pkg|rpm|sbin|tar|uboot)$", "", os.path.basename(infile))))
        outpath = re.sub(r"^/cygdrive/(\w)/", r"\g<1>:/", os.path.abspath(output))
    else:
        # if desired output filename definition already has a .bin filename suffix or version number
        # as packman will add both
        outfile = re.sub(r"(-+|_+|-+r\d+|_+r\d+)$", "", re.sub(r"\d+(-|_|\.)\d+(-|_|\.)[\d\-_\.]+",
                         "", re.sub(r"\.(bin|pkg|rpm|sbin|tar|uboot)$", "", os.path.basename(output))))
        outpath = re.sub(r"^/cygdrive/(\w)/", r"\g<1>:/", os.path.dirname(os.path.abspath(output)))
    # re.sub does non overlapping string matching, so won't repeat check the same string
    # so need to do it again so don't end up with a double dash or underscore in final filename
    outfile = re.sub(r"(-+|_+|-+r\d+|_+r\d+)$", "", outfile)
    if not os.path.exists(os.path.join(workspace, "base")):
        os.mkdir(os.path.join(workspace, "base"))
    if os.path.exists(os.path.join(outpath, outfile)):
        # ensure the output file does not exist prior to sign effort, in case retrying
        # especially since we need to test for the files existance afterwards as a test
        # for success or failure
        os.remove(os.path.join(outpath, outfile))
    os.chdir(workspace)


    if asset_info_path is None or asset_info_path == "":
        asset_info_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(workspace))), "asset_info.json")

    cmdline = generate_cmdline(asset_info_path, header, stype, infile, outpath, outfile, extension, version)
    if not cmdline:
        return 1

    cmdline += ["-j", re.sub(r"^/cygdrive/(\w)/", r"\g<1>:/", os.path.abspath(job))] if job else []
    print_info(" ".join(cmdline))

    (result, stdout, stderr) = run_cmdline(cmdline)
    print_info(stdout)

    if result == 0:
        # confirm success or failure based on if the output file exists
        result = 1
        for file in os.listdir(outpath):
            if not re.search("^" + re.escape(outfile), file) is None:
                result = 0
                break
    if result != 0:
        print_error("\nsign error: could not find " + outfile + "in " + outpath + "!\n" + stderr)
    return result


def sign(header, infile, output, stype, version, job=None):
    return sign_asset(header, infile, output, stype, version, job=job)


def peek_u32(f):
    """ Read a u32 from a byte file without advancing the file cursor """
    u32 = f.read(4)
    f.seek(-4, 1)
    return struct.unpack("<I", u32)[0]

def to_hex_string(fingerprint):
    return "".join(["{:02X}".format(u8) for u8 in fingerprint])

class PackageHeaderV255(LittleEndianStructure):
    _fields_ = [
            ("packageVersion",       c_uint32),
            ("headerLength",         c_uint32),
            ("payloadLength",        c_uint32),
            ("assetType",            c_uint32),
            ("packageName",          c_char * 32),
            ("obfuscationAlgorithm", c_uint32),
            ("keyFingerprint",       c_uint8 * 3),
            ("operation",            c_uint8),
            ("commonName",           c_char * 32),
            ("securityVersion",      c_uint16),
            ("majorVersion",         c_uint16),
            ("minorVersion",         c_uint16),
            ("buildVersion",         c_uint16),
            ]

    def __str__(self):
        string = ("uint32_t packageVersion       = {}\n"
                  "uint32_t headerLength         = {}\n"
                  "uint32_t payloadLength        = {}\n"
                  "uint32_t assetType            = {}\n"
                  "char     packageName[32]      = \"{}\"\n"
                  "uint32_t obfuscationAlgorithm = {}\n"
                  "uint8_t  keyFingerprint[3]    = {} ({})\n"
                  "uint8_t  operation            = {}\n"
                  "char     commonName[32]       = \"{}\"\n"
                  "uint16_t securityVersion      = {}\n"
                  "uint16_t majorVersion         = {}\n"
                  "uint16_t minorVersion         = {}\n"
                  "uint16_t buildVersion         = {}"
                  ).format(self.packageVersion,
                self.headerLength,
                self.payloadLength,
                self.assetType,
                self.packageName.decode(),
                self.obfuscationAlgorithm,
                list(self.keyFingerprint),
                to_hex_string(self.keyFingerprint),
                self.operation,
                self.commonName.decode(),
                self.securityVersion,
                self.majorVersion,
                self.minorVersion,
                self.buildVersion)
        return string

    def version_string(self):
        return "{:02}.{:02}.{:04}".format(self.majorVersion, self.minorVersion, self.buildVersion)

class PackageHeaderV1(LittleEndianStructure):
    _fields_ = [
            ("packageVersion",       c_uint32),
            ("headerLength",         c_uint32),
            ("payloadLength",        c_uint32),
            ("assetType",            c_uint32),
            ("assetVersion",         c_char * 40),
            ("signatureAlgorithm",   c_uint32),
            ("obfuscationAlgorithm", c_uint32),
            ("keyFingerprint",       c_uint8 * 4),
            ]

    def __str__(self):
        string = ("uint32_t packageVersion       = {}\n"
                  "uint32_t headerLength         = {}\n"
                  "uint32_t payloadLength        = {}\n"
                  "uint32_t assetType            = {}\n"
                  "char     assetVersion[40]     = \"{}\"\n"
                  "uint32_t signatureAlgorithm   = {}\n"
                  "uint32_t obfuscationAlgorithm = {}\n"
                  "uint8_t  keyFingerprint[4]    = {} ({})"
                  ).format(self.packageVersion,
                self.headerLength,
                self.payloadLength,
                self.assetType,
                self.assetVersion.decode(),
                self.signatureAlgorithm,
                self.obfuscationAlgorithm,
                list(self.keyFingerprint),
                to_hex_string(self.keyFingerprint[1:]))
        return string

    def version_string(self):
        return self.assetVersion

def print_pkg_header():
    parser = argparse.ArgumentParser("package")
    parser.add_argument("pkg_filename", type=str, help="The filename of the package to be examined", action="store")

    if not len(sys.argv) == 2:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    with open(args.pkg_filename, "rb") as f:
        if peek_u32(f) == 1:
            header = PackageHeaderV1()
            f.readinto(header)
        elif peek_u32(f) == 255:
            header = PackageHeaderV255()
            f.readinto(header)
        else:
            sys.exit("Could not recognise package version of '{}'".format(peek_u32(f)))

    print(header)

def header_info(pkg_filename):
    with open(pkg_filename, "rb") as f:
        if peek_u32(f) == 1:
            header = PackageHeaderV1()
            f.readinto(header)
        elif peek_u32(f) == 255:
            header = PackageHeaderV255()
            f.readinto(header)
        else:
            # sys.exit("Could not recognise package version of '{}'".format(peek_u32(f)))
            return "Could not recognise package version of '{}'".format(peek_u32(f))
    return header

def version_num(pkg_filename):
    with open(pkg_filename, "rb") as f:
        if peek_u32(f) == 1:
            header = PackageHeaderV1()
            f.readinto(header)
        elif peek_u32(f) == 255:
            header = PackageHeaderV255()
            f.readinto(header)
        else:
            # sys.exit("Could not recognise package version of '{}'".format(peek_u32(f)))
            return "Could not recognise package version of '{}'".format(peek_u32(f))
    return header.version_string()

if __name__ == "__main__":
    print_pkg_header()
