# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.11
# Email : muyanru345@163.com
###################################################################

try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    import sip
    sip.setapi("QString",  2)
    sip.setapi("QVariant",  2)
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

import sys
(LANG_ZH, LANG_EN) = range(2)


class MAbout(QDialog):
    def __init__(self, parent = None):
        super(MAbout, self).__init__(parent)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(QSize(100, 50))
        mainLay = QVBoxLayout()
        mainLay.addWidget(self.label)
        self.setLayout(mainLay)
        self.displayContentText()

    def displayContentText(self):
        self.setWindowTitle(self.tr('dialogTitle'))
        self.label.setText(self.tr('IamSubDialog'))

    def changeEvent(self, event):
        if event.type() == QEvent.LanguageChange:
            self.displayContentText()
        else:
            QWidget.changeEvent(self, event)
        
class MMainWindow(QWidget):
    def __init__(self, translator, parent = None):
        super(MMainWindow, self).__init__(parent)
        self.translator = translator
        
        self.but1 = QPushButton()
        self.but2 = QPushButton()
        self.connect(self.but2, SIGNAL('clicked(bool)'), self.about)
        self.lab1 = QLabel()
        self.lab2 = QLabel()
        
        # 这里不需要翻译，每种语言用对应的语言显示
        langCombo = QComboBox()
        langCombo.addItem(('简体中文').decode('gbk'))
        langCombo.addItem('English')
        self.connect(langCombo, SIGNAL('currentIndexChanged(int)'), self.setLanguage)
        
        mainLay = QVBoxLayout()
        mainLay.addWidget(self.lab1)
        mainLay.addWidget(self.but1)
        mainLay.addWidget(self.but2)
        mainLay.addWidget(langCombo)
        self.setLayout(mainLay)
        
    def setLanguage(self, language = None):
        if language == LANG_ZH:
            self.translator.load("./main_translator_cn.qm")
        elif language == LANG_EN:
            self.translator.load("./main_translator_en.qm")
        else:
            self.translator.load("./main_translator_cn.qm")
        
    def about(self):
        about = MAbout(self)
        about.show()

    def displayContentText(self):
        self.setWindowTitle(self.tr('mainTitle'))
        self.but1.setText(self.tr('button1'))
        self.but2.setText(self.tr('subDialog'))
        self.lab1.setText(self.tr('label1'))

    def changeEvent(self, event):
        if event.type() == QEvent.LanguageChange:
            self.displayContentText()
        else:
            QWidget.changeEvent(self, event)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    traslator_en = QTranslator()
    app.installTranslator(traslator_en)
    
    test = MMainWindow(traslator_en)
    test.setLanguage(LANG_ZH)
    test.show()
    sys.exit(app.exec_())