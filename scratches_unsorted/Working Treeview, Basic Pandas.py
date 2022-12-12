from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (
    QAbstractItemModel, QFile,
    QIODevice, QModelIndex, Qt,
    QUrl
)
import pandas as pd

class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return len(self.itemData)

    def data(self, column):
        try:
            return self.itemData[column]
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0

    def __str__(self):

        print(self.itemData)
        for child in self.childItems:
            print(child.itemData)


class DataFrameModel(QtCore.QAbstractItemModel):

    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, data, root, parent=None):
        super(DataFrameModel, self).__init__(parent)

        self.rootItem = TreeItem(root)
        self.setupModelData(data, self.rootItem)

    def roleNames(self):
        roles = {
            Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value'
        }
        return roles

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None

        if role != QtCore.Qt.DisplayRole:
            return None

        item = index.internalPointer()

        return item.data(index.column())

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def setupModelData(self, df, parent):
        parents = [parent]
        layer = [0]

        number = 0
        flag = df.Thales_PN

        df = df.sort_values(by="Thales_PN")
        df = df.reset_index(drop=True)

        df['Top-Level_Component_Flag'] = df.Thales_PN.searchsorted(df.Thales_PN, side="left")
        print(df)

        # filter1 = df.index.values == df["Top-Level_Component_Flag"]
        # df = df.where(filter1, other=False)
        df['Top-Level_Component_Flag'] = df.apply(lambda x: True if x.name == x["Top-Level_Component_Flag"] else False, axis=1)
        print(df)

        for row in df.itertuples():
            print("")
            rowData = [
                row.Thales_PN,
                row.MPN,
            ]
            print(row)
            if row._3:
                print("I am a parent:{}".format(rowData))
                parents[-1].appendChild(TreeItem(rowData, parents[-1]))
            else:
                print("I am a child:{}".format(rowData))
                parents[-1].child(-1).appendChild(TreeItem(rowData, parents[-1].child(-1)))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    test_data = {
        "Thales_PN": ["300-3-00011", "300-3-00011", "300-3-00011", "992312546", "700-3-20000", "700-3-20000"],
        "MPN": ["Kemet PN", "Vishay PN", "Murata PN", "TCIS PN", "Bossard PN", "McMaster-Carr PN"]
    }
    test_df = pd.DataFrame(test_data, columns = ["Thales_PN", "MPN"])
    model = DataFrameModel(test_df, ("Thales_PN", "MPN"))



    view = QtWidgets.QTreeView()
    view.setModel(model)
    view.setWindowTitle("Simple Tree Model")
    view.show()
    sys.exit(app.exec_())