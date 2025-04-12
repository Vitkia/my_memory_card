#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
                            QHBoxLayout, QVBoxLayout, 
                            QGroupBox, QRadioButton, 
                            QPushButton, QLabel,QButtonGroup)
from random import *
#Варианты ответа
#app
app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Memory Card')
btn_ok = QPushButton('ответить')
lbl_question = QLabel('..?')

#
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
     


question_list = []
question_list.append(Question('С каким микроорганизмом борются антибиотиками?', "Бактерия стрептококк", "Грип", 'Вирус ветряной оспы', "вирус HIV"))
question_list.append(Question('В каком контейнере будут расти микробы?', "яблоко в воде", "яблоко в соле", 'яблоко в уксусе', "яблоко в антисептике"))
question_list.append(Question('Что является неправильным способом профилактики гриппа?', "приветствие рукопожатием или поцелуем", "мытье рук", 'Ношение маски', "использование носовых платков"))
question_list.append(Question('Достаточно ли мыть руки только водой?', "нет, нужно мыло", "да, достаточно", 'Может быть?', "Мыть руки не надо!!"))
question_list.append(Question('я не знаю :(', "yipee", ":c", ':(', ":["))




RadioGroupBox = QGroupBox('posible ans')

#answers
btn_ans1 = QRadioButton('pa')
btn_ans2 = QRadioButton('pa')
btn_ans3 = QRadioButton('pa')
btn_ans4 = QRadioButton('pa')

#group answers
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

#vertical layout
line_v1 = QVBoxLayout()
line_v2 = QVBoxLayout()
#horizontal
line_h1 = QHBoxLayout()

line_v1.addWidget(btn_ans1)
line_v1.addWidget(btn_ans3)
line_v2.addWidget(btn_ans2)
line_v2.addWidget(btn_ans4)

line_h1.addLayout(line_v1)
line_h1.addLayout(line_v2)

RadioGroupBox.setLayout(line_h1)

#///////////////////////////////////////////////

#Форма правильнхого орвета

AnsGroupBox = QGroupBox('result')
lbl_res = QLabel('yay or nay?')
lbl_correct = QLabel('answer')

line_res = QVBoxLayout()
line_res.addWidget(lbl_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
line_res.addWidget(lbl_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(line_res)

line_h2 = QHBoxLayout()
line_h3 = QHBoxLayout()
line_h4 = QHBoxLayout()

line_h2.addWidget(lbl_question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line_h3.addWidget(RadioGroupBox)
line_h3.addWidget(AnsGroupBox)
AnsGroupBox.hide()

line_h4.addStretch(1)
line_h4.addWidget(btn_ok, stretch=2)
line_h4.addStretch(1)

m_line = QVBoxLayout()

m_line.addLayout(line_h2, stretch=2)
m_line.addLayout(line_h3, stretch=8)
m_line.addStretch(1)
m_line.addLayout(line_h4, stretch=1)
m_line.addStretch(1)
m_line.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("продолжить")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("ответить")
    RadioGroup.setExclusive(False)
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
    RadioGroup.setExclusive(True)
    
answers = [btn_ans1, btn_ans2, btn_ans3, btn_ans4]

def show_correct(res):
    lbl_res.setText(res)
    show_result()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl_question.setText(q.question) #???????
    lbl_correct.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        mw.score += 1
        show_correct('Corect!')
        print('stat\n all:', mw.total, '\n corec:', mw.score)
        print('Rating:', (mw.score/mw.total)*100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('wrong')
        print('Rating:', (mw.score/mw.total)*100, '%')

def next_question():
    mw.total += 1
    print('stats\n all:', mw.total, '\n corect:', mw.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_ok():
    if btn_ok.text() == "ответить":
        check_answer()
    else:
        next_question()


btn_ok.clicked.connect(click_ok)

#window set up\
mw.total = 0
mw.score = 0
next_question()
mw.resize(600,500)
mw.setLayout(m_line)
mw.show()

#app exit
app.exec_()































