"""
This code is fully generated with ChatGPT.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QSpinBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont, QColor, QPalette


class QuizTimer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.time_per_question = 0
        self.remaining_time = 0
        self.answered_questions = 0
        self.total_saved_time = 0

    def initUI(self):
        # Set window properties
        self.setWindowTitle("Quiz Timer")
        self.setFixedSize(400, 300)

        # Set dark background color
        palette = self.palette()
        palette.setColor(
            QPalette.ColorRole.Window, QColor("#2c2f33")
        )  # Dark background color
        palette.setColor(
            QPalette.ColorRole.WindowText, QColor("#ffffff")
        )  # White text color
        self.setPalette(palette)

        # Set font styles
        header_font = QFont("Arial", 12, QFont.Weight.Bold)
        countdown_font = QFont("Arial", 24, QFont.Weight.Bold)

        # Layout for question count
        question_layout = QHBoxLayout()
        self.question_label = QLabel("Number of questions:")
        self.question_label.setFont(header_font)
        self.question_label.setStyleSheet("color: #ffffff;")  # White text color
        self.question_count_input = QSpinBox()
        self.question_count_input.setRange(1, 100)
        question_layout.addWidget(self.question_label)
        question_layout.addWidget(self.question_count_input)

        # Layout for time input
        time_layout = QHBoxLayout()
        self.time_label = QLabel("Time in minutes:")
        self.time_label.setFont(header_font)
        self.time_label.setStyleSheet("color: #ffffff;")  # White text color
        self.time_input = QSpinBox()
        self.time_input.setRange(1, 999)
        time_layout.addWidget(self.time_label)
        time_layout.addWidget(self.time_input)

        # Button to start the countdown
        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet(
            "background-color: #7289da; color: white; padding: 5px; font-size: 12px;"
        )
        self.start_button.clicked.connect(self.start_quiz)

        # Countdown label
        self.timer_label = QLabel("Remaining time:")
        self.timer_label.setFont(header_font)
        self.timer_label.setStyleSheet("color: #ffffff;")
        self.timer_display = QLabel("00:00")
        self.timer_display.setFont(countdown_font)
        self.timer_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_display.setStyleSheet("color: #ffffff;")

        # Display for time saved and time per question
        self.time_per_question_label = QLabel("Time per question: 0 minutes")
        self.time_per_question_label.setFont(QFont("Arial", 10))
        self.time_per_question_label.setStyleSheet("color: #ffffff;")
        self.saved_time_label = QLabel("Saved time: 0 minutes")
        self.saved_time_label.setFont(QFont("Arial", 10))
        self.saved_time_label.setStyleSheet("color: #ffffff;")

        # Button for answered questions
        self.answer_button = QPushButton("Question answered")
        self.answer_button.setStyleSheet(
            "background-color: #f04747; color: white; padding: 5px; font-size: 12px;"
        )
        self.answer_button.clicked.connect(self.answer_question)
        self.answer_button.setEnabled(False)

        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        layout.addLayout(question_layout)
        layout.addLayout(time_layout)
        layout.addWidget(self.start_button)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.timer_display)
        layout.addWidget(self.time_per_question_label)
        layout.addWidget(self.saved_time_label)
        layout.addWidget(self.answer_button)

        self.setLayout(layout)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def start_quiz(self):
        # Set time and question count
        total_questions = self.question_count_input.value()
        total_time = self.time_input.value()

        self.time_per_question = total_time / total_questions
        self.time_per_question_label.setText(
            f"Time per question: {self.time_per_question:.2f} minutes"
        )

        # Calculate countdown time in seconds
        self.remaining_time = total_time * 60
        self.update_display()

        # Start timer
        self.timer.start(1000)  # 1 second interval
        self.start_button.setEnabled(False)
        self.answer_button.setEnabled(True)

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_display()
        else:
            self.timer.stop()
            self.timer_display.setText("Time's up!")
            self.answer_button.setEnabled(False)

    def update_display(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_display.setText(f"{minutes:02}:{seconds:02}")

    def answer_question(self):
        # Time per question in seconds
        question_time = self.time_per_question * 60

        # Save time if answered quicker
        saved_time = (
            question_time
            - (self.time_input.value() * 60 - self.remaining_time) % question_time
        )
        if saved_time > 0:
            self.total_saved_time += saved_time / 60  # Convert to minutes
            self.saved_time_label.setText(
                f"Saved time: {self.total_saved_time:.2f} minutes"
            )

        # Count answered questions
        self.answered_questions += 1
        if self.answered_questions >= self.question_count_input.value():
            self.timer.stop()
            self.timer_display.setText("Quiz completed")
            self.answer_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz_timer = QuizTimer()
    quiz_timer.show()
    sys.exit(app.exec())
