from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import random


buttons=[]
def button_clicked(button):
    # button.setParent(None)
    print(button.column, button.row)
    text1 = button.text()
    i = button.row
    j = button.column
    if i!=0:
        text_up=buttons[i-1][j].text()
        if text1==text_up:
            buttons[i-1][j].setParent(None)
    if i!=len(buttons)-1:
        text_down=buttons[i+1][j].text()
        if text1==text_down:
            buttons[i+1][j].setParent(None)
    if j!=0:
        text_left=buttons[i][j-1].text()
        if text1==text_left:
            buttons[i][j-1].setParent(None)
    if j!=len(buttons)-1:
        text_right=buttons[i][j+1].text()
        if text1==text_right:
            buttons[i][j+1].setParent(None)









def create_button(x, y, window):
    c=random.randint(6,9)
    button=QPushButton()
    button.setFixedSize(30, 30)
    button.move(x,y)
    button.setText(str(c))
    window.layout().addWidget(button)
    button.clicked.connect(lambda: button_clicked(button))
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
    return button


def crate_button_rov(y,window, coluns, k):
    x=40
    for j in range(10):
        button=create_button(x,y, window)
        coluns.append(button)
        button.column=j
        button.row=k
        x=x+30


if __name__ == "__main__":
    app = QApplication([])

    window = QMainWindow()
    window.setFixedSize(400, 400)

    y=40
    for i in range(10):
        coluns=[]
        buttons.append(coluns)
        crate_button_rov(y,window, coluns, i)
        y=y+30


    # print(buttons)

    window.show()
    app.exec()