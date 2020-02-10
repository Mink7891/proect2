from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import random
from PyQt5.QtCore import Qt, QTimer

buttons=[]
n=10

def button_clicked(button):
    global buttons
    print(button.column, button.row)
    i = button.row
    j = button.column
    walk(i,j)

    window.layout().addWidget(button)
    for k in range(10):
        i=8
        while i>=0:
            j=9
            while j>=0:
                if buttons[i+1][j].parent()==None:
                    a=i
                    while a>=0:
                        # print("[" + str(a) + ", " + str(j) + "]", end=" ")
                        x=buttons[a][j].x()
                        y=buttons[a][j].y()
                        buttons[a+1][j]=buttons[a][j]
                        buttons[a][j].move(x,y+30)
                        buttons[a][j].row += 1
                        a=a-1
                    # print()
                j=j-1
            i=i-1


def walk(i, j):
    global n
    global buttons
    button=buttons[i][j]
    parent = button.parent()
    button.setParent(None)
    text1 = button.text()

    if parent is None:
        return
    if i>0:
        text_up=buttons[i-1][j].text()
        if text1==text_up:
            walk(i-1,j)
    if j>0:
        text_left=buttons[i][j-1].text()
        if text1==text_left:
            walk(i,j-1)
    if i<n-1:
        text_down=buttons[i+1][j].text()
        if text1==text_down:
         walk(i+1,j)
    if j<n-1:
        text_right=buttons[i][j+1].text()
        if text1==text_right:
         walk(i,j+1)








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
    for i in range(n):
        coluns=[]
        buttons.append(coluns)
        crate_button_rov(y,window, coluns, i)
        y=y+30




    # print(buttons)

    window.show()
    app.exec()