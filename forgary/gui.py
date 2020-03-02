import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,
                            QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QFileDialog, QCheckBox, QProgressBar,
                            QComboBox, QLabel, QLineEdit, QInputDialog

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle('Mod Synth')

        extractAction = QAction('&Exit the synth', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)

        openSynth = QAction('&New Synth', self)
        openSynth.setShortcut('Ctrl+E')
        openSynth.setStatusTip('Open Synthesizer')
        openSynth.triggered.connect(self.synth)

        openFile = QAction('&Import Audio', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        savePlot = QAction('&Save Data Plot', self)
        savePlot.setStatusTip('Save Data')
        savePlot.triggered.connect(self.file_save_plot)

        saveWav = QAction('&Save Wave File', self)
        saveWav.setShortcut('Ctrl+S')
        saveWav.setStatusTip('Save File')
        saveWav.triggered.connect(self.file_save)


        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        fileMenu.addAction(openFile)
        fileMenu.addAction(savePlot)
        fileMenu.addAction(saveWav)

        editMenu = mainMenu.addMenu('&Edit')
        editMenu.addAction(openSynth)

        self.toolBar = self.addToolBar('synthesis')

        self.home()


    def synth(self):
        pass

    def file_open(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

        file = open(name, 'r')
        self.synth()

        with file:
            pass

    def file_save(self):
        pass

    def home(self):
        btn = QPushButton('New', self)
        btn.clicked.connect(self.refresh_synth)
        btn.resize(btn.sizeHint())
        btn.move(25, 100)

        checkBox = QCheckBox('Render Data Plot', self)
        checkBox.toggle()
        checkBox.move(25, 150)
        checkBox.stateChanged.connect(self.toggle_plot)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QPushButton('Play', self)
        self.btn.move(25, 200)
        self.btn.clicked.connect(self.play)

        self.dial = QDial()
        self.dial.setMinimum(73.00)
        self.dial.setMaximum(833.333)
        self.dial.setValue(440.0)
        self.dial.move(75, 100)
        self.dial.valueChanged.connect(self.tone_dialed)


        self.lineSecs = QLineEdit('5')
        self.lineSecs.move(75, 150)


