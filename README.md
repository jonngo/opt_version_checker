# OPT VERSION CHECKER
Get OPT version from different sources.

git clone https://github.com/jonngo/opt_version_checker.git

# IDE Setup
run PyCharm

File > Open > opt_version_checker > OK

File > Settings > Project:opt_version_checker > Project Interpreter > (Choose python 3 interpreter) > OK

Pycharm will create the virtual environment

Go to requirements.txt, Pycharm will ask you to install requirements, choose install.

The main file launcher.py, run this file after setting configurations and other dependencies.

# 7zip
Please install 7zip from https://www.7-zip.org/download.html

# config.json
Some important settings before you run:
#### In the pkg_version_cfg

Replace strikeout with a temporary folder to hold the extracted files
- {"base_xtrak_path":"~~D:/JonNgoStorage/my_hack_project/opt_version_checker/extract/~~"}

Replace strikeout with the full path of the installed 7z.exe
- {"sevenZ_exe":"~~C:/Program Files/7-Zip/7z.exe~~"}


