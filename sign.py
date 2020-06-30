#!/usr/bin/env python
# sign a binary, rpm, or package for delivery to the G7
#
# If Packman fails to sign the package with the error like
# "java.security.InvalidKeyException: Illegal key size" it is most likely
# caused because the default 128-bit encryption for java is currently
# installed on the host. To overcome this error, install the
# "Java Cryptography Extension (JCE) Unlimited Strength" files. They are downloaded
# in zip format and need to be unzipped/copied to ${java.home}/jre/lib/security/
# Java 6: http://www.oracle.com/technetwork/java/javase/downloads/jce-6-download-429243.html
# Java 7: http://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html
# Java 8: http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html
#
import argparse
import package
import sys

# define option command line paramaters that are supported by this build script
parser = argparse.ArgumentParser(description = 'Sign a G7 binary or package.')
parser.add_argument('--header', required=False, default='7', help='Define the header version type (6 or 7).')
parser.add_argument('-i', '--input', required=True, default='', help='Define the file or package to sign.')
parser.add_argument('-j', '--job', required=False, default='', help='Define the job bundle properties file.')
parser.add_argument('-o', '--output', required=False, default='', help='Define the output filename.')
parser.add_argument('-t', '--type', required=True, help='define the package type (required).')
parser.add_argument('-v', '--version', required=True, default='', help='Build version number (required).')
args = parser.parse_args()

sys.exit(package.sign(args.header, args.input, args.output, args.type, args.version, job = args.job))
