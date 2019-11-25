# http://zetcode.com/gui/pyqt5/firstprograms/
import sys
import pandas as pd
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets  # import QApplication


class DataTable(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def rowCount(self, parent:QtCore.QModelIndex=None):
        return self.data.shape[0]

    def columnCount(self, parnet:QtCore.QModelIndex=None):
        return self.data.shape[1]

    def data(self, index:QtCore.QModelIndex, role:QtCore.Qt.ItemDataRole=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self.data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col:int, orientation:QtCore.Qt.Orientation=None, role:QtCore.Qt.ItemDataRole=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.data.columns[col]
        return None


class DataGrid(QtWidgets.QTableView):
    def __init__(self, parent:QtWidgets.QWidget = None):
        super().__init__()


class Window(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None, title: str = None):
        super().__init__()
        self.parent = parent
        self.title = title
        self.OnInit(title)

    def OnInit(self, title):
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.center()
        grid = DataGrid(self)
        grid.setObjectName("DataGrid")
        table = DataTable(pd.read_excel("cntx.xlsx", sheet_name="home"))
        grid.setModel(table)
        header = grid.horizontalHeader()
        # setSectionResizeMode() methon has its override.
        # if only resize param passed into it - it'll be applied to all columns.
        # if first argument passed as i=int(0:...) than resize mode will be applied to
        # the i-th column only.
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(grid)
        self.setLayout(layout)

    def center(self):
        s = QtWidgets.QDesktopWidget().screenGeometry()
        w = self.frameGeometry()
        self.move(
            (s.getCoords()[2] - w.getCoords()[2])/2,
            (s.getCoords()[3] - w.getCoords()[3])/2
        )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window("PyQt5 Application")
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec())
