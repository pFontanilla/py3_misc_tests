delegate: Flickable
{
    id: flick
    height: rowHeight
    width: col_MPN_New.width
    contentWidth: edit.paintedWidth
    contentHeight: edit.paintedHeight
    boundsBehavior: Flickable.OvershootBounds
    clip: true

    function ensureVisible(r)
    {
    if (contentX >= r.x)
        contentX = r.x;
else if (contentX + width <= r.x + r.width)
contentX = r.x+r.width-width;
if (contentY >= r.y)
contentY = r.y;
else if (contentY+height <= r.y+r.height)
contentY = r.y+r.height-height;
}

Rectangle{
id: rect
width: col_MPN_New.width
height: (rowHeight > edit.paintedHeight) ? rowHeight: edit.paintedHeight
border.width: 1
border.color: styleData.selected ? Qt.darker("lightgrey"): "lightgrey"
color: "transparent"

TextEdit
{
    id: edit
    width: flick.width
    focus: true
    verticalAlignment: TextEdit.AlignVCenter
    horizontalAlignment: TextEdit.AlignLeft
    text: styleData.value
    wrapMode: TextEdit.NoWrap
    leftPadding: textPad
    topPadding: topPad

    MouseArea{
        anchors.fill: parent
        onClicked: {
            modelDF.retrieveDataBool(styleData.index, "Accepted")
        parent.readOnly = caughtbool
parent.forceActiveFocus()
}
}

onEditingFinished: {
    modelDF.assignData(styleData.index, col_MPN_New.role, text)
}
Keys.onReturnPressed: {
}
}
}
}