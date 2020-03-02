# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioHiveplay.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_playbackApp(object):
    def setupUi(self, playbackApp):
        playbackApp.setObjectName("playbackApp")
        playbackApp.resize(449, 144)
        self.formLayout_2 = QtWidgets.QFormLayout(playbackApp)
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.abortButton = QtWidgets.QPushButton(playbackApp)
        self.abortButton.setObjectName("abortButton")
        self.verticalLayout.addWidget(self.abortButton)
        self.saveButton = QtWidgets.QPushButton(playbackApp)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.plotButton = QtWidgets.QPushButton(playbackApp)
        self.plotButton.setObjectName("plotButton")
        self.verticalLayout.addWidget(self.plotButton)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(playbackApp)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.playbackProgress = QtWidgets.QProgressBar(playbackApp)
        self.playbackProgress.setProperty("value", 0)
        self.playbackProgress.setObjectName("playbackProgress")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.playbackProgress)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.formLayout)
        self.playButton = QtWidgets.QPushButton(playbackApp)
        self.playButton.setObjectName("playButton")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.playButton)

        self.retranslateUi(playbackApp)
        QtCore.QMetaObject.connectSlotsByName(playbackApp)

    def retranslateUi(self, playbackApp):
        _translate = QtCore.QCoreApplication.translate
        playbackApp.setWindowTitle(_translate("playbackApp", "HiveAudio Synth Playback"))
        self.abortButton.setText(_translate("playbackApp", "Exit without Saving"))
        self.saveButton.setText(_translate("playbackApp", "Save"))
        self.plotButton.setText(_translate("playbackApp", "Plot Wave"))
        self.label.setText(_translate("playbackApp", "Track Duration"))
        self.playbackProgress.setFormat(_translate("playbackApp", "%p%p.%p s"))
        self.playButton.setText(_translate("playbackApp", "Play"))
