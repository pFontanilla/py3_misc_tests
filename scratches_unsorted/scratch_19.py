from PyQt5 import QtCore, QtGui, QtWidgets, QtQml
from PyQt5.QtCore import (
    QAbstractItemModel, QFile,
    QIODevice, QModelIndex, Qt,
    QUrl, pyqtSignal, pyqtSlot
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

    def data(self, key):
        try:
            # print("key: '{}'".format(key))
            return self.itemData[key]
        except IndexError:
            return None
        except TypeError:
            print ("self.itemData = '{}'".format(self.itemData))
            print("key = '{}'".format(key))

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

    ThalesPNBOMRole = QtCore.Qt.UserRole + 0
    MPNRole = QtCore.Qt.UserRole + 1
    AcceptedRole = QtCore.Qt.UserRole + 2

    updated = pyqtSignal(str, arguments=["retrieveDataQ"])
    updatedBool = pyqtSignal(bool, arguments=["retrieveDataBool"])

    def __init__(self, data, root, parent=None):
        super(DataFrameModel, self).__init__(parent)

        self.rootItem = TreeItem(root)
        self.setupModelData(data, self.rootItem)

    def roleNames(self):
        roles = {
            Qt.DisplayRole: b'tester',
            # QtCore.Qt.UserRole + 0: b'tester',
            # QtCore.Qt.UserRole + 1: b'value'
            DataFrameModel.ThalesPNBOMRole: b'ThalesPNBOM',
            DataFrameModel.MPNRole: b'MPN',
            DataFrameModel.AcceptedRole: b"Accepted"
        }
        print("roles: '{}'".format(roles))
        return roles

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):

        # print("role: '{}':".format(role))
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == DataFrameModel.ThalesPNBOMRole:
            return item.data("Thales_PN")
        elif role == DataFrameModel.MPNRole:
            print("collecting MPN: '{}'".format(item.data("MPN")))
            return item.data("MPN")
        elif role == DataFrameModel.AcceptedRole:
            return item.data("Accepted")

        item = index.internalPointer()

        return item.data(index.column())

    @pyqtSlot(QModelIndex, str)
    def retrieveDataQ(self, index, role):

        if not index.isValid():
            return None
        item = index.internalPointer()
        # print("itemdata = '{}'".format(item.itemData))
        print("successfully retrieved: '{}'".format(item.itemData[role]))
        self.updated.emit(item.itemData[role])

    @pyqtSlot(QModelIndex, str)
    def retrieveDataBool(self, index, role):

        if not index.isValid():
            return None
        item = index.internalPointer()
        # print("itemdata = '{}'".format(item.itemData))
        print("successfully retrieved bool: '{}'".format(str(item.itemData[role])))
        self.updatedBool.emit(item.itemData[role])

    @pyqtSlot(QModelIndex, str, str)
    def assignData(self, index, role, value):

        if not index.isValid():
            return None
        item = index.internalPointer()
        print("successfully assigned: '{}'".format(value))
        item.itemData[role] = value

    @pyqtSlot(QModelIndex, str, bool)
    def assignDataBool(self, index, role, value):

        if not index.isValid():
            return None
        item = index.internalPointer()
        print("successfully assigned: '{}'".format(value))
        item.itemData[role] = value

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def headerData(self, section, orientation, role):
        # if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
        return self.rootItem.data(section)

        # return None

    def index(self, row, column, parent):

        #print("column '{}' row '{}' parent '{}'".format(row, column, parent))
        # print(self.data(self.index(row, column, parent), "display"))

        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, 0, childItem)
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

        # filter1 = df.index.values == df["Top-Level_Component_Flag"]
        # df = df.where(filter1, other=False)
        df['Top-Level_Component_Flag'] = df.apply(lambda x: True if x.name == x["Top-Level_Component_Flag"] else False, axis=1)
        # print(df.head())

        for row in df.itertuples():

            rowData = {
                "Thales_PN": row.Thales_PN,
                "MPN": row.MPN,
                "Accepted": row._3
            }

            if row._3:
                parents[-1].appendChild(TreeItem(rowData, parents[-1]))
            else:
                parents[-1].child(-1).appendChild(TreeItem(rowData, parents[-1].child(-1)))


if __name__ == '__main__':
    import sys

    app = QtGui.QGuiApplication(sys.argv)

    test_data = {
        "Thales_PN": ["300-3-00011", "300-3-00011", "300-3-00011", "992312546", "700-3-20000", "700-3-20000"],
        "MPN": ["Kemet PN", "Vishay PN", "Murata PN", "TCIS PN", "Bossard PN", "McMaster-Carr PN"]
    }
    test_df = pd.DataFrame(test_data, columns = ["Thales_PN", "MPN"])
    model = DataFrameModel(test_df, ("Thales_PN", "MPN"))

    engine = QtQml.QQmlApplicationEngine()
    engine.rootContext().setContextProperty("modelDF", model)
    engine.quit.connect(app.quit)
    engine.load("treeview_custom/qml/main.qml")


    sys.exit(app.exec_())