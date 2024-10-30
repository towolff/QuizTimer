"""
This code is fully generated with ChatGPT with the following prompt (german):
'Erstelle mir eine GUI in pyQt bei der man zunächst eine Anzahl an Fragen sowie eine Zeit definieren kann. 
Man kann auf Start drücken, sodass dann der Countdown basierend auf der eingegebenen Zeit runterläuft. 
Basierend auf der Anzahl der Fragen und der definierten Zeit soll angezeigt werden, 
wie viel Minuten man pro Frage zeit hat (also Zeit/Anzahl Fragen). Es soll einen Button geben, 
mit dem man sagen kann, dass man eine Frage beantwortet hat. In einem weiteren Feld soll dann angezeigt werden, 
wie viel Zeit man gewonnen hat, wenn man also 30 Fragen und 60 Minuten hat, hat man 2 Minuten pro Frage Zeit. 
Wenn man eine Frage in nur einer Minute beantwortet, hat man eine Minute gewonnen. Dies soll angezeigt werden.'
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QSpinBox,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtCore import QTimer


class QuizTimer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.time_per_question = 0
        self.remaining_time = 0
        self.answered_questions = 0
        self.total_saved_time = 0

    def initUI(self):
        # Eingabefelder für Anzahl der Fragen und Zeit in Minuten
        self.question_label = QLabel("Anzahl der Fragen:")
        self.question_count_input = QSpinBox()
        self.question_count_input.setRange(1, 100)

        self.time_label = QLabel("Zeit in Minuten:")
        self.time_input = QSpinBox()
        self.time_input.setRange(1, 999)

        # Button für den Start des Countdowns
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_quiz)

        # Countdown-Label
        self.timer_label = QLabel("Verbleibende Zeit:")
        self.timer_display = QLabel("00:00")

        # Anzeige für gewonnene Zeit und Zeit pro Frage
        self.time_per_question_label = QLabel("Zeit pro Frage: 0 Minuten")
        self.saved_time_label = QLabel("Gewonnene Zeit: 0 Minuten")

        # Button für beantwortete Fragen
        self.answer_button = QPushButton("Frage beantwortet")
        self.answer_button.clicked.connect(self.answer_question)
        self.answer_button.setEnabled(False)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.question_label)
        layout.addWidget(self.question_count_input)
        layout.addWidget(self.time_label)
        layout.addWidget(self.time_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.timer_display)
        layout.addWidget(self.time_per_question_label)
        layout.addWidget(self.saved_time_label)
        layout.addWidget(self.answer_button)

        self.setLayout(layout)
        self.setWindowTitle("Quiz Timer")

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def start_quiz(self):
        # Zeit und Fragenanzahl setzen
        total_questions = self.question_count_input.value()
        total_time = self.time_input.value()

        self.time_per_question = total_time / total_questions
        self.time_per_question_label.setText(
            f"Zeit pro Frage: {self.time_per_question:.2f} Minuten"
        )

        # Countdown-Zeit in Sekunden berechnen
        self.remaining_time = total_time * 60
        self.update_display()

        # Timer starten
        self.timer.start(1000)  # 1 Sekunde Intervall
        self.start_button.setEnabled(False)
        self.answer_button.setEnabled(True)

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_display()
        else:
            self.timer.stop()
            self.timer_display.setText("Zeit abgelaufen!")
            self.answer_button.setEnabled(False)

    def update_display(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_display.setText(f"{minutes:02}:{seconds:02}")

    def answer_question(self):
        # Zeit pro Frage in Sekunden
        question_time = self.time_per_question * 60

        # Zeit sparen, wenn schneller beantwortet
        saved_time = (
            question_time
            - (self.time_input.value() * 60 - self.remaining_time) % question_time
        )
        if saved_time > 0:
            self.total_saved_time += saved_time / 60  # In Minuten umrechnen
            self.saved_time_label.setText(
                f"Gewonnene Zeit: {self.total_saved_time:.2f} Minuten"
            )

        # Beantwortete Fragen zählen
        self.answered_questions += 1
        if self.answered_questions >= self.question_count_input.value():
            self.timer.stop()
            self.timer_display.setText("Quiz beendet")
            self.answer_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz_timer = QuizTimer()
    quiz_timer.show()
    sys.exit(app.exec())
