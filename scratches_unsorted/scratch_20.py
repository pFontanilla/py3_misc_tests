from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (
    QAbstractItemModel, QFile,
    QIODevice, QModelIndex, Qt,
    QUrl
)
import pandas as pd
import numpy as np

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


class TreeModel(QtCore.QAbstractItemModel):
    def __init__(self, data, parent=None):
        super(TreeModel, self).__init__(parent)

        self.rootItem = TreeItem(("Title", "Summary"))
        self.setupModelData(data.split('\n'), self.rootItem)

    def roleNames(self):
        roles = {
            Qt.UserRole + 1: b"TitleRole",
            Qt.UserRole + 2: b"SummaryRole"
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

        if role != Qt.DisplayRole:
            return None

        item = index.internalPointer()

        return item.data(index.column())

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def setupModelData(self, lines, parent):
        parents = [parent]
        indentations = [0]

        # lines[number] = specific line
        # lines[number][position] = specific character
        # columnData = specific slice in a line

        number = 0

        print("while {} < {}".format(number, len(lines)))
        position = 0
        lineData = lines[number][position:].trimmed()
        columnData = [s for s in lineData.split('\t') if s]
        parents[-1].appendChild(TreeItem(columnData, parents[-1]))
        lineData = lines[5][position:].trimmed()
        columnData = [s for s in lineData.split('\t') if s]
        parents[-1].appendChild(TreeItem(columnData, parents[-1]))
        # parents.append(parents[-1].child(parents[-1].childCount()))
        # while number < len(lines):
        #
        #     print("\n     position=0")
        #     position = 0
        #
        #     print("     while position {} < len(lines[number] {}:".format(number, len(lines[number])))
        #     while position < len(lines[number]):
        #
        #         print("\n         if lines[number][position] {} != ' ':".format(lines[number][position]))
        #         if lines[number][position] != ' ':
        #             print("             break")
        #             break
        #         print("         position + 1 = {}".format(position+1))
        #         position += 1
        #
        #     lineData = lines[number][position:].trimmed()
        #     print("     lineData = {}".format(lines[number][position:].trimmed()))
        #     print("     if linedata:")
        #     if lineData:
        #         # Read the column data from the rest of the line.
        #         print("         columnData = [s for s in lineData.split('tab') if s]")
        #         columnData = [s for s in lineData.split('\t') if s]
        #         print("         columnData:{}".format(columnData))
        #
        #         print("if position {} > indentations[-1] {}:".format(position, indentations[-1]))
        #         if position > indentations[-1]:
        #             # The last child of the current parent is now the new
        #             # parent unless the current parent has no children.
        #
        #             if parents[-1].childCount() > 0:
        #                 parents.append(parents[-1].child(parents[-1].childCount() - 1))
        #                 indentations.append(position)
        #
        #         else:
        #             while position < indentations[-1] and len(parents) > 0:
        #                 parents.pop()
        #                 indentations.pop()
        #
        #         # Append a new item to the current parent's list of children.
        #         parents[-1].appendChild(TreeItem(columnData, parents[-1]))
        #
        #     number += 1


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    f = QtCore.QFile('default.txt')
    f.open(QtCore.QIODevice.ReadOnly)
    model = TreeModel(f.readAll())
    f.close()

    view = QtWidgets.QTreeView()
    view.setModel(model)
    view.setWindowTitle("Simple Tree Model")
    view.show()
    sys.exit(app.exec_())