# Student Performance Prediction

## Overview

The Student Performance Prediction project is a web application that predicts the academic performance of students based on various input features. The project leverages machine learning to provide predictions and is built using HTML for the front end and Flask for the back end.

## Features

- User-friendly interface for entering student details.
- Predicts student performance based on input features.
- Displays the predicted performance score on the web page.

## Tech Stack

- **Front End:** HTML
- **Back End:** Flask
- **Machine Learning:** Scikit-learn (or any other library you used)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/govardhan-06/Student-Performance-Prediction.git
   cd Student-Performance-Prediction
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**

   ```bash
   python app.py
   ```

5. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. **Input Features:**

   - Enter the details of the student, such as study hours, attendance, previous grades, etc.

2. **Predict Performance:**

   - Click on the 'Predict' button to get the predicted performance score.

3. **View Results:**
   - The predicted performance score will be displayed on the screen.

## Model Training

1. **Prepare Data:**

   - Collect and preprocess the dataset containing student details and performance scores.

2. **Train Model:**

   - Train a machine learning model using the dataset and save the model as `model.pkl`.

3. **Integrate Model:**
   - Load the trained model in `applicaton.py` and use it to make predictions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Acknowledgments

- Thanks to all contributors and the open-source community for their valuable input and support.
