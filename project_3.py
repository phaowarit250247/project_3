# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_3.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1576, 791)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 70, 831, 351))
        self.patient_id = QLabel(self.centralwidget)
        self.patient_id.setObjectName(u"patient_id")
        self.patient_id.setGeometry(QRect(1010, 90, 61, 21))
        self.id_card_number = QLabel(self.centralwidget)
        self.id_card_number.setObjectName(u"id_card_number")
        self.id_card_number.setGeometry(QRect(1010, 120, 101, 21))
        self.firstname_th = QLabel(self.centralwidget)
        self.firstname_th.setObjectName(u"firstname_th")
        self.firstname_th.setGeometry(QRect(1010, 160, 101, 21))
        self.lastname_th = QLabel(self.centralwidget)
        self.lastname_th.setObjectName(u"lastname_th")
        self.lastname_th.setGeometry(QRect(1010, 200, 101, 21))
        self.firstname_en = QLabel(self.centralwidget)
        self.firstname_en.setObjectName(u"firstname_en")
        self.firstname_en.setGeometry(QRect(1010, 230, 101, 21))
        self.lastname_en = QLabel(self.centralwidget)
        self.lastname_en.setObjectName(u"lastname_en")
        self.lastname_en.setGeometry(QRect(1010, 270, 101, 21))
        self.gender = QLabel(self.centralwidget)
        self.gender.setObjectName(u"gender")
        self.gender.setGeometry(QRect(1010, 310, 101, 21))
        self.religion = QLabel(self.centralwidget)
        self.religion.setObjectName(u"religion")
        self.religion.setGeometry(QRect(1010, 350, 101, 21))
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(1130, 90, 231, 26))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(1130, 120, 231, 26))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(1130, 160, 231, 26))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(1130, 200, 231, 26))
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(1130, 230, 231, 26))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(1130, 270, 231, 26))
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(1130, 310, 231, 26))
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(1130, 350, 231, 26))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(1050, 420, 257, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Add = QPushButton(self.horizontalLayoutWidget)
        self.Add.setObjectName(u"Add")

        self.horizontalLayout.addWidget(self.Add)

        self.Delect = QPushButton(self.horizontalLayoutWidget)
        self.Delect.setObjectName(u"Delect")

        self.horizontalLayout.addWidget(self.Delect)

        self.Edit = QPushButton(self.horizontalLayoutWidget)
        self.Edit.setObjectName(u"Edit")

        self.horizontalLayout.addWidget(self.Edit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1576, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Patient_ID", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID_Card_Number", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"FirstName_TH", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"LastName_TH", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"FirsName_EN", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"LastName_EN", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Religion", None))
        self.patient_id.setText(QCoreApplication.translate("MainWindow", u"Patient_ID", None))
        self.id_card_number.setText(QCoreApplication.translate("MainWindow", u"ID_Card_Number", None))
        self.firstname_th.setText(QCoreApplication.translate("MainWindow", u"FirstName_TH", None))
        self.lastname_th.setText(QCoreApplication.translate("MainWindow", u"LastName_TH", None))
        self.firstname_en.setText(QCoreApplication.translate("MainWindow", u"FirstName_EN", None))
        self.lastname_en.setText(QCoreApplication.translate("MainWindow", u"LastName_EN", None))
        self.gender.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.religion.setText(QCoreApplication.translate("MainWindow", u"Religion", None))
        self.Add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.Delect.setText(QCoreApplication.translate("MainWindow", u"Delect", None))
        self.Edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

