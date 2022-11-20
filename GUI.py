import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('기압입력(hPa): ')
        self.spinbox = QDoubleSpinBox()
        self.spinbox.setMinimum(-1000)
        self.spinbox.setMaximum(3000)
        self.spinbox.setSingleStep(0.1)
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.spinbox)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('층 계산기')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
        btn1 = QPushButton('확인', self)
        btn1.setCheckable(True)
        btn1.toggle()
        btn1.clicked.connect(self.btnRun_clicked)	
        vbox.addWidget(btn1)


    
    def btnRun_clicked(self):
        self.a=self.spinbox.value()
        strr="층 입니다!"
        flr=(self.a- 1019.484819977867)/ -0000.353997785379;
        floor=round(flr);
        QMessageBox.about(self, " ",str(floor) + strr)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
