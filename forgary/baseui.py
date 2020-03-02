# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from audio_lib import *
from tool_lib import *


class Ui_App(object):
    audio_wave = None


    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(290, 298)
        self.centralwidget = QtWidgets.QWidget(App)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.waveBox = QtWidgets.QComboBox(self.frame)
        self.waveBox.setEditable(False)
        self.waveBox.setObjectName("waveBox")
        self.waveBox.addItem("")
        self.waveBox.addItem("")
        self.waveBox.addItem("")
        self.waveBox.addItem("")
        self.verticalLayout.addWidget(self.waveBox)
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.secsBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.secsBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.secsBox.setObjectName("secsBox")
        self.verticalLayout.addWidget(self.secsBox)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.saveButton = QtWidgets.QPushButton(self.frame_3)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.save_file)

        self.verticalLayout_3.addWidget(self.saveButton)
        self.waveButton = QtWidgets.QPushButton(self.frame_3)
        self.waveButton.setObjectName("waveButton")
        self.waveButton.clicked.connect(self.gen_wave)
        
        self.verticalLayout_3.addWidget(self.waveButton)
        self.plotButton = QtWidgets.QPushButton(self.frame_3)
        self.plotButton.setObjectName("plotButton")
        self.plotButton.clicked.connect(self.plot_wave)

        self.verticalLayout_3.addWidget(self.plotButton)
        self.freqmodButton = QtWidgets.QPushButton(self.frame_3)
        self.freqmodButton.setObjectName("freqmodButton")
        self.freqmodButton.clicked.connect(self.modulate)
        
        self.verticalLayout_3.addWidget(self.freqmodButton)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_3)
        App.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(App)
        self.statusbar.setObjectName("statusbar")
        App.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(App)
        self.toolBar.setObjectName("toolBar")
        App.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(App)
        self.toolBar_2.setObjectName("toolBar_2")
        App.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionGenerate = QtWidgets.QAction(App)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionSave = QtWidgets.QAction(App)
        self.actionSave.setObjectName("actionSave")
        self.actionPlot = QtWidgets.QAction(App)
        self.actionPlot.setObjectName("actionPlot")
        self.actionModulate = QtWidgets.QAction(App)
        self.actionModulate.setObjectName("actionModulate")

        self.retranslateUi(App)
        self.hertzDial.sliderMoved['int'].connect(self.hertzDial.setValue)
        self.secsBox.valueChanged['double'].connect(self.secsBox.setValue)
        self.waveBox.activated['QString'].connect(self.waveBox.setCurrentText)
        QtCore.QMetaObject.connectSlotsByName(App)
        
        

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "HiveAudio Demo"))
        self.label_2.setText(_translate("App", "Wave Shape"))
        self.waveBox.setItemText(0, _translate("App", "Sine Wave"))
        self.waveBox.setItemText(1, _translate("App", "Triangle Wave"))
        self.waveBox.setItemText(2, _translate("App", "Sawtooth Wave"))
        self.waveBox.setItemText(3, _translate("App", "Square Wave"))
        self.label.setText(_translate("App", "Duration (s)"))
        self.saveButton.setText(_translate("App", "Save Wave"))
        self.waveButton.setText(_translate("App", "Generate Wave"))
        self.plotButton.setText(_translate("App", "Plot Wave"))
        self.freqmodButton.setText(_translate("App", "Modulate"))
        self.toolBar.setWindowTitle(_translate("App", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("App", "toolBar_2"))
        self.actionGenerate.setText(_translate("App", "Generate"))
        self.actionGenerate.setToolTip(_translate("App", "Generate audio from wave data"))
        self.actionGenerate.setShortcut(_translate("App", "Alt+Return"))
        self.actionSave.setText(_translate("App", "Save"))
        self.actionSave.setToolTip(_translate("App", "Save to WAV file"))
        self.actionSave.setShortcut(_translate("App", "Ctrl+S"))
        self.actionPlot.setText(_translate("App", "Plot"))
        self.actionPlot.setToolTip(_translate("App", "Plot current waveform "))
        self.actionPlot.setShortcut(_translate("App", "Ctrl+P"))
        self.actionModulate.setText(_translate("App", "Modulate"))
        self.actionModulate.setToolTip(_translate("App", "Generate audio and apply frequency modulation"))


    def save_file(self):
        pass
    
    def gen_wave(self):
        wave_type = self.waveBox.currentText()
        duration = float(self.secsBox.value())
        frequency = float(self.hertzDial.value())
        # create numpy array for audio and play it back
        wave_gen(wave_type=wave_type, duration=duration, frequency=frequency)

    def plot_wave(self):
        audio_wave = self.audio_wave
        plot_audio(audio_wave=audio_wave)


    def modulate(self):
        wave_type = self.waveBox.currentText()
        duration = float(self.secsBox.value())
        frequency = self.hertzDial.value()

        #same as wave_gen, but modul
        pitch_modulate(wave_type=wave_type, duration=duration, frequency=frequency)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QMainWindow()
    ui = Ui_App()
    ui.setupUi(App)
    App.show()
    sys.exit(app.exec_())
