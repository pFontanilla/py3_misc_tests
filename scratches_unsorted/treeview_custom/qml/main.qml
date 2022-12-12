import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQml.Models 2.2

ApplicationWindow{

    id: homePage
    visible: true
    width: 800
    height: 180
    title: "test"
    minimumWidth: 800
    minimumHeight: 180

    property string caught: ""
    property bool caughtbool: true

    TreeView {
        id: treeView
        anchors.fill: parent
        anchors.margins: 6
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        sortIndicatorVisible: true

        model: modelDF

        TableViewColumn {
            title: "Thales PN"
            role: "ThalesPNBOM"
            resizable: true
            movable: false
        }

        TableViewColumn {
            //styleData.selected
            //styleData.value
            //styleData.textcolor
            //styleData.row
            //styleData.column
            //styleData.elideMode
            //styleData.textAlignment
            title: "MPN"
            role: "MPN"
            resizable: true
            movable: false
            id: "col_MPN"
            delegate: Flickable{
                anchors.fill: parent
                contentWidth: parent.width
                clip: true
                TextEdit{
                    anchors.fill: parent
                    verticalAlignment: TextEdit.AlignVCenter
                    horizontalAlignment: TextEdit.AlignLeft
                    text: styleData.value
                    MouseArea{
                        anchors.fill: parent
                        onClicked:{
                            modelDF.retrieveDataBool(styleData.index, "Accepted")
                            parent.readOnly = caughtbool
                            parent.forceActiveFocus()
                        }
                    }
                    onEditingFinished:{
                        modelDF.assignData(styleData.index, "MPN", text)
                    }
                }
            }
        }

        TableViewColumn {
            id: acceptCol
            title: "Accept"
            role: "Accepted"
            resizable: true
            movable: false

            //signal lock(int myIndex, bool lock)

            delegate: CheckBox{
                checked: styleData.value
                onClicked:{
                    parent.forceActiveFocus()
                    if (checked) {
                        modelDF.retrieveDataQ(styleData.index, "MPN")
                        modelDF.assignDataBool(styleData.index, "Accepted", checked)
                        homePage.title = caught
                    } else {
                        modelDF.assignDataBool(styleData.index, "Accepted", checked)
                    }
                }
            }
        }

        rowDelegate: Rectangle{
            id: rowCustom
            color: colorHighlight("lightgrey")
            //color: styleData.selected ? Qt.darker(color, 1.25) : Qt.lighter(color, 1.25)
            border.width: 1
            border.color: "lightgrey"

            function colorHighlight(myColor){
                if (styleData.selected){
                    myColor = Qt.darker(myColor, 1.25)
                } else {
                    myColor = Qt.lighter(myColor, 1.25)
                }

                return myColor
            }
        }

        function lockRow(myRow, myColumn){
            indexAt(myRow, myColumn-1)
        }
    }

    Connections{
        target: modelDF

        onUpdated:{
           caught = retrieveDataQ
        }
        onUpdatedBool:{
            caughtbool = retrieveDataBool
        }
    }

}