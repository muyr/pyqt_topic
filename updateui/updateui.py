# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2015.11
# Email : muyanru345@163.com
###################################################################
from PySide.QtCore import *
from PySide.QtGui import *
import time

class MTaskThread(QThread):
    def __init__(self):
        super(MTaskThread, self).__init__()
        self.stop = False

    def setTaskDetail(self, dataDict):
        self.taskDataDict = dataDict

    def run(self):
        self.emit(SIGNAL('begin()'))
        for i in range(self.taskDataDict['count']):
            while(self.stop):
                self.emit(SIGNAL('showMessage(QString)'), u'=======\n暂停中...\n=======')
                time.sleep(1)
            time.sleep(1)
            self.emit(SIGNAL('showMessage(QString)'), u'【第 %s 次打印】: %s' % (i,self.taskDataDict['content']))

class MTaskWidget(QWidget):
    def __init__(self, parent = None):
        super(MTaskWidget, self).__init__(parent)
        self.resultText = ''
        self.initUI()
        self.taskThread = MTaskThread()
        self.connect(self.taskThread, SIGNAL('showMessage(QString)'), self.updateResultTextEdit)
        self.connect(self.taskThread, SIGNAL('showErrorDialog(QString)'), self.slotShowErrorDialog)
        self.connect(self.taskThread, SIGNAL('begin()'), self.slotBeginRun)
        self.connect(self.taskThread, SIGNAL('finished()'), self.slotFinish)

 ######   ##     ## ####
##    ##  ##     ##  ##
##        ##     ##  ##
##   #### ##     ##  ##
##    ##  ##     ##  ##
##    ##  ##     ##  ##
 ######    #######  ####

    def initUI(self):
        countLabel = QLabel(u'打印次数:')
        self.countSpinBox = QSpinBox()
        self.countSpinBox.setValue(100)
        self.countSpinBox.setMinimum(1)
        contentLabel = QLabel(u'打印内容')
        self.contentLineEdit = QLineEdit('test')

        lay1 = QGridLayout()
        lay1.addWidget(countLabel, 0, 0)
        lay1.addWidget(self.countSpinBox, 0, 1)
        lay1.addWidget(contentLabel, 1, 0)
        lay1.addWidget(self.contentLineEdit, 1, 1)

        self.runButton = QPushButton(u'执行')
        self.runButton.setEnabled(True)
        self.connect(self.runButton, SIGNAL('clicked()'), self.slotRun)

        self.stopButton = QPushButton(u'暂停')
        self.stopButton.setEnabled(False)
        self.connect(self.stopButton, SIGNAL('clicked()'), self.slotStop)

        buttonLay = QHBoxLayout()
        buttonLay.addWidget(self.runButton)
        buttonLay.addWidget(self.stopButton)

        self.resultTextEdit = QTextEdit()
        self.resultTextEdit.ensureCursorVisible()
        self.resultTextEdit.setDocument(QTextDocument(''))

        mainLay = QVBoxLayout()
        mainLay.addLayout(lay1)
        mainLay.addWidget(self.resultTextEdit)
        mainLay.addLayout(buttonLay)

        self.setLayout(mainLay)

    def updateResultTextEdit(self, content):
        self.resultText = self.resultText + content + '\n'
        self.resultTextEdit.setDocument(QTextDocument(self.resultText))
        self.resultTextEdit.moveCursor(QTextCursor.End)

    def clearResultTextEdit(self):
        self.resultText = ''
        self.resultTextEdit.setDocument(QTextDocument(self.resultText))

    def slotBeginRun(self):
        self.runButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.clearResultTextEdit()

    def slotFinish(self):
        QMessageBox.information(self, u'恭喜', u'任务完成！')
        self.runButton.setEnabled(True)
        self.stopButton.setEnabled(False)

    def slotShowErrorDialog(self, content):
        QMessageBox.critical(self, u'出事儿啦', content)

    def slotStop(self):
        if self.taskThread.stop:
            self.taskThread.stop = False
            self.stopButton.setText(u'暂停')
        else:
            self.taskThread.stop = True
            self.stopButton.setText(u'继续')

    def slotRun(self):
        dataDict = {'count':self.countSpinBox.value(), 'content':self.contentLineEdit.text()}
        self.taskThread.setTaskDetail(dataDict)
        self.taskThread.start()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    test = MTaskWidget()
    test.show()
    sys.exit(app.exec_())
