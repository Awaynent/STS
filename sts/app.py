from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy database of registered names
registered_names = [
    'Johnpaul Lintag', 'Luyhien Sidlacan', 'Aile John Tabao',
    'Johnlloyd Precia', 'John Rudolp Ultra', 'Lintag', 'Sidlacan',
    'Tabao', 'Precia', 'Ultra', 'lintag', 'sidlacan', 'tabao', 'precia', 'ultra'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_registration', methods=['POST'])
def check_registration():
    name = request.form['name']
    if name in registered_names:
        return f'{name} is a registered student.'
    else:
        return f'{name} is not a registered student.'

# This block is only used when running the application directly for development.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
