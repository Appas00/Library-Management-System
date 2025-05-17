from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
CSV_FILE = "Library.csv"


def read_books():
    books = {}
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    books[row[0]] = row[1]
    except FileNotFoundError:
        print(f"{CSV_FILE} not found.")
    return books


def write_books(books):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for book, status in books.items():
            writer.writerow([book, status])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title'].strip()
        books = read_books()
        if title not in books:
            books[title] = "Available"
            write_books(books)
        return redirect('/')
    return render_template('add_book.html')


@app.route('/issue', methods=['GET', 'POST'])
def issue():
    message = None
    if request.method == 'POST':
        title = request.form['title'].strip()
        books = read_books()
        if title in books and books[title] == "Available":
            books[title] = "Issued"
            write_books(books)
            message = f"Book '{title}' has been issued."
        else:
            message = f"Book '{title}' is not available or already issued."
    return render_template('issue_book.html', message=message)


@app.route('/view')
def view():
    books = read_books()
    available = [book for book, status in books.items() if status == "Available"]
    issued = [book for book, status in books.items() if status == "Issued"]
    return render_template('view_books.html', available=available, issued=issued)


@app.route('/search', methods=['GET', 'POST'])
def search():
    result = None
    if request.method == 'POST':
        query = request.form['query'].lower()
        books = read_books()
        result = [[title, status] for title, status in books.items() if query in title.lower()]
    return render_template('search_book.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
