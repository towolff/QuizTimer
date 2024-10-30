# Quiz Timer Application
This README as well as the entire code was generated using ChatGPT!

## Overview
The Quiz Timer is a simple GUI application built with PyQt6 (and ChatGPT) to help users manage timed quizzes. The app allows users to:
1. Set the number of questions.
2. Define a total time limit for the quiz.
3. Calculate time allowed per question based on the input values.
4. Track remaining time with a live countdown.
5. Mark questions as answered and keep track of time saved.

This application is perfect for practicing timed quizzes, self-study sessions, or any scenario where you need to manage time effectively across multiple questions.

## Features
- **Set Quiz Parameters**: Input the number of questions and the total time limit in minutes.
- **Start Quiz Countdown**: A timer begins counting down from the specified time, calculating time per question.
- **Track Time per Question**: Displayed time allocation per question.
- **Time Saved Display**: For each question answered before the time limit, the saved time is calculated and displayed.

## Requirements
- **Python 3.x** 
- **PyQt6** (Installed automatically via the script)

## Quick Start

To quickly set up and run the application, use the `run.sh` script, which:
1. Creates a virtual environment.
2. Activates the environment.
3. Installs the required dependencies.
4. Runs the Quiz Timer application.

### Instructions

1. **Clone the repository** or download the files into a directory.
2. **Ensure you have Python 3.x** installed on your machine.

### Running the Application

1. **Make the script executable** (only required once):
   ```bash
   chmod +x run_quiz_timer.sh
