
# main.py
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    exp_name = request.form['exp_name']
    variables = request.form.getlist('variables[]')
    metrics = request.form.getlist('metrics[]')
    # Store experiment details in database

    return redirect('/results')

@app.route('/results')
def results():
    experiments = # Query database for all experiments
    return render_template('results.html', experiments=experiments)

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

if __name__ == '__main__':
    app.run()
