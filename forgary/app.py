import sys
from PyQt5.QtCore import QCoreApplication, Qt

from PyQt5.QtWidgets import QApplication

from baseui import Ui_App


if __name__ == "__main__":

    def run():
        app = QApplication(sys.argv)
        Gui = Ui_App()

        sys.exit(app.exec_())

run()


