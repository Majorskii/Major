import sys 
from PyQt5 import QtWidgets 
 
# 1. Создаем класс Question 
class Question: 
    def __init__(self, question_text, answer_options, correct_answer): 
        self.question_text = question_text 
        self.answer_options = answer_options 
        self.correct_answer = correct_answer 
 
class QuizApp(QtWidgets.QWidget): 
    def __init__(self): 
        super().__init__() 
 
        # 1. Структура хранения вопросов 
        self.questions = [ 
            Question("Какой цвет неба?", ["Синий", "Зеленый", "Красный"], "Синий"), 
            Question("Сколько дней в неделе?", ["5", "6", "7"], "7"), 
            Question("Что такое Python?", ["Язык программирования", "Животное", "Книга"], "Язык программирования"), 
        ] 
         
        self.current_question_index = 0 
        self.initUI() 
 
    def initUI(self): 
        self.setWindowTitle("Memory Card") 
        self.setGeometry(100, 100, 400, 300) 
 
        self.question_label = QtWidgets.QLabel("", self) 
        self.question_label.setGeometry(20, 20, 360, 50) 
 
        self.answer_buttons = [QtWidgets.QPushButton("", self) for _ in range(3)] 
        for i, button in enumerate(self.answer_buttons): 
            button.setGeometry(20, 80 + i * 40, 360, 30) 
            button.clicked.connect(self.click_ok) 
 
        self.show_question()  # Показать первый вопрос 
 
    def show_question(self): 
        question = self.questions[self.current_question_index] 
        self.question_label.setText(question.question_text) 
        for i, button in enumerate(self.answer_buttons): 
            button.setText(question.answer_options[i]) 
            button.show() 
        self.question_label.show() 
 
    def click_ok(self): 
        self.check_answer()  # Здесь можно добавить логику проверки ответа 
        self.next_question()  # Переход к следующему вопросу 
 
    def check_answer(self): 
        # Логика проверки правильного ответа — можно добавить уведомление о правильном ответе 
        current_question = self.questions[self.current_question_index] 
        # Получаем текст нажатой кнопки для проверки 
        selected_answer = self.sender().text() 
        if selected_answer == current_question.correct_answer: 
            print("Ответ правильный!") 
        else: 
            print("Ответ неправильный! Правильный ответ:", current_question.correct_answer) 
 
    def next_question(self): 
        self.current_question_index += 1 
        if self.current_question_index >= len(self.questions): 
            self.current_question_index = 0  # Сброс счетчика 
        self.show_question() 
 
if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv) 
    ex = QuizApp() 
    ex.show() 
    sys.exit(app.exec_())


