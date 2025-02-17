import sys
import os
import argparse
import qdarkstyle

from PyQt5.QtWidgets import QApplication
from .main_window import MainWindow

NAME = "CQ-editor"
os.environ['QT_API'] = 'pyqt5'

# need to initialize QApp here, otherewise svg icons do not work on windows
app = QApplication(sys.argv, applicationName=NAME)
app.setStyleSheet(qdarkstyle.load_stylesheet())


def main():

    parser = argparse.ArgumentParser(description=NAME)
    parser.add_argument("filename", nargs="?", default=None)

    args = parser.parse_args(app.arguments()[1:])

    win = MainWindow(filename=args.filename if args.filename else None)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
