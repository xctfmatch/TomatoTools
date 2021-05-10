# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\user\Desktop\CTFMiscTools\CTF密码学工具\GUI\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 454)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralWidget)
        self.mdiArea.setGeometry(QtCore.QRect(45, 30, 581, 341))
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setAutoFillBackground(True)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actDoc_New = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/GUI/images/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actDoc_New.setIcon(icon)
        self.actDoc_New.setObjectName("actDoc_New")
        self.actAbout = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/GUI/images/11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actAbout.setIcon(icon1)
        self.actAbout.setObjectName("actAbout")
        self.actDoc_Open = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/GUI/images/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actDoc_Open.setIcon(icon2)
        self.actDoc_Open.setObjectName("actDoc_Open")
        self.actEdit_Font = QtWidgets.QAction(MainWindow)
        self.actEdit_Font.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/GUI/images/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Font.setIcon(icon3)
        self.actEdit_Font.setObjectName("actEdit_Font")
        self.actCipher_Analyse = QtWidgets.QAction(MainWindow)
        self.actCipher_Analyse.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/GUI/images/4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actCipher_Analyse.setIcon(icon4)
        self.actCipher_Analyse.setObjectName("actCipher_Analyse")
        self.actAuto_Flag = QtWidgets.QAction(MainWindow)
        self.actAuto_Flag.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/GUI/images/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actAuto_Flag.setIcon(icon5)
        self.actAuto_Flag.setObjectName("actAuto_Flag")
        self.actCipher_Plug = QtWidgets.QAction(MainWindow)
        self.actCipher_Plug.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/GUI/images/6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actCipher_Plug.setIcon(icon6)
        self.actCipher_Plug.setObjectName("actCipher_Plug")
        self.actMDI_Mode = QtWidgets.QAction(MainWindow)
        self.actMDI_Mode.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/GUI/images/8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actMDI_Mode.setIcon(icon7)
        self.actMDI_Mode.setObjectName("actMDI_Mode")
        self.actMDI_Cascade = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/GUI/images/9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actMDI_Cascade.setIcon(icon8)
        self.actMDI_Cascade.setObjectName("actMDI_Cascade")
        self.actMDI_Tile = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/GUI/images/10.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actMDI_Tile.setIcon(icon9)
        self.actMDI_Tile.setObjectName("actMDI_Tile")
        self.actDoc_CloseALL = QtWidgets.QAction(MainWindow)
        self.actDoc_CloseALL.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/GUI/images/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actDoc_CloseALL.setIcon(icon10)
        self.actDoc_CloseALL.setObjectName("actDoc_CloseALL")
        self.mainToolBar.addAction(self.actDoc_New)
        self.mainToolBar.addAction(self.actDoc_Open)
        self.mainToolBar.addAction(self.actDoc_CloseALL)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actCipher_Analyse)
        self.mainToolBar.addAction(self.actAuto_Flag)
        self.mainToolBar.addAction(self.actCipher_Plug)
        self.mainToolBar.addAction(self.actEdit_Font)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actMDI_Mode)
        self.mainToolBar.addAction(self.actMDI_Cascade)
        self.mainToolBar.addAction(self.actMDI_Tile)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actAbout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TomatoTools 「by Randall」"))
        self.actDoc_New.setText(_translate("MainWindow", "新建"))
        self.actDoc_New.setToolTip(_translate("MainWindow", "新建窗口(Ctrl+N)"))
        self.actDoc_New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actAbout.setText(_translate("MainWindow", "关于"))
        self.actAbout.setToolTip(_translate("MainWindow", "程序的详细信息"))
        self.actDoc_Open.setText(_translate("MainWindow", "打开"))
        self.actDoc_Open.setToolTip(_translate("MainWindow", "打开文档(Ctrl+O)"))
        self.actDoc_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actEdit_Font.setText(_translate("MainWindow", "字体设置"))
        self.actEdit_Font.setToolTip(_translate("MainWindow", "字体设置"))
        self.actCipher_Analyse.setText(_translate("MainWindow", "密文分析"))
        self.actCipher_Analyse.setToolTip(_translate("MainWindow", "密文分析(Ctrl+Q)"))
        self.actCipher_Analyse.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actAuto_Flag.setText(_translate("MainWindow", "自动提flag"))
        self.actAuto_Flag.setToolTip(_translate("MainWindow", "自动提flag(Ctrl+F)"))
        self.actAuto_Flag.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actCipher_Plug.setText(_translate("MainWindow", "插件"))
        self.actCipher_Plug.setToolTip(_translate("MainWindow", "插件(Ctrl+G)"))
        self.actCipher_Plug.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actMDI_Mode.setText(_translate("MainWindow", "MDI模式"))
        self.actMDI_Mode.setToolTip(_translate("MainWindow", "窗口模式或页面模式(Ctrl+M)"))
        self.actMDI_Mode.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actMDI_Cascade.setText(_translate("MainWindow", "级联展开"))
        self.actMDI_Cascade.setToolTip(_translate("MainWindow", "窗口级联展开(Ctrl+L)"))
        self.actMDI_Cascade.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actMDI_Tile.setText(_translate("MainWindow", "平铺展开"))
        self.actMDI_Tile.setToolTip(_translate("MainWindow", "窗口平铺展开(Ctrl+P)"))
        self.actMDI_Tile.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actDoc_CloseALL.setText(_translate("MainWindow", "关闭全部"))
        self.actDoc_CloseALL.setToolTip(_translate("MainWindow", "关闭所有窗口(Alt+C)"))
        self.actDoc_CloseALL.setShortcut(_translate("MainWindow", "Alt+C"))
import res_rc
