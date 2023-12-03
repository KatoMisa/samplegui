#!/usr/bin/env python
import sys
import subprocess
import os
import time
import platform
from PyQt5.QtCore import Qt, QThread, pyqtSignal,QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QVBoxLayout, QGroupBox, QRadioButton,QLabel
from pyqtspinner.spinner import WaitingSpinner

class WorkerThread1(QThread):
   finished = pyqtSignal(int)
   def run(self):
       try:
           os.chdir('/home/rsdlab/workspace/seedmover/_sy')
           result = subprocess.run(['./a_collectmodule.sh'], capture_output=True, text=True,shell=False)
           returncode = result.returncode
           self.finished.emit(returncode)
       except subprocess.CalledProcessError:
            self.finished.emit(-1)
class WorkerThread2(QThread):
   finished = pyqtSignal(int)
   def run(self):
       try:
           os.chdir('/home/rsdlab/workspace/seedmover/_sy')
           result = subprocess.run(['./b_collectmodule.sh'], capture_output=True, text=True,shell=False)
           returncode = result.returncode
           self.finished.emit(returncode)
       except subprocess.CalledProcessError:
           self.finished.emit(-1)
class WorkerThread3(QThread):
   finished = pyqtSignal(int)
   def run(self):
       try:
           os.chdir('/home/rsdlab/workspace/seedmover/_sy')
           result = subprocess.run(['./a_SystemBuild.sh'], capture_output=True, text=True,shell=False)
           returncode = result.returncode
           self.finished.emit(returncode)
       except subprocess.CalledProcessError:
           self.finished.emit(-1)
class WorkerThread4(QThread):
   finished = pyqtSignal(int)
   def run(self):
       try:
           os.chdir('/home/rsdlab/workspace/seedmover/_sy')
           result = subprocess.run(['./b_Systembuild.sh'], capture_output=True, text=True,shell=False)
           returncode = result.returncode
           self.finished.emit(returncode)
       except subprocess.CalledProcessError:
           self.finished.emit(-1)
