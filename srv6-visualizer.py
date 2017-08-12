#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from ui.mainwindow import MainWindow
import configparser


def main():
    app = QApplication(sys.argv)
    window = MainWindow(config)
    window.show()

    ret = app.exec_()
    sys.exit(ret)

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config["rtrA"] = {"hostname": "192.168.56.101",
                      "username": "root",
                      "password": "router"}
    config["rtrB"] = {"hostname": "192.168.56.102",
                      "username": "root",
                      "password": "router"}
    config.read('config.ini')

    main()
