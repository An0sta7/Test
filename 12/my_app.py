from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong2 = wrong2
        self.wrong1 = wrong1
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии','Португальский',"Английский", "Испанский","Бразильский"))
question_list.append(Question('Кокого цвета нет на флаге России?',"Зеленого","Красный","Синий","Белый"))
question_list.append(Question('Кто открыл Америку?',"Тимофей","Колумб","Есенин","Наполеон"))
app = QApplication([]) #Создаем приложение
window = QWidget()#Создаем окно
window.setWindowTitle('Test')#Название окна

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году была основана Москва?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1148')
rbtn_3 = QRadioButton('1149')
rbtn_4 = QRadioButton('1146')

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()#вертикальные линии будут внутри горизонтальных
layout3 = QVBoxLayout()
layout2.addWidget(rbtn_1)#два ответа в первый столбец
layout2.addWidget(rbtn_2)
layout3.addWidget(rbtn_3)#Два ответа во второй столбец 
layout3.addWidget(rbtn_4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)#Разместили столбцы в одной строке

RadioGroupBox.setLayout(layout1)

AnsGroupBox = QGroupBox('')
lb_Result = QLabel('')
lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res) 

line1 = QHBoxLayout()#вопрос
line2 = QHBoxLayout()#варианты ответов или результат теста
line3 = QHBoxLayout()#кнопка "ответить"

line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
line3.addWidget(btn_OK)

card = QVBoxLayout()
card.addLayout(line1)
card.addLayout(line2)
card.addLayout(line3)


window.setLayout(card)

def show_result():
#Показывать понель ответов
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():#показать панель вопросов
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')#Сбросить радио кнопку
    #RadioGroupBox.setExslusive()
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    #Функция записывает значения вопроса и ответов в соотверствующие виджеты
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_corret(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_corret('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_corret('Неверно')

def next_question():
    #Задает случаеный вопрос из списка
    #Этой функции нужна переменная, в которой будет указываться номер текущего вопроса
    #Эту переменную можно сделать свойством "глобального объекта"
    window.cur_question = window.cur_question + 1 #переходим к след вопросу
    if window.cur_question >= len(question_list):
        window.cur_question = 0 #Если список вопросов закончился - идем сначала
    q = question_list[window.cur_question] #взяли вопрос
    ask(q) #спросили


def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.resize(400,200)
#Текущий вопрос из списка сделали свойством объекта "окно"
window.cur_question = -1
btn_OK.clicked.connect(click_OK)#По нажатию выбираем 
next_question()
window.show()
app.exec()