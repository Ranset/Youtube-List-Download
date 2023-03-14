from PySide2.QtWidgets import QApplication, QMessageBox

def message_box():
  msg = QMessageBox()
  msg.setIcon(QMessageBox.Information)
  msg.setText("This is a message box")
  msg.setInformativeText("This is additional information")
  msg.setWindowTitle("MessageBox demo")
#   msg.setDetailedText("The details are as follows:")
  msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
  msg.buttonClicked.connect(msgbtn)
  retval = msg.exec_()
  print(retval)
  
def msgbtn(i):
  print("Button pressed is:",i.text())

app = QApplication([])
message_box()
app.exec_()