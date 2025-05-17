📚 Library Management System
![image](https://github.com/user-attachments/assets/ad7d7eec-2461-4d28-a29a-71d6916daa0e)


A simple and visually appealing Library Management System built with Flask and Python, featuring modern UI, animations, and CSV-based data handling.

Features
Add new books to the library

Issue books to users

View available and issued books

Search books by title

Stores data using CSV file (no database required)

Modern UI with CSS animations and 3D effects

Tech Stack
Python – Backend logic
Flask – Web framework
HTML/CSS – Frontend with animations
CSV – Lightweight data storage

Project Structure
library-management/
├── static/
│ └── style.css – CSS animations and styles
├── templates/
│ ├── index.html – Home page
│ ├── add_book.html – Add new books
│ ├── view_books.html – View available & issued books
│ ├── issue_book.html – Issue a book
│ └── search_book.html – Search for books
├── Library.py – Flask app with core logic
├── Library.csv – Book records (title, status)
└── README.md – Project documentation

How to Run
Clone this Repository
git clone https://github.com/yourusername/library-management
cd library-management

(Optional) Create a Virtual Environment
python -m venv venv
source venv/bin/activate (Linux/macOS)
venv\Scripts\activate (Windows)

Install Flask
pip install flask

Run the Flask App
python Library.py

Open your browser and visit
http://127.0.0.1:5000/

Screenshots
![image](https://github.com/user-attachments/assets/e1ab9f17-6bae-403b-8119-9611bd15761b)Quiz App

![image](https://github.com/user-attachments/assets/d9e9ecf9-b664-4055-88e2-64a47a6458b2)
![image](https://github.com/user-attachments/assets/5ba85a98-15d2-4309-b88b-4cfb2056ba69)

Future Improvements
Add login system (admin/user roles)

Replace CSV with SQLite or MySQL

Add return book feature

Track issue/return dates
