import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QDialog
import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO
from gpiozero import Button
import time

from QTtemplate import Ui_DriverScreen  # here you need to correct the names

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_DriverScreen()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
