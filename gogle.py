from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QHBoxLayout,QGroupBox,QVBoxLayout,QRadioButton,QButtonGroup,QPushButton,QLabel)
from random import shuffle, randint

app=QApplication([])
window=QWidget()
window.setWindowTitle("Memory Card")

window.cur_question=-1

lb_Question=QLabel("В каком году основали Москву")
btn_OK=QPushButton("Ответить")

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()

layout_line1.addWidget(lb_Question)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

AnsGroupBox=QGroupBox("Правильно\Неправильно")
right_answer=QLabel("В 1147")
v_layout=QVBoxLayout()
v_layout.addWidget(right_answer,alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
AnsGroupBox.setLayout(v_layout)

RadioGroupBox=QGroupBox("Варианты ответов")
rbtn_1=QRadioButton("1147")
rbtn_2=QRadioButton("2023")
rbtn_3=QRadioButton("1945")
rbtn_4=QRadioButton("1657")

RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

class Question():
    def __init__(self,question,right,wrong1,wrong2,wrong3):
        self.question=question
        self.right=right
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3
q=Question("На какой планете мы живем?","Земля","Марс","Юпитер","Уран")

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(RadioGroupBox)

layout_main=QVBoxLayout()
layout_main.addLayout(layout_line1)

layout_main.addStretch(1)
layout_main.addLayout(layout_line2)
layout_main.addStretch(1)
layout_main.addLayout(layout_line3)
window.setLayout(layout_main)
window.total=0
window.score=0

def next_question():
    window.total+=1
    cur_question=randint(0,len(questions_list)-1)
    q=questions_list[cur_question]
    ask(q)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    right_answer.setText(q.right)
    show_question()

def show_correct(res):
    right_answer.setText(res)
    show_result()

def chek_answer():
    if answers[0].isChecked():
        show_correct("Правильно")
        window.score+=1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неправильно")

questions_list=[]
questions_list.append(
    Question("Сколько оффицальных алфовитов в японском языке?","2","1","3","4",))
questions_list.append(q)

def click_OK():
    print("-Стастика")
    print(f"Всего вопросов: {window.total}")
    print(f"Правильных ответов: {window.score}")
    print(f"Рейтинг: {window.score/window.total*100}%")
    if btn_OK.text()=="Ответить":
        chek_answer()
    else:
        next_question()

btn_OK.clicked.connect(click_OK)
next_question()

window.show()
app.exec_()
