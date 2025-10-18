import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class CarRentalApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car Rental Manager")
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet("background-color: #1e1e1e; color: #ffffff; font-family: Segoe UI;")
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        title = QtWidgets.QLabel("🚗 Car Rental Manager")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #00ffcc;")
        layout.addWidget(title)

        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Car", "Customer", "Date"])
        self.table.setStyleSheet("QHeaderView::section { background-color: #2d2d2d; }")
        layout.addWidget(self.table)

        btn_add = QtWidgets.QPushButton("➕ Add Rental")
        btn_add.setStyleSheet("background-color: #0078d7; color: white; padding: 8px; border-radius: 6px;")
        layout.addWidget(btn_add)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CarRentalApp()
    window.show()
    sys.exit(app.exec_())
