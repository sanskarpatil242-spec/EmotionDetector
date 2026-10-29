# Emotion Detector

An AI-powered web application that analyzes user-submitted English text to predict emotional sentiment across five primary emotions—**anger**, **disgust**, **fear**, **joy**, and **sadness**—and identifies the **dominant emotion**.

This project is developed as part of the **Coursera: Developing AI Applications with Python and Flask** course (IBM Applied AI / Backend Developer Professional Certificate).

---

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running Unit Tests](#running-unit-tests)
- [Running the Flask Application](#running-the-flask-application)
- [API Specification](#api-specification)
- [Static Code Analysis](#static-code-analysis)

---

## Overview

The application integrates with the Watson NLP Emotion Predict service to perform sentiment and emotion analysis. It packages the core AI functionality into a reusable Python module named `EmotionDetection`, exposes an intuitive web interface built with Flask, and includes comprehensive error handling for blank inputs and invalid API responses (HTTP status code 400).

---

## Technologies Used

- **Python 3**: Core application programming language
- **Flask**: Lightweight web framework for application routing and interface rendering
- **Watson NLP Runtime API**: Embeddable AI service for emotional sentiment prediction
- **Requests**: HTTP library for communicating with the Watson NLP REST service
- **Unittest**: Built-in Python testing framework for test-driven development and verification
- **Pylint**: Static code analysis tool enforcing PEP 8 standards and code quality

---

## Project Structure

```text
EmotionDetector/
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
├── emotion_detection.py
├── server.py
├── test_emotion_detection.py
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   ├── mywebscript.js
│   └── style.css
└── templates/
    └── index.html
```

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sanskarpatil242-spec/EmotionDetector.git
   cd EmotionDetector
   ```

2. **Create and Activate a Virtual Environment** (recommended):
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running Unit Tests

To run the automated unit test suite:

```bash
python -m unittest -v test_emotion_detection.py
```

The test suite validates:
- Dominant emotion predictions for standard benchmark statements:
  - `"I am glad this happened"` -> `joy`
  - `"I am really mad about this"` -> `anger`
  - `"I feel disgusted just hearing about this"` -> `disgust`
  - `"I am so sad about this"` -> `sadness`
  - `"I am really afraid that this will happen"` -> `fear`
- Output dictionary keys and data types.
- HTTP status code 400 and empty text error handling (returning `None` for all emotion scores).

---

## Running the Flask Application

1. **Start the Flask Development Server**:
   ```bash
   python server.py
   ```

2. **Access the Web Interface**:
   Open your browser and navigate to:
   ```text
   http://localhost:5000/
   ```

3. **Analyze Emotion**:
   Enter any sentence into the text box and click **Run Sentiment Analysis**. The predicted breakdown across the five emotions and the dominant emotion will be displayed.

---

## API Specification

### Endpoint: `/emotionDetector`
- **Method**: `GET`
- **Query Parameter**: `textToAnalyze` (string)
- **Response Format (Success)**:
  ```text
  For the given statement, the system response is 'anger': 0.002, 'disgust': 0.001, 'fear': 0.001, 'joy': 0.985 and 'sadness': 0.005. The dominant emotion is joy.
  ```
- **Response Format (Error / Blank Input)**:
  ```text
  Invalid text! Please try again!
  ```

---

## Static Code Analysis

Code quality is enforced using `pylint`:

```bash
python -m pylint server.py
python -m pylint EmotionDetection/emotion_detection.py
```

Both modules achieve a **10.00/10** rating adhering to strict PEP 8 guidelines.
