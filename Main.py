from untitled import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QWidget, QStyledItemDelegate, QComboBox
from PyQt6.QtCore import Qt, QModelIndex
import sys



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_window = Ui_MainWindow()
    mainWindow = QMainWindow()
    ui_window.setupUi(mainWindow)

    item = QTreeWidgetItem()
    item.setText(0, "No Editable.")
    cb = QComboBox()
    cb.addItem("Test")
    cb.addItem("Test2")

    item2 = QTreeWidgetItem()
    item2.setText(0, "a")
    item2.setText(1, "b")
    item2.setText(2, "c")
    item2.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)

    item.addChild(item2)

    ui_window.treeWidget.setColumnCount(3)
    ui_window.treeWidget.setColumnHidden(2, True)
    ui_window.treeWidget.addTopLevelItem(item)

    ui_window.treeWidget.setItemWidget(item, 1, cb)

    mainWindow.show()
    sys.exit(app.exec())