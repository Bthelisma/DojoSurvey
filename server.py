from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSafe'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
    if len(request.form['your_name']) < 1:
        flash("Name and cannot be empty")
    else:
        flash("Your name is {} ".format(request.form['your_name']))
    return render_template('result.html')



app.run(debug=True)
