from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import random
from PyQt5.QtCore import Qt, QTimer

buttons=[]
button_move=[]
buttons_to_move = set()
n=10
timer=None
def walk_down(buttons_set):
    global buttons_to_move
    buttons = list(buttons_set)
    buttons_new=set()
    for i in range(len(buttons)):
        x=buttons[i].x()
        y=buttons[i].y()
        if buttons[i].y() ==buttons[i].y_new:
            buttons_new.add(buttons[i])
        if buttons[i] not in buttons_new:
            buttons[i].move(x,y+1)
        # print(len(buttons), len(buttons_new))
        if len(buttons)==len(buttons_new):
            timer.stop()
            buttons_to_move=set()


def button_clicked(button):
    global buttons
    global timer
    print(button.column, button.row)
    i = button.row
    j = button.column
    walk(i,j)

    window.layout().addWidget(button)

    for i in range(10):
        for j in range(10):
            if buttons[i][j] is not None:
                buttons[i][j].y_new = None

    for k in range(10):
        i=8
        while i>=0:
            j=9
            while j>=0:
                if buttons[i+1][j] is not None and buttons[i+1][j].parent()==None:
                    a=i
                    while a>=0:
                        if buttons[a][j] == None:
                            buttons[a+1][j] = None
                            break
                        # print("[" + str(a) + ", " + str(j) + "]", end=" ")
                        x=buttons[a][j].x()
                        y=buttons[a][j].y()
                        buttons[a+1][j]=buttons[a][j]
                        buttons_to_move.add(buttons[a][j])
                        if buttons[a][j].y_new is None:
                            buttons[a][j].y_new=y+30
                        else:
                            buttons[a][j].y_new += 30
                        # buttons[a][j].move(x,button.y_new)
                        buttons[a][j].row += 1
                        if a == 0:
                            buttons[a][j] = None
                        a=a-1
                j=j-1
            i=i-1







    c=int(button.text())
    c=c-1
    button.setText(str(c))
    color(button)
    if c==0:
        window.close()
        print("GGWP")

    timer =QTimer()
    timer.timeout.connect(lambda: walk_down(buttons_to_move))
    timer.setInterval(30)
    timer.start()


def walk(i, j):
    global n
    global buttons
    button=buttons[i][j]
    parent = button.parent()
    button.setParent(None)
    text1 = button.text()

    if parent is None:
        return
    if i>0 and buttons[i-1][j] is not None:
        text_up=buttons[i-1][j].text()
        if text1==text_up:
            walk(i-1,j)
    if j>0 and buttons[i][j-1] is not None:
        text_left=buttons[i][j-1].text()
        if text1==text_left:
            walk(i,j-1)
    if i<n-1 and buttons[i+1][j] is not None:
        text_down=buttons[i+1][j].text()
        if text1==text_down:
         walk(i+1,j)
    if j<n-1 and buttons[i][j+1] is not None:
        text_right=buttons[i][j+1].text()
        if text1==text_right:
         walk(i,j+1)





def color(button):
    c=int(button.text())
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

def create_button(x, y, window):
    button=QPushButton()
    button.setFixedSize(30, 30)
    button.move(x,y)
    c=random.randint(6,9)
    button.setText(str(c))
    color(button)
    window.layout().addWidget(button)
    button.clicked.connect(lambda: button_clicked(button))
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
    window.setStyleSheet('QMainWindow {background-color: black}')
    y=40
    for i in range(n):
        coluns=[]
        buttons.append(coluns)
        crate_button_rov(y,window, coluns, i)
        y=y+30


    window.show()
    app.exec()