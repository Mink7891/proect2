import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel
import random
from PyQt5.QtCore import Qt, QTimer

buttons=[]
all_buttons_to_move = []
n=10
text=0
timers=[]
shethi=0
def add_new_buttons(button):
    global buttons
    global timers
    list_of_Tops=[]
    rezultat=[]
    count=random.randint(1,4)
    for i in range(10):
        if buttons[0][i] == None:
            list_of_Tops.append(i)


    for j in range(count):
        if len(list_of_Tops) == 0:
            break
        a=random.randint(0,len(list_of_Tops) - 1)
        rezultat.append(list_of_Tops[a])
        list_of_Tops.pop(a)

    buttons_to_move = set()
    all_buttons_to_move.append(buttons_to_move)

    for i in rezultat:
        if buttons[0][i] == None:
            a=i
            # print(a)
            x=70
            y=-1
            button=create_button(x+i*30,y, window)
            for j in range(10):
                if buttons[j][i] is not None:
                    y=buttons[j][i].y_new-30
                    # print(y)
                    buttons_to_move.add(button)
                    button.y_new = y
                    buttons[j-1][i]=button
                    button.row = j-1
                    button.column=i
                    break
                if j==9:
                    button.y_new = 370
                    buttons_to_move.add(button)
                    buttons[9][i]=button
                    button.row = 9
                    button.column=i

    timer =QTimer()
    timer.timeout.connect(lambda: walk_down(buttons_to_move, timer, new_buttons=True))
    timer.setInterval(5)
    timer.start()
    timers.append(timer)
def walk_down(buttons_set, timer, new_buttons=False):
    global timers
    buttons = list(buttons_set)
    buttons_new=set()
    for i in range(len(buttons)):
        x=buttons[i].x()
        y=buttons[i].y()
        # print(i)
        if buttons[i].y() >=buttons[i].y_new:
            buttons_new.add(buttons[i])
        if buttons[i] not in buttons_new:
            buttons[i].move(x,y+1)
        # print(len(buttons), len(buttons_new))
        if len(buttons)==len(buttons_new):
            timer.stop()
            timers.remove(timer)
            all_buttons_to_move.remove(buttons_set)
            if not new_buttons:
                add_new_buttons(buttons[i])




def button_clicked(button):
    global buttons
    global timers
    global shethi
    # print(button.column, button.row)
    i = button.row
    j = button.column
    walk(i,j)
    window.layout().addWidget(button)


    buttons_to_move = set()
    all_buttons_to_move.append(buttons_to_move)

    # for i in range(10):
    #     for j in range(10):
    #         if buttons[i][j] is not None:
    #             buttons[i][j].y_new =  buttons[i][j].y()

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
    if shethi>0:
        c=c-1
    else:
        return shethi
    button.setText(str(c))
    color(button)

    if c==0:
        buttonReply = QMessageBox.question(window,'PyQt5 message', "Ты выиграл! Хочешь начать заново?", QMessageBox.Yes | QMessageBox.No )
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        if buttonReply == QMessageBox.No:
            print('No clicked.')
            sys.exit()
    timer =QTimer()
    timer.timeout.connect(lambda: walk_down(buttons_to_move, timer))
    timer.setInterval(5)
    timer.start()
    timers.append(timer)
    shethi=0

def walk(i, j):
    global n
    global buttons
    global shethi
    global text
    button=buttons[i][j]
    parent = button.parent()
    button.setParent(None)
    if parent is None:
        return
    text1 = button.text()
    if i>0 and buttons[i-1][j] is not None:
        text_up=buttons[i-1][j].text()
        if text1==text_up:
            walk(i-1,j)
            shethi+=1
    if j>0 and buttons[i][j-1] is not None:
        text_left=buttons[i][j-1].text()
        if text1==text_left:
            walk(i,j-1)
            shethi+=1
    if i<n-1 and buttons[i+1][j] is not None:
        text_down=buttons[i+1][j].text()
        if text1==text_down:
            walk(i+1,j)
            shethi+=1
    if j<n-1 and buttons[i][j+1] is not None:
        text_right=buttons[i][j+1].text()
        if text1==text_right:
            walk(i,j+1)
            shethi+=1

    if shethi>0:
        text+=int(text1)
        # print(text)

    label.setText(str(text))

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
    x=70
    for j in range(10):
        button=create_button(x,y, window)
        coluns.append(button)
        button.column=j
        button.row=k
        x=x+30


if __name__ == "__main__":
    app = QApplication([])

    window = QMainWindow()
    window.setFixedSize(550, 450)
    # window.setStyleSheet('QMainWindow {background-color: black}')
    y=100
    for i in range(n):
        coluns=[]
        buttons.append(coluns)
        crate_button_rov(y,window, coluns, i)
        y=y+30


    for i in range(10):
        for j in range(10):
            if buttons[i][j] is not None:
                buttons[i][j].y_new =  buttons[i][j].y()


    label=QLabel()
    label.setFixedSize(100,50)
    label.move(400,225)
    label.setText(str(text))
    label.setStyleSheet('QLabel {background-color: silver}')
    window.layout().addWidget(label)

    window.show()
    app.exec()