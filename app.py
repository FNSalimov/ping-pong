from PyQt4 import QtGui, QtCore
import sys, os, design, start

class App(QtGui.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super(App, self).__init__()
		self.setupUi(self)
		#self.show()
		self.time_id = 0
		self.speed = 5
		self.max_score = 0
		self.time_id = self.startTimer(self.speed)
		self.x, self.y = self.radioButton.x(), self.radioButton.y()
		self.x_bool, self.y_bool = True, True
		#self.label.setGeometry(QtCore.QRect(0, 0, 31, 131))
		self.setFocus(True)
		self.pause = False
	def timerEvent(self, event):
		if self.radioButton.x() >= 505:
			self.label_3.setText(str(int(self.label_3.text()) + 1))
			if int(self.label_3.text()) == self.max_score:
				QtGui.QMessageBox.information(start_form, "Congratulations!", self.label_5.text() + " has won!", QtGui.QMessageBox.Ok)
				self.label_3.setText('0')
				self.label_4.setText('0')
		if self.radioButton.x() <= 0:
			self.label_4.setText(str(int(self.label_4.text()) + 1))
			if int(self.label_4.text()) == self.max_score:
				QtGui.QMessageBox.information(start_form, "Error", self.label_6.text() + " has won!", QtGui.QMessageBox.Ok)
				self.label_3.setText('0')
				self.label_4.setText('0')
		if self.radioButton.x() >= 505 or (self.label_2.x() in range(self.radioButton.x(), self.radioButton.x() + 21) and self.radioButton.y() in range(self.label_2.y(), self.label_2.y() + 131)):
			self.x_bool = False
		elif self.radioButton.x() <= 0 or (self.label.x() in range(self.radioButton.x(), self.radioButton.x() + 21) and
							(self.radioButton.y() in range(self.label.y(), self.label.y() + 131)
							or (self.radioButton.y() + 21) in range(self.label.y(), self.label.y() + 131))):
			self.x_bool = True
		if self.radioButton.y() >= 430:
			self.y_bool = False
		elif self.radioButton.y() <= 0:
			self.y_bool = True
		if self.x_bool:
			self.x += 1
		if not self.x_bool:
			self.x -= 1
		if self.y_bool:
			self.y += 1
		if not self.y_bool:
			self.y -= 1
		self.radioButton.setGeometry(QtCore.QRect(self.x, self.y, 20, 30))
	def keyPressEvent(self, event):
		#print(self.time_id)
		if event.key() == 81:
			self.killTimer(self.time_id)
			if self.speed > 1:
				self.speed -= 1
			self.time_id = self.startTimer(self.speed)
		if event.key() == 65:
			self.killTimer(self.time_id)
			if self.speed < 7:
				self.speed += 1
			self.time_id = self.startTimer(self.speed)
		if event.key() == 80:
			if not self.pause:
				self.pause = True
				self.killTimer(self.time_id)
			else:
				self.pause = False
				self.time_id = self.startTimer(self.speed)
		#print(event.key())
		if event.key() == 16777235 and self.label.y() >= 0:
			self.label.setGeometry(QtCore.QRect(20, self.label.y() - 10, 5, 131))
		elif event.key() == 16777237 and self.label.y() <= 460 - 131:
			self.label.setGeometry(QtCore.QRect(20, self.label.y() + 10, 5, 131))
		if event.key() == 87 and self.label_2.y() >= 0:
			self.label_2.setGeometry(QtCore.QRect(500, self.label_2.y() - 10, 5, 131))
		if event.key() == 83 and self.label_2.y() <= 460 - 131:
			self.label_2.setGeometry(QtCore.QRect(500, self.label_2.y() + 10, 5, 131))
		if self.label.y() < 0:
			self.label.setGeometry(QtCore.QRect(20, 0, 5, 131))
		if self.label_2.y() < 0:
			self.label_2.setGeometry(QtCore.QRect(500, 0, 5, 131))

class Opp(QtGui.QMainWindow, start.Ui_MainWindow):
	def __init__(self):
		super(Opp, self).__init__()
		self.setupUi(self)

def start():
	global form, start_form, first_player, second_player, max_score
	first_player, second_player = start_form.lineEdit.text(), start_form.lineEdit_2.text()
	flag = 1
	if first_player == '' or second_player == '':
		flag = 0
	try:
		max_score = int(start_form.lineEdit_3.text())
	except ValueError:
		flag = 0
	if flag:
		if max_score > 0:
			start_form.hide()
			form.label_5.setText(first_player)
			form.label_6.setText(second_player)
			form.max_score = max_score
			form.label_3.setText('0'), form.label_4.setText('0')
			form.show()
		else:
			flag = 0
	if not flag:
		QtGui.QMessageBox.information(start_form, "Error", "Please enter correct data:first_player and second_player-not blank line, max_score-positive integer", QtGui.QMessageBox.Ok)
app = QtGui.QApplication(sys.argv)
form = App()
start_form = Opp()
start_form.show()
first_player, second_player, max_score = '', '', 0
start_form.pushButton.clicked.connect(start)
sys.exit(app.exec_())
