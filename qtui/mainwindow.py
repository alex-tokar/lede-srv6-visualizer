# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qtui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.startPingButton = QtWidgets.QPushButton(self.centralwidget)
        self.startPingButton.setObjectName("startPingButton")
        self.verticalLayout_2.addWidget(self.startPingButton)
        self.stopPingButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopPingButton.setObjectName("stopPingButton")
        self.verticalLayout_2.addWidget(self.stopPingButton)
        self.installRouteButton = QtWidgets.QPushButton(self.centralwidget)
        self.installRouteButton.setObjectName("installRouteButton")
        self.verticalLayout_2.addWidget(self.installRouteButton)
        self.uninstallRouteButton = QtWidgets.QPushButton(self.centralwidget)
        self.uninstallRouteButton.setObjectName("uninstallRouteButton")
        self.verticalLayout_2.addWidget(self.uninstallRouteButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SRv6 Visualizer"))
        self.startPingButton.setText(_translate("MainWindow", "Start Ping"))
        self.stopPingButton.setText(_translate("MainWindow", "Stop Ping"))
        self.installRouteButton.setText(_translate("MainWindow", "Install SRv6 route via Netconf"))
        self.uninstallRouteButton.setText(_translate("MainWindow", "Uninstall SRv6 route via Netconf"))

