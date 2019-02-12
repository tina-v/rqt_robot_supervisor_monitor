import rospy
import os
import rospkg

from python_qt_binding import loadUi

from python_qt_binding.QtWidgets import QWidget

class SupervisorLoggerLevelOptionPane(QWidget):
    closed = Signal(str)

    def __init__(self, name, status):
        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('rqt_robot_monitor'), 'resource',
                           'loggerleveloption.ui')
        loadUi(ui_file, self)

        obj_name = 'Level Option'
        self.setObjectName(obj_name)
        self.setWindowTitle(obj_name)