from PyQt5 import QtCore, QtGui, QtWidgets
from models import *
import sys

x_pos = 0
y_pos = 0

def temp_func(asd):
    print(asd)
    x_pos = 10
    y_pos = 20
    print(x_pos, y_pos)

class Ui_ControlPanel(object):

    def setupUi(self, ControlPanel):

        ControlPanel.setObjectName("ControlPanel")
        ControlPanel.setWindowTitle("Control Panel v1")
        ControlPanel.resize(800, 600)
        
        # ------------------------------------------------ #
                
        self.X_VALUE_LABLE = QtWidgets.QLabel(ControlPanel)
        self.X_VALUE_LABLE.setGeometry(QtCore.QRect(20, 40, 91, 61))
        self.X_VALUE_LABLE.setObjectName("X_VALUE_LABLE")
        self.X_VALUE_LABLE.setText("X Value : ")
        
        self.X_VALUE_INPUT = QtWidgets.QLineEdit(ControlPanel)
        self.X_VALUE_INPUT.setGeometry(QtCore.QRect(140, 40, 104, 61))
        self.X_VALUE_INPUT.setObjectName("X_VALUE_INPUT")
        
        self.Y_VALUE_LABLE = QtWidgets.QLabel(ControlPanel)
        self.Y_VALUE_LABLE.setGeometry(QtCore.QRect(300, 40, 91, 61))
        self.Y_VALUE_LABLE.setObjectName("Y_VALUE_LABLE")
        self.Y_VALUE_LABLE.setText("Y Value : ")
        
        self.Y_VALUE_INPUT = QtWidgets.QLineEdit(ControlPanel)
        self.Y_VALUE_INPUT.setGeometry(QtCore.QRect(420, 40, 104, 61))
        self.Y_VALUE_INPUT.setObjectName("Y_VALUE_INPUT")
        
        self.Z_VALUE_LABLE = QtWidgets.QLabel(ControlPanel)
        self.Z_VALUE_LABLE.setGeometry(QtCore.QRect(550, 40, 91, 61))
        self.Z_VALUE_LABLE.setObjectName("Z_VALUE_LABLE")
        self.Z_VALUE_LABLE.setText("Z Value : ")
        
        self.Z_VALUE_INPUT = QtWidgets.QLineEdit(ControlPanel)
        self.Z_VALUE_INPUT.setGeometry(QtCore.QRect(670, 40, 104, 61))
        self.Z_VALUE_INPUT.setObjectName("Z_VALUE_INPUT")
        
        # ------------------------------------------------ #
        
        self.Expected_view = QtWidgets.QTextEdit(ControlPanel)
        self.Expected_view.setGeometry(QtCore.QRect(130, 140, 621, 281))
        self.Expected_view.setObjectName("Expected_view")
        
        self.X = QtWidgets.QLabel(ControlPanel)
        self.X.setGeometry(QtCore.QRect(730, 430, 21, 16))
        self.X.setObjectName("X")
        
        self.Y = QtWidgets.QLabel(ControlPanel)
        self.Y.setGeometry(QtCore.QRect(110, 140, 21, 16))
        self.Y.setObjectName("Y")
        
        self.EXPECTED_VALUE = QtWidgets.QPushButton(ControlPanel)
        self.EXPECTED_VALUE.setGeometry(QtCore.QRect(20, 140, 71, 281))
        self.EXPECTED_VALUE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EXPECTED_VALUE.setObjectName("EXPECTED_VALUE")
        
        # ------------------------------------------------ #
        
        self.SPEED_VALUE_LABLE = QtWidgets.QLabel(ControlPanel)
        self.SPEED_VALUE_LABLE.setGeometry(QtCore.QRect(60, 470, 131, 51))
        self.SPEED_VALUE_LABLE.setObjectName("SPEED_VALUE_LABLE")
        self.SPEED_VALUE_LABLE.setText("Speed(mm/s) : ")
        
        self.SPEED_VALUE_INPUT = QtWidgets.QLineEdit(ControlPanel)
        self.SPEED_VALUE_INPUT.setGeometry(QtCore.QRect(230, 470, 104, 51))
        self.SPEED_VALUE_INPUT.setObjectName("SPEED_VALUE_INPUT")
        
        self.PULSE_VALUE_LABLE = QtWidgets.QLabel(ControlPanel)
        self.PULSE_VALUE_LABLE.setGeometry(QtCore.QRect(410, 470, 131, 51))
        self.PULSE_VALUE_LABLE.setObjectName("PULSE_VALUE_LABLE")
        self.PULSE_VALUE_LABLE.setText("Pulse : ")
        
        self.PULSE_VALUE_INPUT = QtWidgets.QLineEdit(ControlPanel)
        self.PULSE_VALUE_INPUT.setGeometry(QtCore.QRect(590, 470, 104, 51))
        self.PULSE_VALUE_INPUT.setObjectName("PULSE_VALUE_INPUT")
        
        # ----------------------BOTTOM-------------------- #
        
        self.START_BUTTON = QtWidgets.QPushButton(ControlPanel)
        self.START_BUTTON.setGeometry(QtCore.QRect(10, 540, 131, 51))
        self.START_BUTTON.setObjectName("START_BUTTON")
        self.START_BUTTON.setText("Start")
        self.START_BUTTON.clicked.connect(self.btn_start_click)
        
        self.STOP_BUTTON = QtWidgets.QPushButton(ControlPanel)
        self.STOP_BUTTON.setGeometry(QtCore.QRect(160, 540, 131, 51))
        self.STOP_BUTTON.setObjectName("STOP_BUTTON")
        self.STOP_BUTTON.setText("Stop")
        
        self.FINISH_BUTTON = QtWidgets.QPushButton(ControlPanel)
        self.FINISH_BUTTON.setGeometry(QtCore.QRect(320, 540, 131, 51))
        self.FINISH_BUTTON.setFlat(False)
        self.FINISH_BUTTON.setObjectName("FINISH_BUTTON")
        self.FINISH_BUTTON.setText("Finish")
        
        self.SAVE_AS_BUTTON = QtWidgets.QPushButton(ControlPanel)
        self.SAVE_AS_BUTTON.setGeometry(QtCore.QRect(480, 540, 131, 51))
        self.SAVE_AS_BUTTON.setObjectName("SAVE_AS_BUTTON")
        self.SAVE_AS_BUTTON.setText("Save as")
        
        self.SAVE_BUTTON = QtWidgets.QPushButton(ControlPanel)
        self.SAVE_BUTTON.setGeometry(QtCore.QRect(630, 540, 131, 51))
        self.SAVE_BUTTON.setObjectName("SAVE_BUTTON")
        self.SAVE_BUTTON.setText("Save")
        
        # ------------------------------------------------ #
    
    def btn_start_click(self):
        need_pulse = False
        
        if self.X_VALUE_INPUT.text() == '':
            self.X_VALUE_INPUT.setText('0')
        if self.Y_VALUE_INPUT.text() == '':
            self.Y_VALUE_INPUT.setText('0')
        if self.Z_VALUE_INPUT.text() == '':
            self.PULSE_VALUE_INPUT.setText('0')
        
        if self.PULSE_VALUE_INPUT.text() == '':
            need_pulse = True
            if self.SPEED_VALUE_INPUT.text() == '':
                self.PULSE_VALUE_INPUT.setText('0')
            else:
                # TransFrom Speed to Pulse
                xz = 0
        
        if self.SPEED_VALUE_INPUT.text() == '':
            if self.PULSE_VALUE_INPUT.text() == '':
                self.SPEED_VALUE_INPUT.setText('0')
            else:
                # TransFrom Pulse to Speed
                xz = 0
        
        mXvalue = int(self.X_VALUE_INPUT.text())
        mYvalue = int(self.Y_VALUE_INPUT.text())
        mZvalue = int(self.Z_VALUE_INPUT.text())
        
        if need_pulse:
            mPulse = int(self.PULSE_VALUE_INPUT.text())
        else:
            mPulse = int(self.PULSE_VALUE_INPUT.text())
        
        btn_start_click_function(mXvalue, mYvalue, mZvalue, mPulse)
        MoveInit()
        