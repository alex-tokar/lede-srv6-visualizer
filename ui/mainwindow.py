from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor, QFont, QBrush
from qtui.mainwindow import Ui_MainWindow
import paramiko
import os
from ncclient import manager


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, config):
        # Initialize the super-class and setup the UI
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.config = config

        image_laptop = QtGui.QPixmap("resources/laptop.png")#.scaledToWidth(64)
        image_router = QtGui.QPixmap("resources/router.png")#.scaledToWidth(64)

        self.scene = QGraphicsScene(0, 0, 760, 260)

        item_laptop = QGraphicsPixmapItem()
        item_laptop.setPixmap(image_laptop.copy())
        item_laptop.setPos(50, 90)
        item_laptop.setScale(0.25)
        self.scene.addItem(item_laptop)

        label_laptop = self.scene.addText("Client")
        label_laptop.setPos(item_laptop.pos().x() + 15, item_laptop.pos().y() + 60)

        item_rtrA = QGraphicsPixmapItem()
        item_rtrA.setPixmap(image_router.copy())
        item_rtrA.setPos(350, 90)
        item_rtrA.setScale(0.25)
        self.scene.addItem(item_rtrA)

        label_rtrA = self.scene.addText("rtrA")
        label_rtrA.setPos(item_rtrA.pos().x() + 20, item_rtrA.pos().y() + 60)

        item_rtrB = QGraphicsPixmapItem()
        item_rtrB.setPixmap(image_router.copy())
        item_rtrB.setPos(650, 90)
        item_rtrB.setScale(0.25)
        self.scene.addItem(item_rtrB)

        label_rtrB = self.scene.addText("rtrB")
        label_rtrB.setPos(item_rtrB.pos().x() + 20, item_rtrB.pos().y() + 60)

        self.line_laptop_to_rtrA = self.scene.addLine(item_laptop.pos().x() + 90, item_laptop.pos().y() + 30,
                                                      item_rtrA.pos().x() - 20, item_rtrA.pos().y() + 30,
                                                      QColor(0, 0, 255))

        self.line_rtrA_to_rtrB_1 = self.scene.addLine(item_rtrA.pos().x() + 90, item_rtrA.pos().y() + 30,
                                                      item_rtrB.pos().x() - 20, item_rtrB.pos().y() + 30,
                                                      QColor(0, 0, 255))
        self.line_rtrA_to_rtrB_2 = self.scene.addLine(item_rtrA.pos().x() + 90, item_rtrA.pos().y() + 50,
                                                      item_rtrB.pos().x() - 20, item_rtrB.pos().y() + 50,
                                                      QColor(0, 0, 255))
        self.line_rtrA_to_rtrA_1 = self.scene.addLine(item_rtrA.pos().x() + 90, item_rtrA.pos().y() + 30,
                                                      item_rtrA.pos().x() + 90, item_rtrA.pos().y() + 50,
                                                      QColor(0, 0, 255))
        self.line_rtrB_to_rtrB_1 = self.scene.addLine(item_rtrB.pos().x() - 20, item_rtrB.pos().y() + 30,
                                                      item_rtrB.pos().x() - 20, item_rtrB.pos().y() + 50,
                                                      QColor(0, 0, 255))

        self.indicator_laptop_to_rtrA = self.scene.addEllipse(item_laptop.pos().x() + 80, item_laptop.pos().y() + 25, 10, 10)
        self.indicator_rtrA_to_laptop = self.scene.addEllipse(item_rtrA.pos().x() - 20, item_rtrB.pos().y() + 25, 10, 10)

        self.indicator_rtrA_to_rtrB_1 = self.scene.addEllipse(item_rtrA.pos().x() + 80, item_rtrA.pos().y() + 25, 10, 10)
        self.indicator_rtrB_to_rtrA_1 = self.scene.addEllipse(item_rtrB.pos().x() - 20, item_rtrB.pos().y() + 25, 10, 10)

        self.indicator_rtrA_to_rtrB_2 = self.scene.addEllipse(item_rtrA.pos().x() + 80, item_rtrA.pos().y() + 45, 10, 10)
        self.indicator_rtrB_to_rtrA_2 = self.scene.addEllipse(item_rtrB.pos().x() - 20, item_rtrB.pos().y() + 45, 10, 10)

        self.toggle_indicator(self.indicator_rtrA_to_rtrB_1, False)
        self.toggle_indicator(self.indicator_rtrB_to_rtrA_1, False)
        self.toggle_indicator(self.indicator_rtrA_to_rtrB_2, False)
        self.toggle_indicator(self.indicator_rtrB_to_rtrA_2, False)
        self.toggle_indicator(self.indicator_laptop_to_rtrA, False)
        self.toggle_indicator(self.indicator_rtrA_to_laptop, False)

        label_rtrA_to_rtrB_1 = self.scene.addText("2222:3::1", QFont("Arial", 6))
        label_rtrA_to_rtrB_1.setPos(item_rtrA.pos().x() + 85, item_rtrA.pos().y() + 15)

        label_rtrA_to_rtrB_2 = self.scene.addText("2222:4::1", QFont("Arial", 6))
        label_rtrA_to_rtrB_2.setPos(item_rtrA.pos().x() + 85, item_rtrA.pos().y() + 50)

        label_rtrB_to_rtrA_1 = self.scene.addText("2222:3::2", QFont("Arial", 6))
        label_rtrB_to_rtrA_1.setPos(item_rtrB.pos().x() - 55, item_rtrB.pos().y() + 15)

        label_rtrB_to_rtrA_2 = self.scene.addText("2222:4::2", QFont("Arial", 6))
        label_rtrB_to_rtrA_2.setPos(item_rtrB.pos().x() - 55, item_rtrB.pos().y() + 50)

        label_laptop_to_rtrA = self.scene.addText("NETCONF", QFont("Arial", 6))
        label_laptop_to_rtrA.setPos(item_laptop.pos().x() + 175, item_laptop.pos().y() + 15)

        self.graphicsView.setScene(self.scene)

        self.timer = QTimer()
        self.timer.timeout.connect(self.flash_indicators)
        self.timer.start(250)

        self.ssh_rtrA = paramiko.SSHClient()
        self.ssh_rtrA.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_rtrA.connect(hostname=self.config["rtrA"]["hostname"],
                              username=self.config["rtrA"]["username"],
                              password=self.config["rtrA"]["password"])

        self.ssh_rtrB = paramiko.SSHClient()
        self.ssh_rtrB.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_rtrB.connect(hostname=self.config["rtrB"]["hostname"],
                              username=self.config["rtrB"]["username"],
                              password=self.config["rtrB"]["password"])

        self.router_data = {}

        self.startPingButton.clicked.connect(self.start_ping)
        self.stopPingButton.clicked.connect(self.stop_ping)
        self.installRouteButton.clicked.connect(self.install_route)
        self.uninstallRouteButton.clicked.connect(self.uninstall_route)
        self.ping_command = None

        self.ssh_rtrA.exec_command("killall example2 ; example2")

    def start_ping(self):
        self.ping_command = self.ssh_rtrA.exec_command("ping 2222:4::2")

    def stop_ping(self):
        self.ssh_rtrA.exec_command("killall ping")

    def install_route(self):
        with manager.connect_ssh(self.config["rtrA"]["hostname"],
                                 username=self.config["rtrA"]["username"],
                                 password=self.config["rtrA"]["password"],
                                 hostkey_verify=False) as m:
            with m.locked("running"):
                m.edit_config(target="running", config="""
                <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                    <srv6-explicit-path xmlns="urn:ietf:params:xml:ns:yang:srv6-explicit-path">
                        <path>
                            <destination>2222:4::2</destination>
                            <sr-path>
                                <srv6-segment>2222:3::2</srv6-segment>
                            </sr-path>
                        </path>
                    </srv6-explicit-path>
                </config>""")

    def uninstall_route(self):
        with manager.connect_ssh(self.config["rtrA"]["hostname"],
                                 username=self.config["rtrA"]["username"],
                                 password=self.config["rtrA"]["password"],
                                 hostkey_verify=False) as m:
            with m.locked("running"):
                m.edit_config(target="running", config="""
                <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                    <srv6-explicit-path xmlns="urn:ietf:params:xml:ns:yang:srv6-explicit-path">
                        <path nc:operation="delete">
                            <destination>2222:4::2</destination>
                        </path>
                    </srv6-explicit-path>
                </nc:config>""")

    def closeEvent(self, event):
        self.ssh_rtrA.close()
        self.ssh_rtrB.close()
        event.accept()

    def toggle_indicator(self, indicator, enabled):
        color = QColor(0, 255, 0, 255 if enabled else 0)
        indicator.setPen(color)
        indicator.setBrush(QBrush(color))

    def flash_indicators(self):
        indicators = {
            self.indicator_rtrA_to_rtrB_1: [self.ssh_rtrA, "eth1", "rtrA", self.line_rtrA_to_rtrB_1],
            self.indicator_rtrB_to_rtrA_1: [self.ssh_rtrB, "eth1", "rtrB", self.line_rtrA_to_rtrB_1],
            self.indicator_rtrA_to_rtrB_2: [self.ssh_rtrA, "eth2", "rtrA", self.line_rtrA_to_rtrB_2],
            self.indicator_rtrB_to_rtrA_2: [self.ssh_rtrB, "eth2", "rtrB", self.line_rtrA_to_rtrB_2],
        }

        for indicator in indicators:
            self.toggle_indicator(indicator, False)

        cleared_lines = False
        any_indicator = False

        for indicator in indicators:
            ssh, ifname, hostname, link_line = indicators[indicator]
            stdin, stdout, stderr = ssh.exec_command("ifconfig " + ifname + " | grep 'RX packets'")
            rx = int(stdout.readlines()[0].split(":")[1].split(" ")[0])

            if hostname not in self.router_data:
                self.router_data[hostname] = {}

            if ifname not in self.router_data[hostname]:
                self.router_data[hostname][ifname] = rx
            elif rx > self.router_data[hostname][ifname]:
                if not cleared_lines:
                    cleared_lines = True
                    self.toggle_line(self.line_rtrA_to_rtrB_1, False)
                    self.toggle_line(self.line_rtrA_to_rtrB_2, False)
                    self.toggle_line(self.line_rtrA_to_rtrA_1, False)
                    self.toggle_line(self.line_rtrB_to_rtrB_1, False)

                self.router_data[hostname][ifname] = rx
                self.toggle_indicator(indicator, True)
                self.toggle_line(link_line, True)

    def toggle_line(self, line, enabled):
        line.setPen(QColor(0, 255, 0) if enabled else QColor(0, 0, 255))

    def resizeEvent(self, event):
        self.graphicsView.resetTransform()
        self.graphicsView.scale(event.size().width() / 800.0, event.size().height() / 260.0 / 2.5)

        super(MainWindow, self).resizeEvent(event)

