# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioHiveBase.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(322, 420)
        App.setToolTip("")
        self.gridLayout_2 = QtWidgets.QGridLayout(App)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(App)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.waveBox = QtWidgets.QComboBox(self.frame_2)
        self.waveBox.setEditable(False)
        self.waveBox.setObjectName("waveBox")
        self.waveBox.addItem("")
        self.waveBox.addItem("")
        self.waveBox.addItem("")
        self.waveBox.addItem("")
        self.gridLayout.addWidget(self.waveBox, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(App)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.secsBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.secsBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.secsBox.setObjectName("secsBox")
        self.verticalLayout.addWidget(self.secsBox)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.hertzDial = QtWidgets.QDial(self.frame)
        self.hertzDial.setMinimum(73)
        self.hertzDial.setMaximum(1300)
        self.hertzDial.setSingleStep(1)
        self.hertzDial.setProperty("value", 440)
        self.hertzDial.setWrapping(False)
        self.hertzDial.setNotchTarget(5.0)
        self.hertzDial.setNotchesVisible(False)
        self.hertzDial.setObjectName("hertzDial")
        self.verticalLayout.addWidget(self.hertzDial)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(App)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_2.addWidget(self.saveButton, 2, 0, 1, 1)
        self.plotButton = QtWidgets.QPushButton(App)
        self.plotButton.setObjectName("plotButton")
        self.gridLayout_2.addWidget(self.plotButton, 3, 0, 1, 1)
        self.freqmodButton = QtWidgets.QPushButton(App)
        self.freqmodButton.setObjectName("freqmodButton")
        self.gridLayout_2.addWidget(self.freqmodButton, 4, 0, 1, 1)
        self.waveButton = QtWidgets.QPushButton(App)
        self.waveButton.setObjectName("waveButton")
        self.gridLayout_2.addWidget(self.waveButton, 5, 0, 1, 1)

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "AudioHive PreAlpha"))
        self.waveBox.setItemText(0, _translate("App", "Sine Wave"))
        self.waveBox.setItemText(1, _translate("App", "Triangle Wave"))
        self.waveBox.setItemText(2, _translate("App", "Sawtooth Wave"))
        self.waveBox.setItemText(3, _translate("App", "Square Wave"))
        self.label_2.setText(_translate("App", "Wave Shape"))
        self.label.setText(_translate("App", "Seconds"))
        self.saveButton.setText(_translate("App", "Save Wave"))
        self.plotButton.setText(_translate("App", "Plot Wave"))
        self.freqmodButton.setText(_translate("App", "Modulate"))
        self.waveButton.setText(_translate("App", "Generate Wave"))
