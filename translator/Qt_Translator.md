# PyQt4ʹ��Translator

## ����׼��

�ڴ���������Ҫ����Ҫ������ַ���λ��ʹ��self.tr()������

��ÿ�����У�����changeEvent�¼�

<pre><code class="python">
class MyWidget(QWidget):
    def __init__(self, parent = None):
        super(MyWidget, self).__init__(parent)
        # �����ӿؼ�
        self.label = QLabel
        # ...
        # ����ɶ����ȥ��
        
        # ��ʼ��ʱ����һ��
        self.updateContentText()
        
    # ����������ȡ
    def updateContentText(self):
        # ʹ��self.tr()
        self.label.setText(self.tr('some text'))
        # ...

    def changeEvent(self, event):
        if event.type() == QEvent.LanguageChange:
            # ��������������ʾ�ַ���widget������
            self.updateContentText()
        else:
            QWidget.changeEvent(self, event)
</code></pre>

��ϵͳ��װ��translator�����仯ʱ���ͻᴥ��changeEvent��
ͬʱ�¼�����ΪQEvent.LanguageChange���������ˢ����ʾ�ַ����ĺ���

## ts�ļ���qm�ļ�
����ʹ��PyQt4�ṩ�� pylupdate4 ��������ȡ������.ts�ļ�

<pre><code class="shell">
pylupdate4 -verbose *.py -ts translator_cn.ts
pylupdate4 -verbose *.py -ts translator_en.ts
</code></pre>

������Ҫ�������Ծ����ɼ���.ts�ļ�����ʱ�����ɵ�.ts�ļ�������һ��

���ڴ� Linguist ����PyQt4��װĿ¼�µ�bin�ļ����У������������ɵ�ts�ļ��ǣ�
ָ��ÿ��ts��Ŀ�����ԡ�Ȼ���趨ÿ��ʶ�𵽵��ַ�����Ӧ�����ַ������ݡ�

������ϱ���֮��ִ�в˵�File > Release All��������ts�ļ�����Ϊͬ����.qm�ļ�

## ��̬�л�����
�ڳ������ں����У���������װQTranslator

<pre><code class="python">

(LANG_ZH, LANG_EN) = range(2) # language type

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # �½���QTranslator
    traslator = QTranslator()
    # ����װ��translator
    app.installTranslator(traslator)
    
    test = MMainWindow(traslator)
    # ����Ĭ�ϵ�����
    test.setLanguage(LANG_ZH)
    test.show()
    sys.exit(app.exec_())
</code></pre>

����widget�У�����һ��QComboBox�����û�ѡ��Ҫ�л��������б�
��QComboBoxѡ�е�item�����޸ģ������л���ʱ������һ����translator���ض�Ӧ���Ե�qm�ļ��ĺ���
�����ͻᴥ����widget���������widget��changeEvent��ͬʱ�¼�����ΪQEvent.LanguageChange������ÿ��widget������������
<pre><code class="python">
class MMainWidget(QWidget):
    def __init__(self, translator, parent = None):
        super(MMainWindow, self).__init__(parent)
        self.translator = translator
        # ...
        
        # ���ﲻ��Ҫ���룬ÿ�������ö�Ӧ��������ʾ
        langCombo = QComboBox()
        langCombo.addItem(('��������').decode('gbk'))
        langCombo.addItem('English')
        self.connect(langCombo, SIGNAL('currentIndexChanged(int)'), self.setLanguage)
        
        # ����widget�����Լ�������ȥ

    def setLanguage(self, language = None):
        if language == LANG_ZH:
            self.translator.load("./main_translator_cn.qm")
        elif language == LANG_EN:
            self.translator.load("./main_translator_en.qm")
        else:
            self.translator.load("./main_translator_cn.qm")
</code></pre>


