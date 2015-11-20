# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2015.11
# Email : muyanru345@163.com
###################################################################

from PySide.QtCore import *
from PySide.QtGui import *


REG_RUN = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"

def setAutoStart(is_auto_start):
    # application_name = QApplication.applicationName()
    application_name = 'Arsenal'
    settings = QSettings(REG_RUN, QSettings.NativeFormat)
    if is_auto_start:
        # application_path = QApplication.applicationFilePath()
        application_path = r'Y:\_PIPELINE\_Config\StudioExtra\lib\Arsenal\Arsenal.exe'
        settings.setValue(application_name, application_path.replace("/", "\\"))
    else:
        settings.remove(application_name)


if __name__ == '__main__':
    setAutoStart(True)
    # import sys

    # app = QApplication(sys.argv)
    # test = MMainWindow()
    # test.show()
    # sys.exit(app.exec_())
