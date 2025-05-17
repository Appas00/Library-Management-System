![image](https://github.com/user-attachments/assets/e1ab9f17-6bae-403b-8119-9611bd15761b)Quiz App
A simple, interactive quiz web application built using Python (Flask), HTML, CSS, and optionally JavaScript. This app reads quiz data from a CSV file and dynamically generates questions for users.

Features:

Load quiz questions from a CSV file

Track and display scores

Responsive user interface
![image](https://github.com/user-attachments/assets/ad7d7eec-2461-4d28-a29a-71d6916daa0e)

![image](https://github.com/user-attachments/assets/d9e9ecf9-b664-4055-88e2-64a47a6458b2)
![image](https://github.com/user-attachments/assets/5ba85a98-15d2-4309-b88b-4cfb2056ba69)


Easy to customize and expand

Built with Flask (Python web framework)

Technologies Used:

Python 3

Flask

HTML5 & CSS3

CSV for question storage

Project Structure:
Quiz App/
├── static/
│ ├── css/
│ └── js/
├── templates/
│ ├── index.html
│ └── result.html
├── Quiz.py
├── questions.csv
├── README.md
└── requirements.txt

Getting Started:

Clone the repository:
git clone https://github.com/Appas00/Quiz-app.git
cd Quiz-app

Create a virtual environment:
python -m venv venv
venv\Scripts\activate (for Windows)
source venv/bin/activate (for macOS/Linux)

Install dependencies:
pip install flask

Run the app:
python Quiz.py

Open your browser and go to:
http://localhost:5000/

CSV Format (questions.csv):
question,option1,option2,option3,option4,correct_answer
What is the capital of France?,Paris,London,Berlin,Madrid,Paris

Contributing:
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

License:
This project is open source and available under the MIT License.

Author:
Appas M
GitHub: https://github.com/Appas00



