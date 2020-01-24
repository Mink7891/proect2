from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import random




def create_button(x, y, window):
    c=random.randint(6,9)
    button=QPushButton()
    button.setFixedSize(30, 30)
    button.move(x,y)
    button.setText(str(c))
    window.layout().addWidget(button)
    if c==6:
        button.setStyleSheet('QPushButton {background-color: red}')
    elif c==7:
        button.setStyleSheet('QPushButton {background-color: green}')
    elif c==8:
        button.setStyleSheet('QPushButton {background-color: blue}')
    elif c==9:
        button.setStyleSheet('QPushButton {background-color: orange}')
    elif c==1:
        button.setStyleSheet('QPushButton {background-color: darkslateblue}')
    elif c==2:
        button.setStyleSheet('QPushButton {background-color: maroon}')
    elif c==3:
        button.setStyleSheet('QPushButton {background-color: rosybrown}')
    elif c==4:
        button.setStyleSheet('QPushButton {background-color: gold}')
    elif c==5:
        button.setStyleSheet('QPushButton {background-color: cyan}')

def crate_button_rov(y,window):
    x=40
    for i in range(10):
        create_button(x, y, window)
        x=x+30


if __name__ == "__main__":
    app = QApplication([])

    window = QMainWindow()
    window.setFixedSize(400, 400)

    y=40
    for i in range(10):
        crate_button_rov(y,window)
        y=y+30



    window.show()
    app.exec()