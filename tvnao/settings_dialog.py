# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 412)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxPlaylist = QtWidgets.QGroupBox(Dialog)
        self.groupBoxPlaylist.setObjectName("groupBoxPlaylist")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxPlaylist)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayoutPlaylist = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPlaylist.setObjectName("horizontalLayoutPlaylist")
        self.verticalLayout0 = QtWidgets.QVBoxLayout()
        self.verticalLayout0.setObjectName("verticalLayout0")
        self.label = QtWidgets.QLabel(self.groupBoxPlaylist)
        self.label.setObjectName("label")
        self.verticalLayout0.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBoxPlaylist)
        self.label_2.setObjectName("label_2")
        self.verticalLayout0.addWidget(self.label_2)
        self.horizontalLayoutPlaylist.addLayout(self.verticalLayout0)
        self.verticalLayout1 = QtWidgets.QVBoxLayout()
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.playlistHost = QtWidgets.QLineEdit(self.groupBoxPlaylist)
        self.playlistHost.setObjectName("playlistHost")
        self.verticalLayout1.addWidget(self.playlistHost)
        self.playlistURL = QtWidgets.QLineEdit(self.groupBoxPlaylist)
        self.playlistURL.setObjectName("playlistURL")
        self.verticalLayout1.addWidget(self.playlistURL)
        self.horizontalLayoutPlaylist.addLayout(self.verticalLayout1)
        self.verticalLayout_2.addLayout(self.horizontalLayoutPlaylist)
        self.verticalLayout.addWidget(self.groupBoxPlaylist)
        self.groupBoxPlayer = QtWidgets.QGroupBox(Dialog)
        self.groupBoxPlayer.setObjectName("groupBoxPlayer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxPlayer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayoutPlayer = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPlayer.setObjectName("horizontalLayoutPlayer")
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.label_3 = QtWidgets.QLabel(self.groupBoxPlayer)
        self.label_3.setObjectName("label_3")
        self.verticalLayout2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBoxPlayer)
        self.label_4.setObjectName("label_4")
        self.verticalLayout2.addWidget(self.label_4)
        self.horizontalLayoutPlayer.addLayout(self.verticalLayout2)
        self.verticalLayout3 = QtWidgets.QVBoxLayout()
        self.verticalLayout3.setObjectName("verticalLayout3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playerPath = QtWidgets.QLineEdit(self.groupBoxPlayer)
        self.playerPath.setObjectName("playerPath")
        self.horizontalLayout.addWidget(self.playerPath)
        self.playerButton = QtWidgets.QPushButton(self.groupBoxPlayer)
        self.playerButton.setText("")
        self.playerButton.setObjectName("playerButton")
        self.horizontalLayout.addWidget(self.playerButton)
        self.verticalLayout3.addLayout(self.horizontalLayout)
        self.playerOptions = QtWidgets.QLineEdit(self.groupBoxPlayer)
        self.playerOptions.setClearButtonEnabled(True)
        self.playerOptions.setObjectName("playerOptions")
        self.verticalLayout3.addWidget(self.playerOptions)
        self.horizontalLayoutPlayer.addLayout(self.verticalLayout3)
        self.verticalLayout_3.addLayout(self.horizontalLayoutPlayer)
        self.playerSingle = QtWidgets.QCheckBox(self.groupBoxPlayer)
        self.playerSingle.setObjectName("playerSingle")
        self.verticalLayout_3.addWidget(self.playerSingle)
        self.verticalLayout.addWidget(self.groupBoxPlayer)
        self.groupBoxGuide = QtWidgets.QGroupBox(Dialog)
        self.groupBoxGuide.setObjectName("groupBoxGuide")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxGuide)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayoutGuide = QtWidgets.QHBoxLayout()
        self.horizontalLayoutGuide.setObjectName("horizontalLayoutGuide")
        self.verticalLayout4 = QtWidgets.QVBoxLayout()
        self.verticalLayout4.setObjectName("verticalLayout4")
        self.label_5 = QtWidgets.QLabel(self.groupBoxGuide)
        self.label_5.setObjectName("label_5")
        self.verticalLayout4.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.groupBoxGuide)
        self.label_7.setObjectName("label_7")
        self.verticalLayout4.addWidget(self.label_7)
        self.horizontalLayoutGuide.addLayout(self.verticalLayout4)
        self.verticalLayout5 = QtWidgets.QVBoxLayout()
        self.verticalLayout5.setObjectName("verticalLayout5")
        self.epgHost = QtWidgets.QLineEdit(self.groupBoxGuide)
        self.epgHost.setObjectName("epgHost")
        self.verticalLayout5.addWidget(self.epgHost)
        self.epgURL = QtWidgets.QLineEdit(self.groupBoxGuide)
        self.epgURL.setObjectName("epgURL")
        self.verticalLayout5.addWidget(self.epgURL)
        self.horizontalLayoutGuide.addLayout(self.verticalLayout5)
        self.verticalLayout_4.addLayout(self.horizontalLayoutGuide)
        self.verticalLayout.addWidget(self.groupBoxGuide)
        self.horizontalLayoutBt = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBt.setObjectName("horizontalLayoutBt")
        self.defaultsButton = QtWidgets.QPushButton(Dialog)
        self.defaultsButton.setObjectName("defaultsButton")
        self.horizontalLayoutBt.addWidget(self.defaultsButton)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutBt.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayoutBt)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "tvnao - settings"))
        self.groupBoxPlaylist.setTitle(_translate("Dialog", "Playlist"))
        self.label.setText(_translate("Dialog", "Host:"))
        self.label_2.setText(_translate("Dialog", "URL:"))
        self.groupBoxPlayer.setTitle(_translate("Dialog", "Player"))
        self.label_3.setText(_translate("Dialog", "Path:"))
        self.label_4.setText(_translate("Dialog", "Options:"))
        self.playerSingle.setText(_translate("Dialog", "Keep single player window"))
        self.groupBoxGuide.setTitle(_translate("Dialog", "Program Guide"))
        self.label_5.setText(_translate("Dialog", "Host:"))
        self.label_7.setText(_translate("Dialog", "URL:"))
        self.defaultsButton.setText(_translate("Dialog", "Defaults"))

