import QtQuick 2.0

Rectangle {
    width: 640
    height: 480

    function append(newElement) {
        myModel.append(newElement)
        if (myModel.count >= 1000) {
            myModel.remove(0)
        }
    }

    ListModel {
        id: myModel
    }

    ListView {
        anchors.fill: parent
        id: scheduleList
        model: myModel
        delegate: myDelegete
    }

    Component {
        id: myDelegete
        Text {
            text: message
        }
    }
}
