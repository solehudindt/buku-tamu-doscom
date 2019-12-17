from PyQt5 import QtCore, QtGui, QtWidgets
from forms.form_peminjaman import Form_Pinjam
from models import Pinjam, session

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 578)

        # self.timer_status = QtCore.QTimer()
        # self.timer_status.timeout.connect(self.loadPinjam)

        # # check every half-second
        # self.timer_status.start(1000*2)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 110, 518, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tablePeminj = QtWidgets.QTableWidget(1,5)
        self.tablePeminj.verticalHeader().hide()
        self.tablePeminj.setHorizontalHeaderLabels(column.key for column in Pinjam.__table__.columns)
        self.tablePeminj.setObjectName("tablePeminj")
        # self.loadPinjam()
        self.verticalLayout.addWidget(self.tablePeminj)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tablePenit = QtWidgets.QTableWidget(1,5)
        self.tablePenit.verticalHeader().hide()
        self.tablePenit.setObjectName("tablePenit")
        self.verticalLayout.addWidget(self.tablePenit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(580, 130, 131, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.peminjaman = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.peminjaman.clicked.connect(self.openPinjam)
        self.peminjaman.setObjectName("peminjaman")
        self.verticalLayout_2.addWidget(self.peminjaman)
        self.pengembalian = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pengembalian.setObjectName("pengembalian")
        self.verticalLayout_2.addWidget(self.pengembalian)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(580, 220, 131, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.penitipan = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.penitipan.setObjectName("penitipan")
        self.verticalLayout_4.addWidget(self.penitipan)
        self.pengambilan = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pengambilan.setObjectName("pengambilan")
        self.loadData = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.loadData.setObjectName("loadData")
        self.loadData.clicked.connect(self.loadPinjam)
        self.verticalLayout_4.addWidget(self.pengambilan)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(580, 200, 131, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 60, 191, 16))
        self.label_4.setObjectName("label_4")
        self.loadPinjam()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 490, 80, 23))
        self.pushButton.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuExit = QtWidgets.QAction(MainWindow)
        self.menuExit.setShortcut("")
        self.menuExit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.menuExit.setObjectName("menuExit")
        self.menuFile.addAction(self.menuExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Buku tamu alpha 0.1"))
        self.label_2.setText(_translate("MainWindow", "Data Peminjaman :"))
        self.label.setText(_translate("MainWindow", "Data Penitipan :"))
        self.peminjaman.setText(_translate("MainWindow", "Peminjaman"))
        self.pengembalian.setText(_translate("MainWindow", "Pengembalian"))
        self.penitipan.setText(_translate("MainWindow", "Penitipan"))
        self.pengambilan.setText(_translate("MainWindow", "Pengambilan"))
        self.loadData.setText(_translate("MainWindow", "Load Data"))
        self.label_3.setText(_translate("MainWindow", "Buku Tamu"))
        self.label_4.setText(_translate("MainWindow", "Dinus Open Source Community"))
        self.pushButton.setText(_translate("MainWindow", "Keluar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuExit.setText(_translate("MainWindow", "exit"))

    def openPinjam(self):
        self.pinjamWindow = QtWidgets.QMainWindow()
        self.ui = Form_Pinjam()
        self.ui.setupUi(self.pinjamWindow)
        self.pinjamWindow.show()

    def loadPinjam(self):
        semuaAcara = session.query(Pinjam.id, Pinjam.nama, Pinjam.barang, Pinjam.tanggal, Pinjam.tipe).all()
        for row_number, row_data in enumerate(semuaAcara):
            self.tablePeminj.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tablePeminj.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            # self.timer_status.stop()

    # def timerLoadPinj(self):
    #     self.loadPinjam()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())