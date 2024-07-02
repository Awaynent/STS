from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy database of registered students with IDs
students = [
    {'name': 'Johnpaul Lintag', 'id': '001'},
    {'name': 'Luyhien Sidlacan', 'id': '002'},
    {'name': 'Aile John Tabao', 'id': '003'},
    {'name': 'Johnlloyd Precia', 'id': '004'},
    {'name': 'John Rudolp Ultra', 'id': '005'},
    {'name': 'Lintag', 'id': '006'},
    {'name': 'Sidlacan', 'id': '007'},
    {'name': 'Tabao', 'id': '008'},
    {'name': 'Precia', 'id': '009'},
    {'name': 'Ultra', 'id': '010'},
    {'name': 'lintag', 'id': '011'},
    {'name': 'sidlacan', 'id': '012'},
    {'name': 'tabao', 'id': '013'},
    {'name': 'precia', 'id': '014'},
    {'name': 'ultra', 'id': '015'}
]

# Dummy schedule data
schedules = {
    'Sunday': [],
    'Monday': [{'name': 'GNED 03', 'time': '4 PM - 5 PM', 'room': 'TBA'}],
    'Tuesday': [
        {'name': 'ITEC 50A', 'time': '7 AM - 11 AM', 'room': 'CL1'},
        {'name': 'GNED 01', 'time': '1 PM - 3 PM', 'room': '121'},
        {'name': 'GNED 03', 'time': '3 PM - 6 PM', 'room': 'TBA'}
    ],
    'Wednesday': [
        {'name': 'ITEC 50A', 'time': '7 AM - 9 AM', 'room': 'CL5'},
        {'name': 'GNED 06', 'time': '9 AM - 12 NN', 'room': '121'},
        {'name': 'FITT 2', 'time': '1 PM - 3 PM', 'room': 'COURT'}
    ],
    'Thursday': [],
    'Friday': [
        {'name': 'DCIT 23A', 'time': '7 AM - 3 PM', 'room': 'A-303'},
        {'name': 'GNED 12', 'time': '3 PM - 4 PM', 'room': '404'}
    ],
    'Saturday': [
        {'name': 'NSTP 2', 'time': '7 AM - 12 NN', 'room': 'TBA'},
        {'name': 'GNED 12', 'time': '5 PM - 7 PM', 'room': '404'}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_registration', methods=['POST'])
def check_registration():
    name = request.form['name']
    if any(student['name'] == name for student in students):
        return f'{name} is a registered student.'
    else:
        return f'{name} is not a registered student.'

@app.route('/masterlist')
def masterlist():
    return render_template('masterlist.html', students=students, schedules=schedules)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
