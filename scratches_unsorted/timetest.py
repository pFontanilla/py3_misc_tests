SETUP_CODE="""from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (
    QAbstractItemModel, QFile,
    QIODevice, QModelIndex, Qt,
    QUrl
)
import pandas as pd
import numpy as np
import timeit
import sys
from __main__ import DataFrameModel
from __main__ import TreeItem"""

TEST_CODE1="""app = QtWidgets.QApplication(sys.argv)

test_data = {
    "Thales_PN": ["300-3-00011", "300-3-00011", "300-3-00011", "992312546", "700-3-20000", "700-3-20000"],
    "MPN": ["Kemet PN", "Vishay PN", "Murata PN", "TCIS PN", "Bossard PN", "McMaster-Carr PN"]
}
test_df = pd.DataFrame(test_data, columns = ["Thales_PN", "MPN"])
model = DataFrameModel(test_df, ("Thales_PN", "MPN"), True)
print('a')"""

TEST_CODE2="""app = QtWidgets.QApplication(sys.argv)

test_data = {
    "Thales_PN": ["300-3-00011", "300-3-00011", "300-3-00011", "992312546", "700-3-20000", "700-3-20000"],
    "MPN": ["Kemet PN", "Vishay PN", "Murata PN", "TCIS PN", "Bossard PN", "McMaster-Carr PN"]
}
test_df = pd.DataFrame(test_data, columns = ["Thales_PN", "MPN"])
model = DataFrameModel(test_df, ("Thales_PN", "MPN"), False)"""
