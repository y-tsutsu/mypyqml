import QtQuick 2.0

Rectangle {
    id: imageViewer
    width: 512
    height: 512

    Image {
        id: view
        clip: true
        sourceSize.width: 0
        anchors.fill: parent
        source: imageUrl
    }

    Rectangle {
        id: closeButton
        width: 100
        height: 100
        color: 'gray'
        anchors.right: parent.right

        MouseArea {
            anchors.fill: parent
            onPressed: {
                Qt.quit()
            }
        }

        Text {
            text: 'close'
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            wrapMode: Text.NoWrap
        }
    }
}
