import rospy
import os
import rospkg

from python_qt_binding import loadUi
from python_qt_binding.QtCore import Signal
from python_qt_binding.QtWidgets import QDialog
from .status_item import StatusItem

class SupervisorLoggerLevelOptionPane(QDialog):
    closed = Signal(str)

    def __init__(self, name = None, status= None, parent= None):
        super(SupervisorLoggerLevelOptionPane, self).__init__()
        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('rqt_robot_supervisor_monitor'), 'src', 'resource',
                           'loggerleveloption.ui')
        loadUi(ui_file, self)

        obj_name = 'Level Option'
        self.setObjectName(obj_name)
        self.setWindowTitle(obj_name)

        self.show()

        # display node name in collumn view
        self._node_tree = StatusItem(self.node_tree.invisibleRootItem())
        string_level = str(status.level)
        name = status.name
        self._node_tree[name].update(status, string_level)
        self.node_tree.resizeColumnToContents(0)

#display level in spinbox
#setting new level by using supervisor node service -> ok button
# closing optionpanel with cancel button qDialog button box
#optional: greying setting level button if msg doesn't come from supervisor- (as it demands other service call that option panel can't handle)