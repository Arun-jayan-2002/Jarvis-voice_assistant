# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(700, 550)
        Widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 91))
        self.label.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(0, 0, 255);\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.59901 rgba(54, 238, 241, 255));\n"
            "font: 700 italic 32pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(-8, 90, 711, 401))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\arunj\\PycharmProjects\\Jarvis1\\GUI files\\start1.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.start = QtWidgets.QPushButton(Widget)
        self.start.setGeometry(QtCore.QRect(190, 500, 131, 41))
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.144, y1:0.199, x2:0.812, y2:0.784, stop:0.0891089 rgba(249, 8, 12, 255), stop:0.777228 rgba(249, 252, 5, 255));\n"
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.59901 rgba(54, 238, 241, 255));\n"
            "font: 700 italic 20pt \"Segoe UI\";\n"
            "\n"
            "border-color: rgb(85, 255, 255);\n"
            "border-style: solid;\n"
            "    border-width: 4px;\n"
            "    border-radius: 12px;")
        self.start.setObjectName("start")
        self.exit = QtWidgets.QPushButton(Widget)
        self.exit.setGeometry(QtCore.QRect(390, 500, 131, 41))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.144, y1:0.199, x2:0.812, y2:0.784, stop:0.0891089 rgba(249, 8, 12, 255), stop:0.777228 rgba(249, 252, 5, 255));\n"
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.59901 rgba(54, 238, 241, 255));\n"
            "font: 700 italic 20pt \"Segoe UI\";\n"
            "\n"
            "border-color: rgb(85, 255, 255);\n"
            "border-style: solid;\n"
            "    border-width: 4px;\n"
            "    border-radius: 12px;")
        self.exit.setObjectName("exit")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "       JARVIS TECHNOLOGY"))
        self.start.setText(_translate("Widget", "START"))
        self.exit.setText(_translate("Widget", "EXIT"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