class MainWindow(QWidget):
   def __init__(self):
       super().__init__()
       self.resize(400,450)
       self.setWindowTitle('Robot Controll')
       self.layout = QVBoxLayout()
  
       self.label9=QLabel('Robot Controll')
       self.label9.setAlignment(Qt.AlignCenter)
       self.label9.setStyleSheet("font-weight:bold")
       self.layout.addWidget(self.label9)

       self.group_box1 = QGroupBox("Robot")
       self.radio_button1 = QRadioButton("Seed-Noid")
       self.radio_button2 = QRadioButton("AIREC")
       self.radio_button1.setChecked(True)

       self.group_box_layout1 = QVBoxLayout()
       self.group_box_layout1.addWidget(self.radio_button1)
       self.group_box_layout1.addWidget(self.radio_button2)
       self.group_box1.setLayout(self.group_box_layout1)

       self.group_box2 = QGroupBox("Option")
       self.button1 = QPushButton("CollectModules")
       self.button2 = QPushButton("SystemBuild")
       self.button3 = QPushButton("SystemRun")
       self.button3.setEnabled(False)
       self.group_box_layout2 = QVBoxLayout()
       self.group_box_layout2.addWidget(self.button1)
       self.group_box_layout2.addWidget(self.button2)
       self.group_box_layout2.addWidget(self.button3)
       self.group_box2.setLayout(self.group_box_layout2)

       self.button4 = QPushButton("stop")
       self.button4.setEnabled(False)

       #self.layout = QVBoxLayout()
       self.spinner = WaitingSpinner(self, center_on_parent=True,lines=12,line_length=10,line_width=10)
       self.group_box1.move(100,100)
       self.group_box2.move(100,180)
       self.layout.addWidget(self.group_box1)
       self.layout.addWidget(self.group_box2)
       self.layout.addWidget(self.button4)

       self.label7=QLabel('Seed-Noid 動作可能')
       self.label7.setAlignment(Qt.AlignCenter)
       self.layout.addWidget(self.label7)
       self.label8=QLabel('AIREC 動作可能')
       self.label8.setAlignment(Qt.AlignCenter)
       self.layout.addWidget(self.label8)
       self.label7.setVisible(False)
       self.label8.setVisible(False)
       
       self.button1.clicked.connect(self.start_process1)
       self.button2.clicked.connect(self.start_process2)
       self.button3.clicked.connect(self.start_process3)
       self.button4.clicked.connect(self.start_process4)
       self.setLayout(self.layout)

   def start_process1(self):
       self.button1.setEnabled(False)
       self.button2.setEnabled(False)
       self.button3.setEnabled(False)
       self.button4.setEnabled(False)
       self.radio_button1.setEnabled(False)
       self.radio_button2.setEnabled(False)
       self.label7.setVisible(False)
       self.label8.setVisible(False)
              
       self.spinner.start()
       self.layout.addWidget(self.spinner)
       self.spinner.raise_()
       if self.radio_button1.isChecked()==True:
         self.label1=QLabel('Seed-Noid CollectModules...')
         self.label1.setAlignment(Qt.AlignCenter)
         self.layout.addWidget(self.label1)
         self.worker = WorkerThread1()
         self.worker.finished.connect(self.process_finished1)
         self.worker.start()
       else:
         self.label2=QLabel('AIREC CollectModules...')
         self.label2.setAlignment(Qt.AlignCenter)
         self.layout.addWidget(self.label2)
         self.worker = WorkerThread2()
         self.worker.finished.connect(self.process_finished2)
         self.worker.start()

   def start_process2(self):
       self.button1.setEnabled(False)
       self.button2.setEnabled(False)
       self.button3.setEnabled(False)
       self.button4.setEnabled(False)
       self.radio_button1.setEnabled(False)
       self.radio_button2.setEnabled(False)
       self.label7.setVisible(False)
       self.label8.setVisible(False)
       
       self.spinner.start()
       self.spinner.raise_()
       self.layout.addWidget(self.spinner)
       if self.radio_button1.isChecked()==True:
         self.label3=QLabel('Seed-Noid SystemBuild...')
         self.label3.setAlignment(Qt.AlignCenter)
         self.layout.addWidget(self.label3)
         self.worker = WorkerThread3()
         self.worker.finished.connect(self.process_finished3)
         self.worker.start()
       else:
         self.label4=QLabel('AIREC SystemBuild...')
         self.label4.setAlignment(Qt.AlignCenter)
         self.layout.addWidget(self.label4)
         self.worker = WorkerThread4()
         self.worker.finished.connect(self.process_finished4)
         self.worker.start()

   def start_process3(self):
       self.button1.setEnabled(False)
       self.button2.setEnabled(False)
       self.button3.setEnabled(False)
       self.button4.setEnabled(False)
       self.radio_button1.setEnabled(False)
       self.radio_button2.setEnabled(False)

       self.spinner.start()
       self.spinner.raise_()
       self.layout.addWidget(self.spinner)
       if self.radio_button1.isChecked()==True:
         self.label7.setVisible(False)
         self.label5=QLabel('Seed-Noid SystemRun...')
         self.label5.setAlignment(Qt.AlignCenter)
         self.layout.addWidget(self.label5)
         QTimer.singleShot(5000, self.stop_spinner5)
         os.chdir('/home/rsdlab/workspace/seedmover/_sy')
         self.result5 = subprocess.Popen(['./a_systemrun.sh'])
       else:
         self.label8.setVisible(False)
         self.label6=QLabel('AIREC SystemRun...')
         self.label6.setAlignment(Qt.AlignCenter)
         self.layout.addWidget(self.label6)
         QTimer.singleShot(5000, self.stop_spinner6)
         os.chdir('/home/rsdlab/workspace/seedmover/_sy')
         self.result6 = subprocess.Popen(['./b_systemrun.sh'])

   def start_process4(self):
       os.chdir('/home/rsdlab/workspace/seedmover/_sy')
       subprocess.Popen(['./stop.sh'])
       self.label7.setVisible(False)
       self.label8.setVisible(False)
       self.button1.setEnabled(True)
       self.button2.setEnabled(True)
       self.button3.setEnabled(False)
       self.radio_button1.setEnabled(True)
       self.radio_button2.setEnabled(True)
       self.button4.setEnabled(False)
   def process_finished1(self, returncode):
       self.spinner.stop()
       self.label1.hide()

       self.button1.setEnabled(True)
       self.button2.setEnabled(True)
       self.button3.setEnabled(True)
       self.button4.setEnabled(False)
       self.radio_button1.setEnabled(True)
       self.radio_button2.setEnabled(True)
       if returncode == 0:
           print('sucucess')
       else:
           print('failed')
   def process_finished2(self, returncode):
       self.spinner.stop()
       self.label2.hide()

       self.button1.setEnabled(True)
       self.button2.setEnabled(True)
       self.button3.setEnabled(True)
       self.button4.setEnabled(False)
       self.radio_button1.setEnabled(True)
       self.radio_button2.setEnabled(True)
       if returncode == 0:
           print('sucucess')
       else:
           print('failed')
   def process_finished3(self, returncode):
       self.spinner.stop()
       self.label3.hide()

       self.button1.setEnabled(True)
       self.button2.setEnabled(True)
       self.button3.setEnabled(True)
       self.button4.setEnabled(False)
       self.radio_button1.setEnabled(True)
       self.radio_button2.setEnabled(False)
       if returncode == 0:
           print('sucucess')
           
           
           
           
           
       else:
           print('failed')
   def process_finished4(self, returncode):
       self.spinner.stop()
       self.label4.hide()

       self.button1.setEnabled(True)
       self.button2.setEnabled(True)
       self.button3.setEnabled(True)
       self.button4.setEnabled(False)
       self.radio_button1.setEnabled(False)
       self.radio_button2.setEnabled(True)
       if returncode == 0:
           print('sucucess')
       else:
           print('failed')
   def stop_spinner5(self):
       self.spinner.stop()
       self.label5.hide()
    
       self.label7.setVisible(True)
       self.button1.setEnabled(False)
       self.button2.setEnabled(False)
       self.button3.setEnabled(False)
       self.button4.setEnabled(True)
       self.radio_button1.setEnabled(False)
       self.radio_button2.setEnabled(False)
   def stop_spinner6(self):
       self.spinner.stop()
       self.label6.hide()

       self.label8.setVisible(True)
       self.button1.setEnabled(False)
       self.button2.setEnabled(False)
       self.button3.setEnabled(False)
       self.button4.setEnabled(True)
       self.radio_button1.setEnabled(False)
       self.radio_button2.setEnabled(False)
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())
