# PyQt4使用Translator

## 代码准备

在代码中我们要把需要翻译的字符串位置使用self.tr()括起来

在每个类中，重载changeEvent事件

<pre><code class="python">
class MyWidget(QWidget):
    def __init__(self, parent = None):
        super(MyWidget, self).__init__(parent)
        # 创建子控件
        self.label = QLabel
        # ...
        # 布局啥的略去了
        
        # 初始化时调用一下
        self.updateContentText()
        
    # 函数名字自取
    def updateContentText(self):
        # 使用self.tr()
        self.label.setText(self.tr('some text'))
        # ...

    def changeEvent(self, event):
        if event.type() == QEvent.LanguageChange:
            # 更新类中所有显示字符串widget的内容
            self.updateContentText()
        else:
            QWidget.changeEvent(self, event)
</code></pre>

当系统安装的translator发生变化时，就会触发changeEvent，
同时事件类型为QEvent.LanguageChange，调用类的刷新显示字符串的函数

## ts文件和qm文件
我们使用PyQt4提供的 pylupdate4 程序来提取并生产.ts文件

<pre><code class="shell">
pylupdate4 -verbose *.py -ts translator_cn.ts
pylupdate4 -verbose *.py -ts translator_en.ts
</code></pre>

我们需要几种语言就生成几个.ts文件，这时候，生成的.ts文件内容是一样

现在打开 Linguist 程序（PyQt4安装目录下的bin文件夹中），打开上述生成的ts文件们，
指定每个ts的目标语言。然后设定每个识别到的字符串对应的两种翻译内容。

设置完毕保存之后，执行菜单File > Release All，将两个ts文件编译为同名的.qm文件

## 动态切换语言
在程序的入口函数中，创建并安装QTranslator

<pre><code class="python">

(LANG_ZH, LANG_EN) = range(2) # language type

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 新建个QTranslator
    traslator = QTranslator()
    # 程序安装该translator
    app.installTranslator(traslator)
    
    test = MMainWindow(traslator)
    # 设置默认的语言
    test.setLanguage(LANG_ZH)
    test.show()
    sys.exit(app.exec_())
</code></pre>

在主widget中，创建一个QComboBox来让用户选择要切换的语言列表
当QComboBox选中的item发生修改（语言切换）时，调用一个让translator加载对应语言的qm文件的函数
这样就会触发主widget及其各种子widget的changeEvent，同时事件类型为QEvent.LanguageChange，会让每个widget都更新了语言
<pre><code class="python">
class MMainWidget(QWidget):
    def __init__(self, translator, parent = None):
        super(MMainWindow, self).__init__(parent)
        self.translator = translator
        # ...
        
        # 这里不需要翻译，每种语言用对应的语言显示
        langCombo = QComboBox()
        langCombo.addItem(('简体中文').decode('gbk'))
        langCombo.addItem('English')
        self.connect(langCombo, SIGNAL('currentIndexChanged(int)'), self.setLanguage)
        
        # 其他widget部件以及布局略去

    def setLanguage(self, language = None):
        if language == LANG_ZH:
            self.translator.load("./main_translator_cn.qm")
        elif language == LANG_EN:
            self.translator.load("./main_translator_en.qm")
        else:
            self.translator.load("./main_translator_cn.qm")
</code></pre>


