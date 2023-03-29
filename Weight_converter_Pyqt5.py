import sys,webbrowser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QWidget):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.resize(1800,450)
      self.setWindowTitle("PyQt5")
      self.label = QLabel(self)
      
      
      op=int(input("Choose option 1 or 2 !!"))
      if op==1:
          k=input("Enter weight in Kg")
          p=(int(k)/.453592)
          
          self.label.setText(str(k)+"Pounds"+" \n"+str(p)+"kilogram")
      if op==2:
          k=input("Enter Weight in Pounds")
          p=(int(k)*.453592)
          self.label.setText(str(k)+"lbs"+" \n"+str(p)+"kilograms")
          
      else:
          self.label.setText("Choose option 1 or 2 Nigga\n")
          
          webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
          
          
          
          
          
      
      self.label.move(50,20)
      
      
      font = QFont()
      font.setFamily("Arial")
      font.setPointSize(80)
      self.label.setFont(font)
      self.label.move(50,20)
def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()
